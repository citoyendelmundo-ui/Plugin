# Lake Michigan surf alerts (`lmsurf`)

This tool finds surfable windows at specific Lake Michigan beaches far enough ahead to travel for them. It also measures how often it's right at each lead time, so you learn how far ahead to trust it.

## The frame

Lake Michigan has **no groundswell**. Every rideable wave is local wind-sea, so "will Grand Haven be good Saturday?" is really three questions:

1. **Wind forecast:** will a strong enough wind blow from the right direction for long enough? This sets your lead time. It's a synoptic weather-model question, decent at 3–5 days and good at 1–2.
2. **Fetch geometry:** given that wind, how much open water lies upwind of *this* beach? A W wind lights up Michigan, a NNE wind lights up Chicago, and a NE/E wind lights up Sheboygan. This part is deterministic.
3. **Quality and access:** is the wind onshore and blown out, or is there a clean-up window after it drops or turns offshore? Is that window in daylight, and can you get there before it starts?

So "reliable" can't mean "always right 5 days out." It means **calibrated**: the tool says how sure it is, gets surer as the event approaches, and keeps score so you can check that its confidence is earned.

## How it works

| Layer | What it does | Source |
|---|---|---|
| Wind ensemble | Hourly 10 m wind for 7 days from 4 independent models (GFS, ECMWF, ICON, GEM) | Open-Meteo forecast API (free, no key) |
| Wave physics | Each model's wind becomes nearshore Hs/Tp via fetch- and duration-limited growth (USACE CEM), with ray-cast fetch from a digitised shoreline, beach-orientation filtering and post-storm decay | `lmsurf/physics.py`, `lmsurf/geo.py` |
| Official cross-check | NWS gridded wave height (fed by NOAA's GLWU Great Lakes wave model). A contradiction from it blocks a GO | api.weather.gov |
| Rating | Size, period and wind (offshore/light, cross, onshore and its strength) give flat/poor/fair/good/epic. Daylight only | `lmsurf/engine.py` |
| Tiers | **GO**: ≤48 h out, ≥75% of models agree, NWS doesn't contradict. **WATCH**: ≤5 days out, ≥50% agree. **OUTLOOK**: anything else | |
| Reachability | A window is only alerted if it starts after `drive_hours + prep_buffer_hours` from now | `spots.json` |
| Delivery | 4×/day GitHub Action updates a pinned issue. New or upgraded GO/WATCH windows post a comment (GitHub email/mobile notification), plus optional phone push via [ntfy](https://ntfy.sh) | `.github/workflows/surf.yml` |
| Scorekeeping | Every run logs its forecast. NDBC buoy observations and your own session reports score it by lead time | `lmsurf/verify.py`, `data/scorecard.md` |

The wind ensemble does the main work, for two reasons: it reaches further ahead than the official wave grids, and NWS nearshore wave grids are typically issued only ~Apr–Dec, while Lake Michigan's best surf runs Oct–Apr. NWS waves serve as a veto, not a dependency.

## Setup (≈10 minutes)

1. **Merge this branch to the default branch.** GitHub only runs scheduled workflows from the default branch.
2. **`spots.json` is preconfigured** for home at 5701 N Sheridan Rd (Edgewater). Hollywood/Osterman is the home break. Each spot carries:
   - `drive_hours`: door-to-water time from Edgewater in normal traffic. Adjust for rush hour if you'd be leaving then.
   - `prep_buffer_hours`: notice needed on top of the drive. It's 1 h for the home break, up to ~10 h for the Leelanau trips, where you'd need to clear a workday.
   - `window` (optional, default 75°): how far off `facing` a wind can blow and still send waves in. Leave it at the default until the scorecard says otherwise.
   - Worth-the-drive threshold: `min_height_ft` 2.0, `min_period_s` 4.5, `min_rating` fair.
3. **Phone push (optional):** install the ntfy app, subscribe to a hard-to-guess topic name, and add it as the repo secret `NTFY_TOPIC`. Without it you still get GitHub issue notifications.
4. **Run it once:** Actions → *Lake Michigan surf* → Run workflow → `run`.

## Keeping score

After every beach check, **including skunks and flat days**, log what you found:

- From your phone: Actions → *Lake Michigan surf* → Run workflow → `log-session`, then fill in spot, local time and rating.
- From a laptop: `python -m lmsurf log-session --spot grand-haven --time 2026-10-06T08:00 --rating good --face-ft 4`

**Webcam checks count.** Every time an alert fires, or a flat call looks suspicious, look at a public cam for that beach and log what you see (add `--notes cam`). That builds the per-spot record without driving, and it's how the tool learns which beaches its direction model gets wrong.

`data/scorecard.md` then shows, per lead-time bucket:
- **vs. buoys (45007, 45002):** bias and error of the wave model in feet. If the bias is consistently +1 ft, set `height_scale` (e.g. 0.8) in `spots.json`.
- **vs. your sessions:** hits, misses and false alarms. This is the real test of usefulness.

- **Per spot, "where the model is wrong":** misses and false alarms tallied by the wind direction that was forecast. Missed surf bunched on one direction (e.g. "Missed surf on winds from NNE×4" at Michigan City) means the spot works on winds the model rules out. Widen that spot's `window` or rotate `facing` toward that side. False alarms bunched on one direction mean the reverse. Treat ~3 reports in the same direction as a pattern, and change one setting at a time.

**Ways this could turn out to be wrong, and what each would mean:**
- WATCH-tier calls at 72–120 h verify less than about a third of the time. The 5-day horizon is noise, so raise the WATCH threshold or shorten it to 72 h.
- You keep finding surf the tool rated flat (misses). Your `facing`/window values or `min_*` thresholds are off for that spot, or the spot works on a direction the fetch model undersells (e.g. refraction around a pier).
- Buoy MAE is above ~1.5 ft at 0–24 h. The physics is mis-specified for this lake, so depend on the NWS/GLWU grid more and the wind ensemble less.
- GO calls verify no better than WATCH calls. The tiering adds nothing, so simplify it.

## Known limits

- **Shoreline is hand-digitised** (~5–10 km error). Fetch is good to roughly ±10%. Green Bay and the Straits are treated as closed.
- **Deep-water growth formulas.** There's no shoaling, breaking or refraction, and piers and sandbars aren't modelled. `height_scale` plus the scorecard is the correction path.
- **Spot `facing` values are first guesses** from shoreline orientation, not local knowledge. They're the single biggest per-spot accuracy lever, and the per-spot scorecard is how to correct them.
- **NDBC buoys are pulled for winter** (roughly Nov–Apr), so buoy scoring pauses then and session logs carry the load.
- **The code is untested against live APIs.** It was built in a sandbox with no outbound access to NOAA or Open-Meteo. Parsers are written to the documented schemas and unit-tested with fixtures. The first Actions run is the live test, and the report's *Data notes* section will flag any source that comes back empty.

## Development

```
python -m unittest discover -s tests -v   # stdlib only, no installs
python -m lmsurf run                      # needs internet
python -m lmsurf verify
```
