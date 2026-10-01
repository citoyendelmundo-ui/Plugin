"""Turn raw winds + official wave grids into rated, tiered surf windows per spot."""
import math
import statistics
from datetime import timedelta

from . import geo, physics

RATINGS = ["flat", "poor", "fair", "good", "epic"]
MS_TO_KT = 1.94384


def rating_index(name):
    return RATINGS.index(name)


def wind_relation(wind_from, facing):
    rel = geo.angdiff(wind_from, facing)
    if rel < 60:
        return "onshore"
    if rel <= 120:
        return "cross"
    return "offshore"


def rate_hour(h_ft, tp, wind_kt, wind_dir, facing, prefs):
    if h_ft < prefs["min_height_ft"] or tp < prefs["min_period_s"]:
        return 0
    size = 1 if h_ft < 3 else 2 if h_ft < 5 else 3
    period = 1 if tp >= 6.5 else 0
    rel = wind_relation(wind_dir, facing) if wind_dir is not None else "cross"
    if wind_kt < 6 or (rel == "offshore" and wind_kt <= 20):
        wind = 1
    elif rel == "onshore":
        wind = 0 if wind_kt < 12 else -1 if wind_kt <= 22 else -2
    elif rel == "cross":
        wind = 0 if wind_kt < 12 else -1
    else:
        wind = -1  # strong offshore: holds waves up but hard to paddle into
    return max(1, min(size + period + wind, 4 if h_ft >= 5 else 3))


def circular_mean(dirs):
    s = sum(math.sin(math.radians(d)) for d in dirs)
    c = sum(math.cos(math.radians(d)) for d in dirs)
    return math.degrees(math.atan2(s, c)) % 360


def is_daylight(t, sun):
    return any(rise - timedelta(minutes=30) <= t <= sset + timedelta(minutes=15) for rise, sset in sun)


def hourly_ensemble(times, model_winds, fetch_tbl, facing, height_scale=1.0, window=75):
    """Per-hour ensemble: median wave + per-model waves + consensus wind.

    height_scale is a calibration multiplier; set it from `lmsurf verify` bias.
    """
    ft = physics.M_TO_FT * height_scale
    per_model = {m: physics.wave_series(w, fetch_tbl, facing, window) for m, w in model_winds.items()}
    hours = []
    for i, t in enumerate(times):
        waves = [per_model[m][i] for m in per_model]
        winds = [model_winds[m][i] for m in model_winds if model_winds[m][i][0] is not None
                 and model_winds[m][i][1] is not None]
        if not waves:
            continue
        hours.append({
            "time": t,
            "hs_ft": statistics.median(w["hs_m"] for w in waves) * ft,
            "tp_s": statistics.median(w["tp_s"] for w in waves),
            "model_hs_ft": {m: per_model[m][i]["hs_m"] * ft for m in per_model},
            "model_tp_s": {m: per_model[m][i]["tp_s"] for m in per_model},
            "wind_kt": statistics.median(w[0] for w in winds) * MS_TO_KT if winds else 0.0,
            "wind_dir": circular_mean([w[1] for w in winds]) if winds else None,
        })
    return hours


def analyse_spot(spot, prefs, times, model_winds, sun, nws_waves, now):
    lat, lon = geo.offset(spot["lat"], spot["lon"], spot["facing"], prefs["offshore_km"])
    tbl = spot.get("_fetch") or geo.fetch_table(lat, lon)
    hours = hourly_ensemble(times, model_winds, tbl, spot["facing"], prefs.get("height_scale", 1.0),
                            spot.get("window", 75))
    n_models = max(1, len(model_winds))
    for h in hours:
        h["rating"] = rate_hour(h["hs_ft"], h["tp_s"], h["wind_kt"], h["wind_dir"], spot["facing"], prefs)
        h["agree"] = sum(
            rate_hour(h["model_hs_ft"][m], h["model_tp_s"][m], h["wind_kt"], h["wind_dir"],
                      spot["facing"], prefs) >= rating_index(prefs["min_rating"])
            for m in h["model_hs_ft"]) / n_models
        nws = nws_waves.get(h["time"].replace(minute=0, second=0, microsecond=0))
        h["nws_ft"] = None if nws is None else nws * physics.M_TO_FT
        h["daylight"] = is_daylight(h["time"], sun) if sun else True
    return hours, find_windows(spot, prefs, hours, now)


def find_windows(spot, prefs, hours, now):
    min_r = rating_index(prefs["min_rating"])
    drive = spot.get("drive_hours", prefs["default_drive_hours"])
    need = drive + spot.get("prep_buffer_hours", prefs["prep_buffer_hours"])
    windows, cur = [], []

    def close():
        if len(cur) >= prefs["min_window_hours"]:
            windows.append(summarise(spot, cur, now, need, prefs))
        cur.clear()

    for h in hours:
        if h["time"] < now - timedelta(hours=1):
            continue
        good = h["rating"] >= min_r and (h["daylight"] or not prefs["daylight_only"])
        if good and cur and h["time"] - cur[-1]["time"] > timedelta(hours=1):
            close()
        if good:
            cur.append(h)
        elif cur:
            close()
    if cur:
        close()
    return windows


def summarise(spot, hrs, now, need_hours, prefs):
    start, end = hrs[0]["time"], hrs[-1]["time"] + timedelta(hours=1)
    peak = max(hrs, key=lambda h: (h["rating"], h["hs_ft"]))
    lead = (start - now).total_seconds() / 3600
    agree = sum(h["agree"] for h in hrs) / len(hrs)
    nws_vals = [h["nws_ft"] for h in hrs if h["nws_ft"] is not None]
    if nws_vals:
        nws_ok = sum(v >= prefs["min_height_ft"] for v in nws_vals) >= len(nws_vals) / 2
    else:
        nws_ok = None
    if lead <= 48 and agree >= 0.75 and nws_ok is not False:
        tier = "GO"
    elif lead <= 120 and agree >= 0.5 and nws_ok is not False:
        tier = "WATCH"
    else:
        tier = "OUTLOOK"
    return {
        "spot": spot["id"], "name": spot["name"], "start": start, "end": end,
        "hours": len(hrs), "lead_h": lead, "tier": tier,
        "rating": RATINGS[peak["rating"]], "peak_ft": peak["hs_ft"], "peak_tp": peak["tp_s"],
        "wind_kt": peak["wind_kt"], "wind_dir": peak["wind_dir"],
        "wind_rel": wind_relation(peak["wind_dir"], spot["facing"]) if peak["wind_dir"] is not None else "?",
        "agree": agree, "nws_peak_ft": max(nws_vals) if nws_vals else None, "nws_ok": nws_ok,
        "reachable": lead >= need_hours, "need_h": need_hours,
    }
