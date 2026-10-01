"""The disconfirmation loop: log every forecast, collect ground truth, score by lead time.

Ground truth comes from two places:
- NDBC mid-lake buoys (objective wave height, but offshore and pulled for winter).
- Your own session log (the only truth about "was it surfable at that beach").
The output answers: at N hours of lead time, how often did a predicted window
verify, and how often did surf show up that the tool missed?
"""
import csv
import glob
import os
from datetime import datetime, timedelta, timezone

from .engine import RATINGS, rating_index
from .sources import parse_time

LOG_FIELDS = ["issued", "spot", "valid", "lead_h", "hs_ft", "tp_s", "rating", "agree", "nws_ft"]
OBS_FIELDS = ["time", "wvht_m", "dpd_s", "mwd", "wspd", "wdir"]
SESSION_FIELDS = ["time", "spot", "rating", "face_ft", "notes"]
BUCKETS = [(0, 24), (24, 48), (48, 72), (72, 120), (120, 999)]


def _bucket(lead):
    for lo, hi in BUCKETS:
        if lo <= lead < hi:
            return f"{lo}-{hi}h" if hi < 999 else f"{lo}h+"
    return None


def _append(path, fields, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if new:
            w.writeheader()
        w.writerows(rows)


def log_forecast(data_dir, issued, spot_id, hours, every_h=6, max_lead_h=168):
    """Append a thinned copy of this run's hourly forecast (every `every_h` UTC hours)."""
    rows = []
    for h in hours:
        lead = (h["time"] - issued).total_seconds() / 3600
        if lead < 0 or lead > max_lead_h or h["time"].hour % every_h:
            continue
        rows.append({
            "issued": issued.isoformat(), "spot": spot_id, "valid": h["time"].isoformat(),
            "lead_h": round(lead), "hs_ft": round(h["hs_ft"], 2), "tp_s": round(h["tp_s"], 1),
            "rating": RATINGS[h["rating"]] if "rating" in h else "",
            "agree": round(h.get("agree", 0), 2),
            "nws_ft": "" if h.get("nws_ft") is None else round(h["nws_ft"], 2),
        })
    _append(os.path.join(data_dir, "log", f"{issued:%Y-%m}.csv"), LOG_FIELDS, rows)
    return len(rows)


def merge_obs(data_dir, station, rows):
    path = os.path.join(data_dir, "obs", f"{station}.csv")
    seen = set()
    if os.path.exists(path):
        with open(path) as f:
            seen = {r["time"] for r in csv.DictReader(f)}
    new = [{k: (r[k].isoformat() if k == "time" else ("" if r[k] is None else r[k])) for k in OBS_FIELDS}
           for r in rows if r["time"].isoformat() not in seen and r["wvht_m"] is not None]
    new.sort(key=lambda r: r["time"])
    _append(path, OBS_FIELDS, new)
    return len(new)


def log_session(data_dir, time, spot, rating, face_ft="", notes=""):
    if rating not in RATINGS:
        raise ValueError(f"rating must be one of {RATINGS}")
    _append(os.path.join(data_dir, "sessions.csv"), SESSION_FIELDS,
            [{"time": time.astimezone(timezone.utc).isoformat(), "spot": spot, "rating": rating,
              "face_ft": face_ft, "notes": notes}])


def _read(path_glob):
    rows = []
    for p in sorted(glob.glob(path_glob)):
        with open(p) as f:
            rows += list(csv.DictReader(f))
    return rows


def _nearest(series, t, tol):
    best = None
    for st, v in series:
        d = abs((st - t).total_seconds())
        if d <= tol.total_seconds() and (best is None or d < best[0]):
            best = (d, v)
    return None if best is None else best[1]


def score(data_dir, min_height_ft=2.0, min_rating="fair"):
    """Return a markdown scorecard."""
    log = _read(os.path.join(data_dir, "log", "*.csv"))
    out = ["# Forecast scorecard", ""]

    # --- Buoys: objective height skill of the wind->wave model.
    out += ["## Wave model vs. NDBC buoys", "",
            "| Buoy | Lead | n | Bias (ft) | MAE (ft) | Hit | Miss | False alarm |",
            "|---|---|---|---|---|---|---|---|"]
    any_buoy = False
    for path in sorted(glob.glob(os.path.join(data_dir, "obs", "*.csv"))):
        station = os.path.basename(path)[:-4]
        obs = [(parse_time(r["time"]), float(r["wvht_m"]) * 3.28084) for r in _read(path) if r["wvht_m"]]
        stats = {}
        for r in log:
            if r["spot"] != station:
                continue
            o = _nearest(obs, parse_time(r["valid"]), timedelta(minutes=40))
            if o is None:
                continue
            b = _bucket(float(r["lead_h"]))
            s = stats.setdefault(b, {"n": 0, "err": 0.0, "abs": 0.0, "hit": 0, "miss": 0, "fa": 0})
            p = float(r["hs_ft"])
            s["n"] += 1
            s["err"] += p - o
            s["abs"] += abs(p - o)
            ps, os_ = p >= min_height_ft, o >= min_height_ft
            s["hit"] += ps and os_
            s["miss"] += os_ and not ps
            s["fa"] += ps and not os_
        for b in [_bucket(lo) for lo, _ in BUCKETS]:
            if b in stats:
                s = stats[b]
                any_buoy = True
                out.append(f"| {station} | {b} | {s['n']} | {s['err'] / s['n']:+.1f} | "
                           f"{s['abs'] / s['n']:.1f} | {s['hit']} | {s['miss']} | {s['fa']} |")
    if not any_buoy:
        out.append("| — | — | 0 | | | | | |")

    # --- Sessions: did the tool's call match what you found at the beach?
    sessions = _read(os.path.join(data_dir, "sessions.csv"))
    out += ["", "## Forecast vs. your session reports", "",
            "| Lead | Reports | Hit | Miss | False alarm | Correct flat |", "|---|---|---|---|---|---|"]
    thr = rating_index(min_rating)
    table = {}
    for s in sessions:
        t = parse_time(s["time"])
        observed = rating_index(s["rating"]) >= thr
        by_issue = {}
        for r in log:
            if r["spot"] != s["spot"]:
                continue
            if abs((parse_time(r["valid"]) - t).total_seconds()) > 3 * 3600:
                continue
            by_issue.setdefault(r["issued"], r)
        for r in by_issue.values():
            lead = (t - parse_time(r["issued"])).total_seconds() / 3600
            if lead < 0:
                continue
            b = _bucket(lead)
            c = table.setdefault(b, {"n": 0, "hit": 0, "miss": 0, "fa": 0, "cn": 0})
            pred = r["rating"] in RATINGS and rating_index(r["rating"]) >= thr
            c["n"] += 1
            c["hit"] += pred and observed
            c["miss"] += observed and not pred
            c["fa"] += pred and not observed
            c["cn"] += not pred and not observed
    for b in [_bucket(lo) for lo, _ in BUCKETS]:
        if b in table:
            c = table[b]
            out.append(f"| {b} | {c['n']} | {c['hit']} | {c['miss']} | {c['fa']} | {c['cn']} |")
    if not table:
        out.append("| — | 0 | | | | |")
    out += ["", "_Log skunks and flat checks too. A log of only good sessions can't show false alarms._", ""]
    return "\n".join(out)


def now_utc():
    return datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
