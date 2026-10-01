import json
import os
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from unittest import mock

from lmsurf import cli, engine, geo, physics, report, sources, verify

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = json.load(open(os.path.join(ROOT, "spots.json")))
PREFS = CFG["preferences"]
SPOTS = {s["id"]: s for s in CFG["spots"]}
KT = 1 / engine.MS_TO_KT
T0 = datetime(2026, 10, 5, 0, tzinfo=timezone.utc)


def hours(n, start=T0):
    return [start + timedelta(hours=i) for i in range(n)]


def all_day_sun(times):
    return [(times[0] - timedelta(hours=1), times[-1] + timedelta(hours=1))]


class Geometry(unittest.TestCase):
    def test_every_spot_samples_open_water(self):
        for s in CFG["spots"]:
            lat, lon = geo.offset(s["lat"], s["lon"], s["facing"], PREFS["offshore_km"])
            self.assertTrue(geo.in_lake(lat, lon), s["id"])
        for b in CFG["buoys"]:
            self.assertTrue(geo.in_lake(b["lat"], b["lon"]), b["id"])

    def test_known_fetches(self):
        def fetch(spot, d):
            s = SPOTS[spot]
            return geo.effective_fetch_km(*geo.offset(s["lat"], s["lon"], s["facing"], 3), d)
        self.assertTrue(100 < fetch("grand-haven", 270) < 160)   # across to Milwaukee ~130 km
        self.assertTrue(80 < fetch("sheboygan", 90) < 130)       # across to Ludington ~100 km
        self.assertGreater(fetch("chicago-north", 15), 200)      # the long N fetch Chicago lives on
        self.assertLess(fetch("grand-haven", 90), 10)            # offshore wind: no fetch

    def test_islands_block_and_land_is_not_lake(self):
        self.assertFalse(geo.in_lake(45.67, -85.55))  # Beaver Island
        self.assertFalse(geo.in_lake(42.30, -85.60))  # Kalamazoo
        self.assertTrue(geo.in_lake(43.0, -87.0))

    def test_angdiff_and_lookup(self):
        self.assertEqual(geo.angdiff(350, 10), 20)
        self.assertEqual(geo.angdiff(90, 270), 180)
        tbl = {d: float(d) for d in range(0, 360, 5)}
        self.assertAlmostEqual(geo.lookup_fetch(tbl, 7.5), 7.5)
        self.assertAlmostEqual(geo.lookup_fetch(tbl, 357.5), 177.5)  # wraps 355 -> 0


class Physics(unittest.TestCase):
    def test_growth_monotonic_and_limited(self):
        h1, _ = physics.grow(10, 50, 48)
        h2, _ = physics.grow(10, 150, 48)
        h3, _ = physics.grow(15, 150, 48)
        self.assertLess(h1, h2)
        self.assertLess(h2, h3)
        short, _ = physics.grow(15, 150, 2)
        self.assertLess(short, h3)  # duration-limited
        self.assertEqual(physics.grow(0.2, 150, 10), (0.0, 0.0))

    def test_plausible_lake_storm(self):
        h, t = physics.grow(30 * KT, 120, 12)  # 30 kt W across to Grand Haven
        self.assertTrue(2.0 < h < 3.5, h)
        self.assertTrue(5.0 < t < 7.5, t)

    def test_offshore_wind_makes_no_waves_but_swell_decays(self):
        tbl = {d: 130.0 for d in range(0, 360, 5)}
        winds = [(12.0, 270.0)] * 18 + [(4.0, 90.0)] * 12
        s = physics.wave_series(winds, tbl, facing=265)
        self.assertGreater(s[17]["hs_m"], 1.5)
        self.assertGreater(s[18]["hs_m"], 0.0)              # leftover swell, clean-up session
        self.assertLess(s[29]["hs_m"], s[18]["hs_m"] * 0.2)  # decays over ~12 h
        flat = physics.wave_series([(12.0, 90.0)] * 10, tbl, facing=265)
        self.assertTrue(all(h["hs_m"] == 0 for h in flat))


class Parsing(unittest.TestCase):
    def test_openmeteo_multimodel(self):
        doc = {
            "hourly": {
                "time": ["2026-10-05T00:00", "2026-10-05T01:00"],
                "wind_speed_10m_gfs_seamless": [10.0, 11.0],
                "wind_direction_10m_gfs_seamless": [270, 275],
                "wind_speed_10m_ecmwf_ifs025": [None, None],
                "wind_direction_10m_ecmwf_ifs025": [None, None],
            },
            "daily": {"time": ["2026-10-05"], "sunrise": ["2026-10-05T12:05"], "sunset": ["2026-10-05T23:40"]},
        }
        times, winds, sun = sources.parse_openmeteo(doc, ["gfs_seamless", "ecmwf_ifs025", "icon_seamless"])
        self.assertEqual(times[0], T0)
        self.assertEqual(list(winds), ["gfs_seamless"])
        self.assertEqual(winds["gfs_seamless"][1], (11.0, 275))
        self.assertEqual(sun[0][0].hour, 12)

    def test_nws_layer_expansion(self):
        layer = {"uom": "wmoUnit:m", "values": [
            {"validTime": "2026-10-05T00:00:00+00:00/PT3H", "value": 1.0},
            {"validTime": "2026-10-05T03:00:00+00:00/P1DT2H", "value": 2.0},
            {"validTime": "2026-10-06T05:00:00+00:00/PT1H", "value": None}]}
        out = sources.expand_layer(layer)
        self.assertEqual(out[T0 + timedelta(hours=2)], 1.0)
        self.assertEqual(out[T0 + timedelta(hours=28)], 2.0)
        self.assertEqual(len(out), 3 + 26)
        ft = sources.expand_layer({"uom": "wmoUnit:ft", "values": [
            {"validTime": "2026-10-05T00:00:00+00:00/PT1H", "value": 10}]})
        self.assertAlmostEqual(ft[T0], 3.048)

    def test_ndbc(self):
        text = ("#YY  MM DD hh mm WDIR WSPD GST  WVHT   DPD   APD MWD   PRES  ATMP  WTMP  DEWP  VIS PTDY  TIDE\n"
                "#yr  mo dy hr mn degT m/s  m/s     m   sec   sec degT   hPa  degC  degC  degC  nmi  hPa    ft\n"
                "2026 10 05 01 50 270  9.0 11.0   1.4     6   4.8 265 1012.0  12.0  15.0   MM   MM   MM    MM\n"
                "2026 10 05 00 50 260  8.0 10.0    MM    MM    MM  MM 1012.0  12.0  15.0   MM   MM   MM    MM\n")
        rows = sources.parse_ndbc(text)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["wvht_m"], 1.4)
        self.assertIsNone(rows[1]["wvht_m"])


def westerly_event(models, n=48, blow=(6, 30), speed_kt=25, after=(8, 100)):
    """Wind series: calm, then a W blow, then light offshore clean-up."""
    out = {}
    for m in models:
        w = []
        for i in range(n):
            if i < blow[0]:
                w.append((2.0, 180.0))
            elif i < blow[1]:
                w.append((speed_kt * KT, 265.0))
            else:
                w.append((after[0] * KT, after[1]))
        out[m] = w
    return out


class Engine(unittest.TestCase):
    def run_spot(self, winds, nws=None, now=T0, spot="grand-haven", prefs=PREFS):
        times = hours(len(next(iter(winds.values()))))
        return engine.analyse_spot(SPOTS[spot], prefs, times, winds, all_day_sun(times), nws or {}, now)

    def test_ensemble_agreement_gives_go(self):
        _, wins = self.run_spot(westerly_event(["a", "b", "c", "d"]))
        self.assertTrue(wins)
        w = wins[0]
        self.assertEqual(w["tier"], "GO")
        self.assertGreater(w["peak_ft"], 3)
        self.assertEqual(w["agree"], 1.0)
        self.assertTrue(w["reachable"])

    def test_disagreement_downgrades(self):
        winds = westerly_event(["a", "b"])
        winds.update({m: [(2.0, 180.0)] * 48 for m in ("c", "d", "e")})
        _, wins = self.run_spot(winds)
        self.assertTrue(all(w["tier"] != "GO" for w in wins))

    def test_nws_contradiction_blocks_go(self):
        winds = westerly_event(["a", "b", "c", "d"])
        nws = {t: 0.1 for t in hours(48)}
        _, wins = self.run_spot(winds, nws)
        self.assertTrue(wins)
        self.assertTrue(all(w["tier"] == "OUTLOOK" for w in wins))

    def test_wrong_shore_is_flat(self):
        _, wins = self.run_spot(westerly_event(["a", "b", "c"]), spot="sheboygan")
        self.assertEqual(wins, [])

    def test_unreachable_when_too_soon(self):
        # A 25 kt onshore blow rates poor; the window is the clean-up after it (hour 30+).
        _, wins = self.run_spot(westerly_event(["a", "b"]), now=T0)
        self.assertGreaterEqual(wins[0]["start"], T0 + timedelta(hours=29))
        _, wins = self.run_spot(westerly_event(["a", "b"]), now=T0 + timedelta(hours=29))
        self.assertTrue(wins)
        self.assertFalse(wins[0]["reachable"])

    def test_daylight_filter(self):
        winds = westerly_event(["a", "b"])
        times = hours(48)
        sun = [(T0 + timedelta(hours=40), T0 + timedelta(hours=44))]
        _, wins = engine.analyse_spot(SPOTS["grand-haven"], PREFS, times, winds, sun, {}, T0)
        for w in wins:
            self.assertGreaterEqual(w["start"], T0 + timedelta(hours=39))

    def test_rating_wind_effects(self):
        clean = engine.rate_hour(4, 6, 5, 90, 265, PREFS)
        blown = engine.rate_hour(4, 6, 28, 265, 265, PREFS)
        self.assertGreater(clean, blown)
        self.assertEqual(engine.rate_hour(1.0, 6, 5, 90, 265, PREFS), 0)
        self.assertEqual(engine.rate_hour(3, 4.0, 5, 90, 265, PREFS), 0)


class Alerts(unittest.TestCase):
    def win(self, tier, start_h=30, reachable=True, spot="grand-haven"):
        return {"spot": spot, "name": spot, "start": T0 + timedelta(hours=start_h),
                "end": T0 + timedelta(hours=start_h + 4), "tier": tier, "reachable": reachable,
                "rating": "good", "peak_ft": 4.0, "peak_tp": 6.0, "wind_kt": 10, "wind_dir": 260,
                "wind_rel": "onshore", "agree": 1.0, "nws_peak_ft": 4.2, "nws_ok": True,
                "lead_h": start_h, "need_h": 9, "hours": 4}

    def test_dedupe_and_upgrade(self):
        tz = "America/Chicago"
        a, st = report.select_alerts([self.win("WATCH")], {}, T0, tz)
        self.assertEqual(len(a), 1)
        a, st = report.select_alerts([self.win("WATCH", start_h=33)], st, T0, tz)
        self.assertEqual(a, [])  # same spot, same local day
        a, st = report.select_alerts([self.win("GO")], st, T0, tz)
        self.assertEqual(len(a), 1)
        a, _ = report.select_alerts([self.win("GO", reachable=False, spot="x"),
                                     self.win("OUTLOOK", spot="y")], st, T0, tz)
        self.assertEqual(a, [])

    def test_state_pruned(self):
        _, st = report.select_alerts([], {"old|2026-09-01": "GO"}, T0, "America/Chicago")
        self.assertEqual(st, {})

    def test_report_renders(self):
        md = report.build_report([self.win("GO"), self.win("WATCH", reachable=False)], T0,
                                 "America/Chicago", ["note"])
        self.assertIn("Reachable windows", md)
        self.assertIn("too soon", md)
        self.assertIn("**GO**", md)


class Verification(unittest.TestCase):
    def test_scorecard_end_to_end(self):
        with tempfile.TemporaryDirectory() as d:
            hrs = [{"time": T0 + timedelta(hours=i), "hs_ft": 4.0, "tp_s": 6.0,
                    "rating": 2, "agree": 1.0, "nws_ft": None} for i in range(0, 72)]
            verify.log_forecast(d, T0, "45007", hrs)
            verify.log_forecast(d, T0, "grand-haven", hrs)
            obs = [{"time": T0 + timedelta(hours=i, minutes=-10), "wvht_m": 1.0, "dpd_s": 6.0,
                    "mwd": 265.0, "wspd": 9.0, "wdir": 265.0} for i in range(72)]
            self.assertGreater(verify.merge_obs(d, "45007", obs), 0)
            self.assertEqual(verify.merge_obs(d, "45007", obs), 0)  # idempotent
            verify.log_session(d, T0 + timedelta(hours=30), "grand-haven", "good")
            verify.log_session(d, T0 + timedelta(hours=54), "grand-haven", "flat")
            card = verify.score(d)
            self.assertIn("| 45007 | 0-24h |", card)
            self.assertIn("| 24-48h | 1 | 1 | 0 | 0 | 0 |", card)  # hit
            self.assertIn("| 48-72h | 1 | 0 | 0 | 1 | 0 |", card)  # false alarm

    def test_bad_rating_rejected(self):
        with tempfile.TemporaryDirectory() as d, self.assertRaises(ValueError):
            verify.log_session(d, T0, "grand-haven", "rad")


class CliOffline(unittest.TestCase):
    def test_run_with_stubbed_sources(self):
        def fake_om(lat, lon, models, **kw):
            times = hours(72, start=T0 - timedelta(hours=24))
            winds = {m: [(2.0, 180.0)] * 30 + [(25 * KT, 265.0)] * 24 + [(3.0, 100.0)] * 18
                     for m in models}
            return times, winds, all_day_sun(times)

        with tempfile.TemporaryDirectory() as d, \
                mock.patch.object(sources, "fetch_openmeteo", fake_om), \
                mock.patch.object(sources, "fetch_nws_waves", lambda la, lo: {}), \
                mock.patch.object(sources, "fetch_ndbc", lambda s: []), \
                mock.patch.object(verify, "now_utc", lambda: T0), \
                mock.patch.dict(os.environ, {"NTFY_TOPIC": ""}), \
                mock.patch("sys.stdout", new=open(os.devnull, "w")) as out:
            self.assertEqual(cli.main(["--config", os.path.join(ROOT, "spots.json"), "--data", d, "run"]), 0)
            with open(os.path.join(d, "outlook.md")) as f:
                md = f.read()
            self.assertIn("Grand Haven", md)
            self.assertNotIn("Sheboygan, WI |", md)  # W wind: wrong shore
            self.assertTrue(os.path.exists(os.path.join(d, "alerts.txt")))
            self.assertTrue(os.listdir(os.path.join(d, "log")))
            out.close()


if __name__ == "__main__":
    unittest.main()
