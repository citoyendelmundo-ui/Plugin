# Hike Finder run: Driftless inventory · 2026-10-21

- **Output:** Claude Doc "Driftless Hike Inventory" (https://claude.ai/artifact/NQ68FYab72nKUQBJ1mxr99).
- **Scope:** Driftless core (WI/MN/IA/IL) plus the Baraboo Hills edge class; ≤5 h one way from Edgewater (approved).

## Scoring model
- **Weights:** views 25%, variety 20%, rock 15%, water 15%, openness 10%, payoff density 10%, history 5%. Vetoes subtract up to 1.
- **Calibration:** Devil's Lake bluffs 4.40 (rated 5); Sauk Point → Parfrey's 1.70 (rated 2.5).
- **Tiers:** Tier 1 ≥ 4.0; Tier 2 3.3–3.99; Tier 3 < 3.3.
- **Script:** `tools/driftless_scoring.py`.

## Results
- **Tier 1:** Wyalusing 4.40; Whitewater 4.20; Perrot 4.17.
- **Tier 2:** Backbone, Pikes Peak, Mines of Spain, Wildcat Mtn, Ferry Bluff, Effigy Mounds, Kickapoo VR, Gov Dodge, Great River Bluffs, Latsch, Rush Creek, Decorah.
- **Tier 3:** 9 routes.

## Open items
- **Unconfirmed status:**
  - Treasure Cave reopening (Wyalusing);
  - Whitewater trail closures;
  - Ferry Bluff closure start (Nov 15 vs Dec 1).
- **Not checked in detail:** Latsch, Beaver Creek, Apple River, Baxter's Hollow, Pewit's Nest, Natural Bridge.
- **Physical follow-up still pending:**
  - Sauk Point → Parfrey's Glen (Oct 20) outcome;
  - Oct 19 evening and Oct 20 morning checks.

## Update: official links + hiking time (v2 table in `2026-10-21-driftless-table-v2.md`)
- **Time model** (calibrated to Oct 19 actual): mi/3 + gain/1000 h, ×1.25 for stops. Predicts 6h24 vs actual 6h17 for Devil's Lake.
- **Links:** confirmed via search results on official domains (WI DNR, MN DNR, Iowa DNR, IL DNR, NPS, KVR, TNC, City of Decorah).
  - MN park IDs are taken from the official map filenames (spk00280 confirmed as the Whitewater page).
  - Hixon Forest has no official city trail page; the visitor bureau page is used.
- **5-hour-capable days:**
  - On their own (by adding loops): all three Tier 1 parks, plus Backbone, Mines of Spain, KVR, Gov Dodge, Miss. Palisades, Yellow River, Hixon.
  - Paired: Wildcat + KVR; Decorah + Trout Run/Beaver Creek.
  - Pikes Peak and Effigy are borderline.
