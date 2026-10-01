"""Fetch- and duration-limited wind-wave growth (USACE Coastal Engineering Manual, Part II-2).

Lake Michigan has no remote swell: every wave is local wind-sea, so wave height
is a function of wind speed, how far that wind has blown over water (fetch), and
how long it has blown (duration). This module turns an hourly wind series into an
hourly nearshore wave estimate for one spot.
"""
import math

from .geo import angdiff, lookup_fetch

G = 9.81
M_TO_FT = 3.28084

# A wind is treated as "the same event" while it stays within this many degrees.
DIRECTION_TOLERANCE = 30
MAX_DURATION_H = 48
# Lake Michigan wind-sea decays quickly once forcing stops (hours).
DECAY_TAU_H = 5.0


def _ustar(u10):
    cd = 0.001 * (1.1 + 0.035 * u10)
    return u10 * math.sqrt(cd)


def grow(u10, fetch_km, duration_h):
    """Significant height (m) and peak period (s) for steady wind u10 (m/s)."""
    if u10 <= 0.5 or fetch_km <= 0 or duration_h <= 0:
        return 0.0, 0.0
    us = _ustar(u10)
    x_fetch = fetch_km * 1000.0 * G / us ** 2
    # Equivalent fetch from duration (CEM II-2-38): gX/u*^2 = 5.23e-3 (g t / u*)^1.5
    x_dur = 5.23e-3 * (G * duration_h * 3600.0 / us) ** 1.5
    x = min(x_fetch, x_dur)
    h = 4.13e-2 * math.sqrt(x) * us ** 2 / G
    t = 0.651 * x ** (1.0 / 3.0) * us / G
    # Fully developed limit
    h = min(h, 211.5 * us ** 2 / G)
    t = min(t, 239.8 * us / G)
    return h, t


def sustained(winds, i):
    """Hours (and mean speed) the wind at index i has blown from roughly the same direction."""
    d0 = winds[i][1]
    speeds = []
    j = i
    while j >= 0 and len(speeds) < MAX_DURATION_H:
        sp, dr = winds[j]
        if sp is None or dr is None or angdiff(dr, d0) > DIRECTION_TOLERANCE:
            break
        speeds.append(sp)
        j -= 1
    if not speeds:
        return 0, 0.0
    return len(speeds), sum(speeds) / len(speeds)


def wave_series(winds, fetch_table, facing=None, window=75):
    """Hourly wave estimates at a spot.

    winds: list of (speed m/s, from-direction deg) at hourly steps.
    facing: bearing the beach looks out to; None for an open-water point (buoy).
    window: waves from more than this many degrees off `facing` don't reach the beach.
    Returns list of dicts {hs_m, tp_s, dir} (dir = direction waves come from).
    """
    out = []
    prev_h, prev_t, prev_d = 0.0, 0.0, None
    decay = math.exp(-1.0 / DECAY_TAU_H)
    for i, (sp, dr) in enumerate(winds):
        h_gen, t_gen = 0.0, 0.0
        if sp is not None and dr is not None:
            dur, mean_sp = sustained(winds, i)
            # Use the event-mean speed, but let a fresh gust-up count immediately.
            u = max(mean_sp, 0.85 * sp)
            fetch = lookup_fetch(fetch_table, dr)
            h_gen, t_gen = grow(u, fetch, dur)
            if facing is not None:
                off = angdiff(dr, facing)
                h_gen = 0.0 if off >= window else h_gen * math.sqrt(math.cos(math.radians(off)))
        h_dec, t_dec = prev_h * decay, prev_t * 0.985
        if h_gen >= h_dec:
            h, t, d = h_gen, max(t_gen, t_dec if h_dec > 0.5 * h_gen else 0.0), dr
        else:
            h, t, d = h_dec, t_dec, prev_d
        out.append({"hs_m": h, "tp_s": t, "dir": d})
        prev_h, prev_t, prev_d = h, t, d
    return out
