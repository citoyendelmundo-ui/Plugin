# Hike Finder run — Five-Hour Hike Inventory (master) · 2026-10-21

- **Scope:** Michigan, Indiana and the rest of Illinois within a 5 h drive, merged with the Driftless list. Shawnee is included as a stretch class (5h30–6h).
- **Scoring:** score = 0.85 × features + 0.15 × capacity (new driver, approved 2026-10-21).
  - Capacity scale: 5 = 2+ full days; 3 = fills one 5 h day; 1 = ~2 h. Only quality hours count.
  - Enjoyment ≈ 0.9 + 0.92 × score.
- **Calibration:**

  | Rated hike | Predicted | Actual |
  | --- | --- | --- |
  | Devil's Lake | 5.0 | 5 |
  | Indiana Dunes SP | 3.5 | 3.75 |
  | Sauk Point → Parfrey's Glen | 2.5 | 2.5 |

  Known bias: lake and dune hikes are under-rated by ~0.25 because they get no rock credit.
- **Doc:** https://claude.ai/artifact/JTWDnFdMxuFUFgwKg4V3Bw
- **Tools:**
  - `tools/master_scoring.py` produces the JSON.
  - `tools/master_table.py <master.json> <drift_rows.json> <out.md>` renders the table.
  - `drift_rows.json` holds the rows of `runs/2026-10-21-driftless-table-v2.md`.
- **Confidence:** new-region features are desk estimates. Fit Medium; operational Medium (checked today).

## Master ranking

| # | Hike | Region | Tier | Score (features · capacity) | Drive | Distance · climb | Hiking time | 5-hour day? | Base town | Official site |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Wyalusing State Park: Sentinel Ridge + Bluff Trail + Treasure Cave + Sand Cave loop | Driftless | 1 | **4.34** (4.40 · 4) | 4h | 6–7 mi · ~800 ft | 3h45 | Yes, by adding park loops (14+ mi of trail) | Prairie du Chien | [WI DNR](https://dnr.wisconsin.gov/topic/parks/wyalusing) |
| 2 | Sleeping Bear Dunes NL (MI): Dunes Hiking Trail + Pyramid Point + Empire Bluff | Michigan | 1 | **4.19** (4.05 · 5) | 5h | ~7.7 mi · ~900 ft | ~5h (sand adds ~15%) | Yes; 2+ days with Alligator Hill, Bay View, Lasso Loop | Empire / Glen Arbor | [NPS](https://www.nps.gov/slbe/) |
| 3 | Whitewater State Park (MN): Chimney Rock + Inspiration Point + Coyote Point + river | Driftless | 1 | **4.17** (4.20 · 4) | 5h | 5–6 mi · ~900 ft | 3h30 | Yes, by adding the park's other trails | Winona / Rochester | [MN DNR](https://www.dnr.state.mn.us/state-parks/park.html?id=spk00280) |
| 4 | Perrot State Park: Brady's Bluff + Perrot Ridge + Riverview figure-eight | Driftless | 1 | **4.14** (4.17 · 4) | 4h30 | 5–6 mi · ~1,000 ft | 3h30 | Yes, by adding Riverview and ridge loops | Trempealeau / La Crosse | [WI DNR](https://dnr.wisconsin.gov/topic/parks/perrot) |
| 5 | Nordhouse Dunes Wilderness (MI): Nurnberg trailhead → interior dunes → beach return | Michigan | 2 | **3.81** (3.60 · 5) | 4h15 | ~9 mi · ~500 ft | ~5h on sand | Yes; extended loop ~14 mi; add Ludington SP for day 2 | Ludington / Manistee | [USFS](https://www.fs.usda.gov/r09/huron-manistee/recreation/nordhouse-dunes-wilderness-area-0) |
| 6 | Clifty Falls State Park (IN): Trails 2 (creekbed) + 3 + 4 + 5 + 8 past four falls | Indiana | 2 | **3.64** (3.75 · 3) | 5h | ~9 mi · ~900 ft | 4h55 (creekbed: slow) | Yes | Madison IN | [IN DNR](https://www.in.gov/dnr/state-parks/parks-lakes/clifty-falls-state-park/) |
| 7 | Pikes Peak State Park (IA): Bridal Veil Falls + bluff trail toward Point Ann | Driftless | 2 | **3.63** (3.65 · 3.5) | 4h | 4–8 mi · ~500 ft | 4h30 | Borderline: all ~11 mi of trail ≈ 5 h | McGregor / Prairie du Chien | [Iowa DNR](https://www.iowadnr.gov/places-go/state-parks/all-parks/pikes-peak-state-park) |
| 8 | Backbone State Park (IA): Backbone Trail over the dolomite fin + river and lake trails | Driftless | 2 | **3.59** (3.70 · 3) | 4h15 | 4–6 mi · ~600 ft | 2h45 | Yes (~21 mi of trail) | Dubuque / Strawberry Point | [Iowa DNR](https://www.iowadnr.gov/places-go/state-parks/all-parks/backbone-state-park) |
| 9 | Kickapoo Valley Reserve: Hanson Rock / West Ridge overlook + Weister Creek | Driftless | 2 | **3.52** (3.43 · 4) | 3h45 | ~7 mi · ~700 ft | 3h45 | Yes (40+ mi of trail) | Viroqua / La Farge | [Reserve](https://kvr.state.wi.us/Home) |
| 10 | Mines of Spain (Dubuque): Horseshoe Bluff + Catfish Creek + Julien Dubuque Monument | Driftless | 2 | **3.51** (3.60 · 3) | 3h15 | ~5 mi · ~600 ft | 2h45 | Yes (~20 mi of trail) | Dubuque | [Iowa DNR](https://www.iowadnr.gov/places-go/state-parks/all-parks/mines-spain-state-recreation-area) |
| 11 | Governor Dodge State Park: Lost Canyon + Stephens Falls + Pine Cliff | Driftless | 2 | **3.49** (3.40 · 4) | 3h | ~6 mi · ~500 ft | 3h | Yes (~40 mi of trail) | Spring Green / Dodgeville | [WI DNR](https://dnr.wisconsin.gov/topic/parks/govdodge) |
| 12 | Turkey Run State Park (IN): Trails 3 (ladders) + 2 + 5 + 9 + 10 via the suspension bridge | Indiana | 2 | **3.49** (3.58 · 3) | 2h45 | ~10 mi · ~800 ft | 5h10 (ladders, creekbed: slow) | Yes (~14 mi); Shades next door for day 2 | Marshall / Crawfordsville | [IN DNR](https://www.in.gov/dnr/state-parks/parks-lakes/turkey-run-state-park/index) |
| 13 | Wildcat Mountain State Park: Old Settler's Trail + Hemlock Nature Trail | Driftless | 2 | **3.47** (3.55 · 3) | 3h45 | ~4 mi · ~750 ft | 2h30 | Yes, with Kickapoo Valley Reserve the same day | Viroqua / Ontario | [WI DNR](https://dnr.wisconsin.gov/topic/parks/wildcat) |
| 14 | Effigy Mounds National Monument: Fire Point + Twin Views + Hanging Rock (North Unit) | Driftless | 2 | **3.46** (3.45 · 3.5) | 4h | ~7 mi · 600–880 ft | 3h45 | Close: add the South Unit for ~5 h | McGregor / Prairie du Chien | [NPS](https://www.nps.gov/efmo/) |
| 15 | Shades State Park (IN): Six Ravine route + Devil's Punchbowl + Inspiration Point | Indiana | 2 | **3.44** (3.52 · 3) | 2h45 | ~7 mi · ~800 ft | 3h55 | Close: pair with Turkey Run | Waveland / Crawfordsville | [IN DNR](https://www.in.gov/dnr/state-parks/parks-lakes/shades-state-park/) |
| 16 | Yellow River State Forest (IA): Paint Creek loop with Fire Tower / Cedar Point overlooks | Driftless | 2 | **3.40** (3.12 · 5) | 4h | 8–13 mi · ~1,200 ft | 7h | Yes: the full loop is a 5–7 h day | McGregor / Decorah | [Iowa DNR](https://www.iowadnr.gov/places-go/state-forests/yellow-river-state-forest) |
| 17 | Manistee River Trail + NCT loop (MI): West half of the 20-mi loop, suspension bridge, bluff camps | Michigan | 2 | **3.37** (3.08 · 5) | 4h45 | ~10.5 mi · ~1,000 ft | 5h40 | Yes; full 20-mi loop = 2 days | Wellston / Mesick | [USFS](https://www.fs.usda.gov/r09/huron-manistee/recreation/trails/manistee-river-trail) |
| 18 | Ludington State Park (MI): Skyline + Ridge + Island Lake + Lighthouse beach | Michigan | 2 | **3.32** (3.20 · 4) | 4h | ~10 mi · ~400 ft | ~5h on sand | Yes (21 mi of marked trail) | Ludington | [MI DNR](https://www.michigan.gov/ludington) |
| 19 | Starved Rock + Matthiessen (IL): East canyons (French→Ottawa/Kaskaskia) + Matthiessen Dells | Illinois | 2 | **3.32** (3.20 · 4) | 1h45 | ~10 mi · ~900 ft | 5h20 | Yes (13+ mi + 5 mi); LaSalle/Tonti closed | Utica / Oglesby | [IL DNR Starved Rock](https://dnr.illinois.gov/parks/park.starvedrock) · [Matthiessen](https://dnr.illinois.gov/parks/activity/park.matthiessen.html) |
| 20 | Decorah bluffs and springs: Dunning's Spring + Ice Cave + Palisades Park + Pulpit Rock | Driftless | 3 | **3.25** (3.30 · 3) | 4h30 | ~5 mi · ~500 ft | 2h45 | Yes, adding Trout Run Trail (paved) or Beaver Creek | Decorah | [City of Decorah](https://parks.decorahia.org/) |
| 21 | Great River Bluffs State Park (MN): King's Bluff + overlook trails | Driftless | 3 | **3.19** (3.40 · 2) | 5h | ~4 mi · ~300 ft | 2h | No (~6.5 mi in park): pair with Perrot or Latsch | Winona | [MN DNR](https://www.dnr.state.mn.us/state-parks/park.html?id=spk00244) |
| 22 | Mississippi Palisades State Park (IL): Sentinel + Twin Sisters + Indian Head (south trails) | Driftless | 3 | **3.15** (3.18 · 3) | 2h45 | ~4 mi · ~500 ft | 2h15 | Yes, adding the north trails (~15 mi total) | Savanna / Galena | [IL DNR](https://dnr.illinois.gov/parks/activity/park.mississippipalisades.html) |
| 23 | Knobstone Trail (IN): Delaney Park → Elk Creek section (south half is the steep bit) | Indiana | 3 | **3.13** (2.80 · 5) | 4h45 | ~10 mi · ~2,000 ft | 6h40 | Yes (48–58 mi; a Deam Lake segment closed) | Salem / Scottsburg | Indiana DNR (Knobstone page URL not confirmed) |
| 24 | Rush Creek State Natural Area: Old lane to the goat-prairie bluff tops | Driftless | 3 | **3.12** (3.32 · 2) | 4h | 3–4 mi · ~450 ft | 2h | No: pair with Wyalusing | Prairie du Chien / Ferryville | [WI DNR](https://dnr.wisconsin.gov/topic/statenaturalareas/RushCreek) |
| 25 | Arcadia Dunes / Old Baldy (MI): Old Baldy loop + Arcadia Marsh (pair with Nordhouse or Sleeping Bear) | Michigan | 3 | **3.12** (3.32 · 2) | 4h45 | ~3.2 mi · ~350 ft | 1h45 | No: pair with Nordhouse or Sleeping Bear | Frankfort / Arcadia | [Grand Traverse Regional Land Conservancy](https://www.gtrlc.org/) (preserve page not confirmed) |
| 26 | Ferry Bluff State Natural Area: Bluff-top climb over the Wisconsin River | Driftless | 3 | **3.09** (3.55 · 0.5) | 3h | ~1 mi · ~300 ft | 0h45 | No: pair with Governor Dodge or Devil's Lake | Sauk City / Baraboo | [WI DNR](https://dnr.wisconsin.gov/topic/statenaturalareas/FerryBluff) |
| 27 | Beaver Creek Valley State Park (MN): Spring-fed creek valley loops | Driftless | 3 | **3.08** (3.18 · 2.5) | 4h30 | ~5 mi · ~400 ft | 2h30 | Unlikely alone: pair with Decorah | Decorah / Caledonia | [MN DNR](https://www.dnr.state.mn.us/state-parks/park.html?id=spk00112) |
| 28 | John A. Latsch State Park (MN): Stairway trail to the bluff top | Driftless | 3 | **3.04** (3.40 · 1) | 4h45 | ~1 mi · ~450 ft | 1h | No: an add-on | Winona | [MN DNR](https://www.dnr.state.mn.us/state-parks/park.html?id=spk00177) |
| 29 | Indiana Dunes SP + NP (IN): Trails 9 + 8 (3 Dune Challenge) + 10 + West Beach / Cowles Bog day | Indiana | 3 | **2.98** (2.80 · 4) | 1h15 | ~11 mi · ~900 ft | 5h45 | Yes (50+ mi across both parks) | Chesterton | [IN DNR](https://www.in.gov/dnr/state-parks/parks-lakes/indiana-dunes-state-park/) · [NPS](https://www.nps.gov/indu/) |
| 30 | Charles C. Deam Wilderness (IN): Peninsula Trail to Lake Monroe shore + Grubb Ridge | Indiana | 3 | **2.98** (2.62 · 5) | 4h15 | ~11 mi · ~1,000 ft | 5h50 | Yes (36 mi of trail) | Bloomington | [USFS](https://www.fs.usda.gov/r09/hoosier/recreation/charles-c-deam-wilderness) |
| 31 | Saugatuck Dunes State Park (MI): South Trail + North Trail + beach | Michigan | 3 | **2.85** (2.82 · 3) | 2h15 | ~8 mi · ~700 ft | 4h15 | Close: all four trails (~12–13 mi) ≈ 6h | Saugatuck | [MI DNR](https://www.michigan.gov/recsearch/parks/saugatuck) |
| 32 | Castle Rock SP + Lowden-Miller SF (IL): Castle Rock bluff + Lowden-Miller river-bluff loops | Illinois | 3 | **2.85** (2.82 · 3) | 2h | ~10 mi · ~600 ft | 4h55 | Yes (6–7 mi + ~22 mi) | Oregon IL | [IL DNR Lowden-Miller](https://dnr.illinois.gov/parks/activity/park.lowdenmiller.html) (Castle Rock page not confirmed) |
| 33 | Muskegon State Park (MI): Lost Lake loops + Dune Ridge + Snowshoe trails + beach | Michigan | 3 | **2.79** (2.75 · 3) | 3h | ~8 mi · ~700 ft | 4h15 | Close: ~12 mi of trail | Muskegon | [MI DNR](https://www.michigan.gov/muskegon) (URL not confirmed) |
| 34 | P.J. Hoffmaster State Park (MI): Dune Overlook stairs + Homestead + Walk-a-Mile + beach | Michigan | 3 | **2.78** (2.83 · 2.5) | 2h45 | ~7 mi · ~500 ft | 3h30 | No (~10 mi in park): pair with Muskegon | Grand Haven / Muskegon | [MI DNR](https://www.michigan.gov/hoffmaster) |
| 35 | Brown County State Park (IN): Trails 8 + 10 (fire tower) + 9/11 to Ogle Lake | Indiana | 3 | **2.77** (2.55 · 4) | 4h | ~10 mi · ~1,100 ft | 5h30 | Yes | Nashville IN | [IN DNR](https://www.in.gov/dnr/state-parks/parks-lakes/brown-county-state-park/index) |
| 36 | Hixon Forest + Grandad Bluff: George's Point + Hixon View + Grandad Bluff loop | Driftless | 3 | **2.75** (2.70 · 3) | 4h15 | ~4 mi · ~700 ft | 2h30 | Yes, using the wider Hixon network (10+ mi) | La Crosse | [Explore La Crosse (visitor bureau)](https://explorelacrosse.com/places/the-nature-place/) |
| 37 | McCormick's Creek State Park (IN): Trail 3 canyon + falls + Trails 5/7 | Indiana | 3 | **2.75** (2.88 · 2) | 3h45 | ~5 mi · ~400 ft | 2h35 | No: pair with Brown County | Spencer / Bloomington | [IN DNR](https://www.in.gov/dnr/state-parks/parks-lakes/mccormicks-creek-state-park/) |
| 38 | Kankakee River State Park (IL): Rock Creek canyon + river bluff trail | Illinois | 3 | **2.68** (2.62 · 3) | 1h15 | ~8 mi · ~300 ft | 3h45 | Close | Bourbonnais | IL DNR (URL not confirmed) |
| 39 | Maquoketa Caves State Park (IA): Caves loop + Natural Bridge + Dancehall Cave | Driftless | 3 | **2.67** (2.88 · 1.5) | 3h | 3–4 mi · ~400 ft | 2h | No (~6–7 mi in park): pair with Backbone | Dubuque / Maquoketa | [Iowa DNR](https://www.iowadnr.gov/places-go/state-parks/all-parks/maquoketa-caves-state-park) |
| 40 | Baxter's Hollow (Nature Conservancy): Creek gorge in the Baraboo Hills | Driftless | 3 | **2.62** (2.73 · 2) | 3h | 3–4 mi · ~300 ft | 1h45 | No: rough, unmaintained trail | Baraboo | [Nature Conservancy](https://www.nature.org/en-us/get-involved/how-to-help/places-we-protect/baxters-hollow-rd/) |
| 41 | Apple River Canyon State Park (IL): Canyon trails | Driftless | 3 | **2.59** (2.78 · 1.5) | 2h45 | ~3 mi · ~250 ft | 1h30 | No: pair with Mississippi Palisades | Galena | [IL DNR](https://dnr.illinois.gov/parks/park.applerivercanyon.html) |
| 42 | Warren Dunes State Park (MI): Tower Hill + Great Warren Dune + beach loop | Michigan | 3 | **2.55** (2.65 · 2) | 1h45 | ~6 mi · ~700 ft | 3h25 | No (~6 mi in park) | Sawyer / Bridgman | [MI DNR](https://www.michigan.gov/warrendunes) |
| 43 | Yankee Springs Recreation Area (MI): Hall Lake + Graves Hill + Devil's Soup Bowl + NCT | Michigan | 3 | **2.53** (2.45 · 3) | 2h45 | ~9 mi · ~600 ft | 4h30 | Close (16+ mi, few loops) | Hastings / Middleville | [MI DNR](https://www.michigan.gov/YankeeSprings) |
| 44 | Pokagon State Park (IN): 8-mile connector loop over Hell's Point + Potawatomi preserve | Indiana | 3 | **2.53** (2.45 · 3) | 2h45 | ~8 mi · ~400 ft | 3h50 | Close | Angola | [IN DNR](https://www.in.gov/dnr/state-parks/parks-lakes/pokagon-state-parktrine-state-recreation-area/) |
| 45 | Pewit's Nest State Natural Area: Sandstone gorge walk | Driftless | 3 | **2.16** (2.45 · 0.5) | 3h15 | ~1 mi · ~100 ft | 0h30 | No: an add-on | Baraboo | [WI DNR](https://dnr.wisconsin.gov/topic/statenaturalareas/PewitsNest) |
| 46 | White Pines Forest State Park (IL): Pine stands + creek fords + CCC lodge | Illinois | 3 | **1.83** (1.98 · 1) | 2h | ~4 mi · ~200 ft | 1h55 | No: an add-on to Castle Rock | Mount Morris | IL DNR (URL not confirmed) |
| 47 | Natural Bridge State Park: Sandstone arch + rock shelter | Driftless | 3 | **1.73** (1.95 · 0.5) | 3h15 | ~1 mi · ~150 ft | 0h30 | No (~4 mi in park): an add-on | Baraboo | [WI DNR](https://dnr.wisconsin.gov/topic/parks/naturalbridge) |
| 48 | Garden of the Gods + Rim Rock (IL, Shawnee): Observation Trail + Indian Point + River to River section; Rim Rock/Pounds Hollow second day | Shawnee (stretch) | Stretch | **4.40** (4.30 · 5) | 5h45 | ~10 mi · ~1,200 ft | 5h40 | Yes; Rim Rock + Pounds Hollow + High Knob fill day 2 | Harrisburg / Elizabethtown | [USFS Garden of the Gods](https://fs.usda.gov/r09/shawnee/recreation/garden-gods-recreation-area) · [Rim Rock](https://www.fs.usda.gov/r09/shawnee/recreation/trails/rim-rock-national-recreation-trail) |
| 49 | Bell Smith Springs + Jackson Falls (IL, Shawnee): Natural Bridge + Mill Branch + Sentry Bluff; Jackson Falls bluff line | Shawnee (stretch) | Stretch | **3.96** (3.95 · 4) | 5h45 | ~8 mi · ~700 ft | 4h15 | Close; Jackson Falls bluff line adds ~1h | Eddyville / Harrisburg | [USFS Bell Smith](https://fs.usda.gov/r09/shawnee/recreation/bell-smith-springs-recreation-area) · [Jackson Falls](https://www.fs.usda.gov/r09/shawnee/recreation/jackson-falls) |
| 50 | Little Grand Canyon (IL, Shawnee): Rim + canyon-floor loop | Shawnee (stretch) | Stretch | **3.61** (3.90 · 2) | 5h45 | ~3.6 mi · ~350 ft | 1h55 | No: pair with Giant City | Murphysboro / Carbondale | [USFS Shawnee](https://www.fs.usda.gov/r09/shawnee/maps-guides/recreation-opportunity-guides) |
| 51 | Ferne Clyffe State Park (IL): Big Rocky Hollow + Round Bluff + Happy Hollow | Shawnee (stretch) | Stretch | **3.31** (3.37 · 3) | 5h30 | ~7 mi · ~600 ft | 3h40 | Close: pair with Giant City | Goreville | IL DNR (URL not confirmed) |
| 52 | Giant City State Park (IL): Red Cedar loop + Giant City Nature Trail + Stone Fort | Shawnee (stretch) | Stretch | **3.15** (3.00 · 4) | 5h30 | ~12 mi · ~1,000 ft | 6h15 | Yes (Red Cedar loop; closed in shotgun deer season) | Makanda / Carbondale | [IL DNR Red Cedar trail PDF](https://dnr.illinois.gov/content/dam/soi/en/web/dnr/parks/documents/giantcityredcedartrail.pdf) |

## Headlines
- **Wyalusing #1 (4.34)** and **Sleeping Bear #2 (4.19)**. Sleeping Bear is the best two-day trip.
- **Nordhouse + Ludington (#5, #18):** the most remote weekend.
- **Turkey Run + Shades (#12, #15):** the most rugged ground for the shortest drive.
- **Starved Rock + Matthiessen (#19):** the only 5 h day within 2 h of home.
- **Shawnee Garden of the Gods (4.40)** would rank #1 if the envelope is widened. **Decision pending from Aaron.**

## Status flags (as of 2026-10-21)
- Huron-Manistee recreation sites were closed after the April 2026 storm (update July 9). Check before any Nordhouse trip.
- Shades: Trail 7 closed; Pine Hills NP closed by flooding (August 2026).
- Starved Rock: LaSalle and Tonti canyons closed.
- Knobstone: Deam Lake segment closed.
- Glenwood Dunes partly closed through Dec 31.
- Giant City Red Cedar trail closes during shotgun deer season.

## Open questions (§4.2)
1. Widen the envelope to ~6 h for Shawnee overnights?
2. On the next lakeshore outing, rate views, water and enjoyment separately to test the dune under-rating bias.
