"""Data fetchers. Stdlib only so the GitHub Action needs no install step.

- Open-Meteo forecast API: hourly 10 m wind from several independent NWP models
  (GFS, ECMWF, ICON, GEM). Model spread is our confidence signal.
- NWS api.weather.gov gridpoints: the official forecaster wave grid (waveHeight),
  which ingests NOAA's Great Lakes wave model (GLWU). Typically issued ~Apr-Dec.
- NDBC realtime2: buoy observations, used only to score past forecasts.
"""
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

USER_AGENT = "lake-michigan-surf-alert (https://github.com/citoyendelmundo-ui/plugin)"


def _get(url, accept="application/json", tries=3):
    last = None
    for k in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise
            last = e
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
        time.sleep(2 ** (k + 1))
    raise last


def parse_time(s):
    """ISO time -> aware UTC datetime. Bare times (Open-Meteo with timezone=GMT) are UTC."""
    dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


# ---------------------------------------------------------------- Open-Meteo

def openmeteo_url(lat, lon, models, forecast_days=7, past_days=2):
    q = {
        "latitude": f"{lat:.4f}",
        "longitude": f"{lon:.4f}",
        "hourly": "wind_speed_10m,wind_direction_10m,wind_gusts_10m",
        "daily": "sunrise,sunset",
        "models": ",".join(models),
        "wind_speed_unit": "ms",
        "timezone": "GMT",
        "forecast_days": forecast_days,
        "past_days": past_days,
    }
    return "https://api.open-meteo.com/v1/forecast?" + urllib.parse.urlencode(q)


def parse_openmeteo(doc, models):
    """-> (times, {model: [(speed, dir), ...]}, [(sunrise, sunset), ...])"""
    hourly = doc["hourly"]
    times = [parse_time(t) for t in hourly["time"]]
    winds = {}
    for m in models:
        sp = hourly.get(f"wind_speed_10m_{m}")
        dr = hourly.get(f"wind_direction_10m_{m}")
        if sp is None and len(models) == 1:
            sp, dr = hourly.get("wind_speed_10m"), hourly.get("wind_direction_10m")
        if sp is None or dr is None or all(v is None for v in sp):
            continue
        winds[m] = list(zip(sp, dr))
    sun = []
    daily = doc.get("daily") or {}
    for key in daily:
        if key.startswith("sunrise"):
            rises = daily[key]
            sets = daily[key.replace("sunrise", "sunset")]
            sun = [(parse_time(a), parse_time(b)) for a, b in zip(rises, sets) if a and b]
            break
    return times, winds, sun


def fetch_openmeteo(lat, lon, models, **kw):
    doc = json.loads(_get(openmeteo_url(lat, lon, models, **kw)))
    return parse_openmeteo(doc, models)


# ---------------------------------------------------------------- NWS

_DUR = re.compile(r"P(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?)?")


def _duration_hours(s):
    m = _DUR.fullmatch(s)
    if not m:
        return 1
    d, h, mi = (int(x) if x else 0 for x in m.groups())
    return max(1, d * 24 + h + (1 if mi >= 30 else 0))


def expand_layer(layer):
    """NWS gridpoint layer -> {hour datetime: value}, converted to metres if needed."""
    scale = 0.3048 if layer.get("uom", "").endswith(":ft") else 1.0
    out = {}
    for v in layer.get("values", []):
        if v.get("value") is None:
            continue
        start_s, dur_s = v["validTime"].split("/")
        start = parse_time(start_s)
        for k in range(_duration_hours(dur_s)):
            out[start + timedelta(hours=k)] = v["value"] * scale
    return out


def fetch_nws_waves(lat, lon):
    """-> {hour: waveHeight m} or {} if the point has no marine wave grid."""
    try:
        pt = json.loads(_get(f"https://api.weather.gov/points/{lat:.4f},{lon:.4f}",
                             accept="application/geo+json"))
        grid_url = pt["properties"]["forecastGridData"]
        grid = json.loads(_get(grid_url, accept="application/geo+json"))
    except (urllib.error.HTTPError, urllib.error.URLError, KeyError, TimeoutError):
        return {}
    return expand_layer(grid["properties"].get("waveHeight", {}))


# ---------------------------------------------------------------- NDBC

def parse_ndbc(text):
    """realtime2 stdmet text -> list of {time, wvht_m, dpd_s, mwd, wspd, wdir}."""
    rows = []
    cols = None
    for line in text.splitlines():
        if line.startswith("#"):
            if cols is None:
                cols = line.lstrip("#").split()
            continue
        if not cols:
            continue
        f = dict(zip(cols, line.split()))
        try:
            t = datetime(int(f["YY"]), int(f["MM"]), int(f["DD"]), int(f["hh"]), int(f["mm"]),
                         tzinfo=timezone.utc)
        except (KeyError, ValueError):
            continue

        def num(k):
            v = f.get(k, "MM")
            return None if v == "MM" else float(v)

        rows.append({"time": t, "wvht_m": num("WVHT"), "dpd_s": num("DPD"), "mwd": num("MWD"),
                     "wspd": num("WSPD"), "wdir": num("WDIR")})
    return rows


def fetch_ndbc(station):
    try:
        return parse_ndbc(_get(f"https://www.ndbc.noaa.gov/data/realtime2/{station}.txt",
                               accept="text/plain"))
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        return []
