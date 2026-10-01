"""Markdown outlook, alert selection/dedupe, and push notification."""
import json
import os
import urllib.request
from datetime import timedelta
from zoneinfo import ZoneInfo

TIER_ORDER = {"OUTLOOK": 0, "WATCH": 1, "GO": 2}
COMPASS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
           "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]


def compass(deg):
    return "?" if deg is None else COMPASS[int((deg % 360) / 22.5 + 0.5) % 16]


def fmt_t(t, tz):
    return t.astimezone(tz).strftime("%a %b %-d %-I%p").replace("AM", "am").replace("PM", "pm")


def window_row(w, tz):
    nws = "n/a" if w["nws_peak_ft"] is None else f"{w['nws_peak_ft']:.1f} ft"
    leave = fmt_t(w["start"] - timedelta(hours=w["need_h"]), tz) if w["reachable"] else "—"
    return (f"| **{w['tier']}** | {w['name']} | {fmt_t(w['start'], tz)} → {fmt_t(w['end'], tz)} "
            f"| {w['rating']} · {w['peak_ft']:.1f} ft @ {w['peak_tp']:.0f}s "
            f"| {w['wind_kt']:.0f} kt {compass(w['wind_dir'])} ({w['wind_rel']}) "
            f"| {w['agree']:.0%} | {nws} | {leave} |")


HEADER = ("| Tier | Spot | Window | Peak | Wind at peak | Models agree | NWS waves | Start moving by |\n"
          "|---|---|---|---|---|---|---|---|")


def build_report(windows, issued, tz_name, notes):
    tz = ZoneInfo(tz_name)
    reach = sorted([w for w in windows if w["reachable"]],
                   key=lambda w: (-TIER_ORDER[w["tier"]], w["start"]))
    soon = sorted([w for w in windows if not w["reachable"]], key=lambda w: w["start"])
    lines = [f"# Lake Michigan surf outlook — issued {fmt_t(issued, tz)} ({tz_name})", ""]
    if reach:
        lines += ["## Reachable windows", "", HEADER] + [window_row(w, tz) for w in reach] + [""]
    else:
        lines += ["## Reachable windows", "", "_None in the next 7 days at your thresholds._", ""]
    if soon:
        lines += ["## Happening too soon to travel for", "", HEADER] + [window_row(w, tz) for w in soon] + [""]
    lines += [
        "## How to read this",
        "- **GO**: ≤48 h out, ≥75% of wind models produce surf, and the NWS wave grid does not contradict it.",
        "- **WATCH**: ≤5 days out and at least half the models agree. Plan for it, but don't commit yet.",
        "- **OUTLOOK**: a signal that's too far out or too uncertain. Ignore it unless it upgrades.",
        "- Sizes are modelled nearshore significant wave height (Hs). Lake faces usually look like ~1–1.5× Hs.",
        "- *Start moving by* = window start minus drive time and prep buffer.",
        "",
    ]
    if notes:
        lines += ["## Data notes", ""] + [f"- {n}" for n in notes] + [""]
    return "\n".join(lines)


def _key(w, tz):
    return f"{w['spot']}|{w['start'].astimezone(tz).date().isoformat()}"


def select_alerts(windows, state, issued, tz_name):
    """New or upgraded reachable GO/WATCH windows. Mutates and returns state."""
    tz = ZoneInfo(tz_name)
    fresh = []
    for w in windows:
        if not w["reachable"] or w["tier"] == "OUTLOOK":
            continue
        k = _key(w, tz)
        if TIER_ORDER[w["tier"]] > TIER_ORDER.get(state.get(k), -1):
            state[k] = w["tier"]
            fresh.append(w)
    cutoff = (issued.astimezone(tz) - timedelta(days=3)).date().isoformat()
    for k in [k for k in state if k.split("|")[1] < cutoff]:
        del state[k]
    return fresh, state


def alert_text(alerts, tz_name):
    tz = ZoneInfo(tz_name)
    return "\n".join(
        f"{w['tier']}: {w['name']} {fmt_t(w['start'], tz)}–{fmt_t(w['end'], tz)}, "
        f"{w['rating']} {w['peak_ft']:.1f}ft@{w['peak_tp']:.0f}s, wind {w['wind_kt']:.0f}kt "
        f"{compass(w['wind_dir'])}, {w['agree']:.0%} models agree"
        for w in sorted(alerts, key=lambda w: w["start"]))


def push_ntfy(topic, alerts, tz_name):
    if not topic or not alerts:
        return False
    top = max(alerts, key=lambda w: TIER_ORDER[w["tier"]])["tier"]
    req = urllib.request.Request(
        f"https://ntfy.sh/{topic}", data=alert_text(alerts, tz_name).encode(),
        headers={"Title": f"Lake Michigan surf {top}", "Tags": "ocean",
                 "Priority": "high" if top == "GO" else "default"})
    urllib.request.urlopen(req, timeout=20)
    return True


def load_json(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def save_json(path, obj):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump(obj, f, indent=1, sort_keys=True)
