"""lmsurf: Lake Michigan surf window finder.

  python -m lmsurf run            fetch forecasts, write report, log, alert
  python -m lmsurf log-session    record what you actually found at a beach
  python -m lmsurf verify         score past forecasts against buoys and sessions
"""
import argparse
import json
import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

from . import engine, geo, report, sources, verify


def load_config(path):
    with open(path) as f:
        cfg = json.load(f)
    cfg["preferences"].setdefault("timezone", "America/Chicago")
    return cfg


def cmd_run(args):
    cfg = load_config(args.config)
    prefs, models = cfg["preferences"], cfg["models"]
    issued = verify.now_utc()
    notes, windows, no_nws = [], [], []
    model_hits = {}

    for spot in cfg["spots"]:
        lat, lon = geo.offset(spot["lat"], spot["lon"], spot["facing"], prefs["offshore_km"])
        try:
            times, winds, sun = sources.fetch_openmeteo(lat, lon, models)
        except Exception as e:  # one bad spot must not sink the run
            notes.append(f"{spot['name']}: wind fetch failed ({e.__class__.__name__}); skipped.")
            continue
        for m in winds:
            model_hits[m] = model_hits.get(m, 0) + 1
        nws = sources.fetch_nws_waves(lat, lon)
        if not nws:
            no_nws.append(spot["id"])
        hours, wins = engine.analyse_spot(spot, prefs, times, winds, sun, nws, issued)
        windows += wins
        verify.log_forecast(args.data, issued, spot["id"], hours)

    for buoy in cfg.get("buoys", []):
        try:
            times, winds, _ = sources.fetch_openmeteo(buoy["lat"], buoy["lon"], models)
            tbl = geo.fetch_table(buoy["lat"], buoy["lon"])
            hours = engine.hourly_ensemble(times, winds, tbl, None, prefs.get("height_scale", 1.0))
            verify.log_forecast(args.data, issued, buoy["id"], hours)
        except Exception as e:
            notes.append(f"Buoy {buoy['id']} model run failed ({e.__class__.__name__}).")
        obs = sources.fetch_ndbc(buoy["id"])
        verify.merge_obs(args.data, buoy["id"], obs)
        if not obs:
            notes.append(f"NDBC {buoy['id']}: no observations (buoys are pulled for winter).")

    if no_nws:
        which = "all spots" if len(no_nws) == len(cfg["spots"]) else ", ".join(no_nws)
        notes.append(f"No NWS wave grid for {which}, so these use the wind-model ensemble only "
                     "(normal outside ~Apr–Dec). GO is not cross-checked against NWS for them.")
    missing = [m for m in models if m not in model_hits]
    if missing:
        notes.append(f"Wind models returned no data: {', '.join(missing)}. Agreement uses the rest.")

    tz = prefs["timezone"]
    md = report.build_report(windows, issued, tz, notes)
    os.makedirs(args.data, exist_ok=True)
    with open(os.path.join(args.data, "outlook.md"), "w") as f:
        f.write(md)

    state_path = os.path.join(args.data, "alert_state.json")
    alerts, state = report.select_alerts(windows, report.load_json(state_path, {}), issued, tz)
    report.save_json(state_path, state)
    alert_path = os.path.join(args.data, "alerts.txt")
    if alerts:
        with open(alert_path, "w") as f:
            f.write(report.alert_text(alerts, tz) + "\n")
        try:
            report.push_ntfy(os.environ.get("NTFY_TOPIC"), alerts, tz)
        except Exception as e:
            print(f"ntfy push failed: {e}", file=sys.stderr)
    elif os.path.exists(alert_path):
        os.remove(alert_path)
    print(md)
    return 0


def cmd_log_session(args):
    cfg = load_config(args.config)
    ids = {s["id"] for s in cfg["spots"]}
    if args.spot not in ids:
        sys.exit(f"unknown spot {args.spot!r}; choose from: {', '.join(sorted(ids))}")
    t = datetime.fromisoformat(args.time)
    if t.tzinfo is None:
        t = t.replace(tzinfo=ZoneInfo(cfg["preferences"]["timezone"]))
    verify.log_session(args.data, t, args.spot, args.rating, args.face_ft or "", args.notes or "")
    print(f"logged {args.rating} at {args.spot} {t.isoformat()}")
    return 0


def cmd_verify(args):
    prefs = load_config(args.config)["preferences"]
    print(verify.score(args.data, prefs["min_height_ft"], prefs["min_rating"]))
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="lmsurf", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--config", default="spots.json")
    p.add_argument("--data", default="data")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("run").set_defaults(fn=cmd_run)
    s = sub.add_parser("log-session")
    s.add_argument("--spot", required=True)
    s.add_argument("--time", required=True, help="ISO time; local timezone from config if no offset")
    s.add_argument("--rating", required=True, choices=engine.RATINGS)
    s.add_argument("--face-ft", type=float)
    s.add_argument("--notes")
    s.set_defaults(fn=cmd_log_session)
    sub.add_parser("verify").set_defaults(fn=cmd_verify)
    args = p.parse_args(argv)
    return args.fn(args)
