# Aaron — Hiking & Outdoor Delight Profile (source of truth)

Version 0.2 · 2026-09-25 · Status: capability layer **accepted**; taste layer **calibrated (session 1)**

## 0. Provenance and authority

| Source | Authority | What it contributes |
|---|---|---|
| *Outdoor Opportunity Intelligence System — Product & Engineering Specification* (Google Doc, last edited 2026-09-22), §§2–5, 8.1–8.3, 8.6 | **Normative.** It wins on any conflict. | Decision contract, origin/envelope, physical state, safety, hiking capability, terrain matrix |
| Same spec, cycling (§8.4) and surfing (§8.5) sections | Accepted for those lanes; **cross-activity inference only** here | Crowd, traffic, exploration and progression signals |
| Trail maps saved to Drive (2020–2026) | Weak behavioral signal | Where Aaron has hiked or planned to. Saving a map doesn't mean he loved the place. |
| Co-authored "PM-ASK co-creation" planning sheet (2024, shared) | Weak; co-authored | "Wonder and awe", "sleep under the stars", hiking/camping on a shared idea list |

Confidence labels: **HIGH** = stated and accepted by Aaron · **MED** = he designed the system to track this, but gave no weight · **LOW** = inferred from behavior or a co-authored source · **UNKNOWN** = calibration target. Don't fill it with a default (spec FR-AIP-002).

**Taste layer:** the spec deferred hiking taste (AIP-09). §4 now holds the accepted records from calibration session 1 (2026-09-25), which are candidates to fold back into the spec as the hiking AIP-09 packet.

---

## 1. Decision contract (HIGH, frozen in the spec)

- The recommendation unit is **Place × Activity Configuration × Time Window × Conditions × User Context**. A park isn't a recommendation; *this route, this window, under these conditions* is.
- Every candidate gets **three separate judgments**. Never blend them into one score.
  - **Readiness:** Actionable · Conditional · Monitor · No-go · Unknown/Hold
  - **Personal value:** Exceptional · Strong · Worthwhile · Low differentiation · Unassessed
  - **Confidence:** operational confidence and personal-fit confidence, kept separate
- Eligibility order: identity → legal access → safety → evidence sufficiency → capability & equipment → time & logistics → *then* personal value.
- Value, rarity, or progression appeal **never** offsets a failed safety, access, or equipment gate. Critical safety uncertainty gives **Unknown/Hold**, never Conditional.
- Never surface closed, prohibited, private, ecologically restricted, or "secret" access.
- Viability ("can do") and desirability ("will love") are always shown separately.

## 2. Geography & logistics (HIGH)

- **Default origin:** Bryn Mawr Red Line station, Edgewater, Chicago. For another geography, ask for or assume a stated origin and say which one you used.
- **Envelope:** one-way travel soft cap of 3 h. Exceptional opportunities may stretch to 4 h. Anything farther needs explicit expansion.
- **Mobility:** a car (Toyota Corolla) is usually available. Always also evaluate CTA, Pace, Metra, train+bike, and other credible multimodal options, which may be *prioritized*. MED inference: a good car-free route adds value.
- **Trip shape:** day trip by default. Note when an overnight is feasible (lodging infrastructure exists) but don't source lodging.
- Travel envelopes depend on origin and departure time. Use real door-to-door time, not radius.

## 3. Capability, body, equipment, safety (HIGH, spec §8.1–8.3)

### 3.1 Demonstrated evidence
- **Aug 2026, Patapsco Valley SP (MD):** ~10 mi in ~3 h, ≤ ~300 ft reported elevation change. Felt great, no pain. Valid only for long, low-elevation, maintained-trail hiking. **It says nothing about** steep climbing, technical footing, sand, mud, snow, ice, exposure, or heavy packs.

### 3.2 Envelopes
- **Routine (provisional):** ~4 active hours, ~800 ft reported gain, moderately hilly maintained trail, minimal next-day recovery. Distance, pack weight, footing, and what "elevation" measures are UNKNOWN.
- **Physical state:** Normal by default. Scoped constraint: **repetitive or sustained uphill left-hip flexion** is the challenging dimension. Show this as a scoped modification, never label Aaron "injured". Past health information alone never creates a restriction.
- **Rehab goal:** Aaron wants controlled hiking variation to learn his limits and train hip and core toward full strength and range of motion. **Controlled progression is a positive value**, not just a tolerated risk.

### 3.3 Terrain matrix (compose per route; no single "difficulty" score)

| Route characteristic | Evidence | Use band | Companion |
|---|---|---|---|
| Maintained flat/rolling trail | Demonstrated | **Routine** | Optional |
| Roots, rocks, continuous uneven footing | Untested | Controlled progression | Optional |
| Sustained steep ascent | Untested at dose | Controlled progression; **poles Recommended** (left-hip flexion) | Optional* |
| Sustained/technical descent | Untested | Controlled progression | Optional* |
| Dunes / loose sand | Untested | Controlled progression | Optional |
| Mud, shallow crossings, wet footing | Untested | Controlled progression; conditions highly material | Optional* |
| Hands-required scrambling (no major exposure) | Untested | Controlled progression | **Recommended** initially |
| Exposed heights, cliff edges, consequential falls | Untested | **Route-specific only**, never Routine | Recommended → may be Required |
| Poorly marked routes | Strong navigation | Routine *for navigation* | Optional (remoteness escalates) |
| Legal off-trail | Strong navigation, terrain untested | Controlled progression | Optional/Recommended |
| Snow-covered trail | Untested | Controlled progression; conditions highly material | Optional* |
| Ice with traction | Gear owned, untested | Controlled progression | Optional/Recommended |

\* subject to route consequences, remoteness, and bailout. Strong navigation **never** promotes untested physical terrain or exposure into Routine. "Untested" means neither capable nor incapable.

### 3.4 Progression rule (calibration-first)
A progression outing raises **one** demand dimension at a time and keeps the others familiar. It requires: fresh body-state confirmation, a named progression dimension, easy bailout or route shortening, a conservative turnaround trigger, and poles when repeated uphill hip flexion is material. **Symptom logging** (pre / during / immediately post / same-day / next-day) is high priority. Without it, the outing can still be Actionable but doesn't expand the capability envelope.

### 3.5 Readiness rule
- Low-consequence maintained routes inside the routine envelope → Actionable, no fresh check needed.
- Controlled progression → needs current body-state confirmation plus an explicit rationale.
- Technical, exposed, poorly marked, remote, or hard-to-exit routes → need a route-specific assessment.
- Required gear gap that he can obtain → Conditional. Gear confirmed unavailable → No-go.

### 3.6 Navigation & equipment
- **Navigation (strong):** marked trails, phone maps, offline maps, rerouting, paper topo, compass, legal off-trail, wrong-turn recovery.
- **Owned gear:** trail shoes/boots, waterproof footwear, trekking poles, microspikes, headlamp, offline nav plus backup battery, daypack and hydration, rain/wind shell, cold layers, first aid, emergency bivy/blanket, whistle, insect/tick protection. *Owning* gear doesn't mean it's suitable or available that day.

### 3.7 Solo & safety posture
- **Progression-supportive, safety-bounded.**
- Assistance context has three states: Independent · Solo-exposed · Remote solo.
- Low-consequence solo outings can be Actionable. Scrutiny escalates with exposure, remoteness, cold, darkness, poor comms, and weak bailout.
- For remote solo, recommend a compact safety plan. It's advisory, not a gate.
- If Aaron overrides a No-go, record it but never learn a looser boundary from it. Closures are never overridable.

---

## 4. Sources of delight — calibrated taste layer

Calibration session 1: 2026-09-25, forced-choice plus multi-select, answered by Aaron. Records below are **accepted** at the stated confidence. One session gives direction, not precise weights, so re-test the weights after real outings.

### 4.1 Accepted taste records

| ID | Record | Conf. | Evidence (2026-09-25) | Engine behavior |
|---|---|---|---|---|
| USR-HIK-TASTE-001 | **Openness and remoteness beat access convenience.** An open, big-sky, remote-feeling landscape justifies a long drive over a pleasant, transit-close wooded option. | HIGH | Chose a 4 h drive to Dolly Sods-type heath over a 40 min train to a Wissahickon-type gorge. Named "openness / big sky" and "feeling of remoteness" as the reasons, and did *not* name novelty or "making a day of it". | Weight openness and remoteness heavily. Travel time is a cost, not a veto, for high-openness places within the 4 h Exceptional stretch. |
| USR-HIK-TASTE-002 | **Felt capability is a primary reward.** "The body worked" is part of what makes a hike great. Given an ordinary hard hike vs an easy hike at a rare peak, he picks the hard one. | HIGH | Learn-vs-rare pair; Patapsco "the body worked" | Progression value lifts the value tier. A well-designed controlled-progression route is a first-class recommendation, not a consolation. |
| USR-HIK-TASTE-003 | **Flow and momentum, with dwell stops.** Keeps a rhythm and covers ground, but stops at length at payoffs such as overlooks and water. | HIGH | Patapsco "flow / momentum"; pace style | Prefer routes with continuous walkable stretches punctuated by real payoff points. Budget dwell time in duration estimates, roughly +15–25%, to be calibrated. |
| USR-HIK-TASTE-004 | **Water is a strong positive:** lakeshore/dunes, rivers/gorges, water along the route. | HIGH | Landscape picks; Patapsco "river / water"; loved the Pine Barrens (cedar-water rivers) | Water adjacency is a major value driver. |
| USR-HIK-TASTE-005 | **Hike-plus-swim in summer.** Summer is appealing specifically as morning or evening hikes with swimming access. | HIGH | Stated in his own words | In summer, favor early or late windows and routes that end at, or pass, a legal swimming spot. Swimming stays under its own lane's gates: designated or guarded swimming is Live, unguarded open water is Inventory-only. |
| USR-HIK-TASTE-006 | **Views and elevated vantage are positive.** | MED-HIGH | Picked "bluffs / ridges / views"; open-sky driver | Overlooks and bluff edges add value. Exposure still follows the terrain matrix. |
| USR-HIK-TASTE-007 | **Seasons:** spring, fall, and winter are all welcome. Summer only in the swim-access form (TASTE-005). | HIGH | Season picks | Winter hiking is a desired lane, but snow and ice remain Controlled progression under §3.3. |
| USR-HIK-TASTE-008 | **Vetoes** (taste, not safety): road/traffic noise; crowds and bottlenecks; bugs, heat, and mud. | HIGH | Veto list | A route materially exposed to a veto drops ≥1 value tier and must be disclosed. Readiness is unchanged. Mud-heavy routes appear only when the mode is explicitly a wet-footing progression. Watch bug season (spring/summer wetlands and woods) and heat. |
| USR-HIK-TASTE-009 | **Crowd rule:** busy iconic trails are acceptable only when the payoff is truly exceptional. Crowding and bottlenecks otherwise lower value. | HIGH | "Depends on the payoff" plus the veto | For iconic places, recommend off-peak windows (weekday, early start, shoulder season) and quieter alternative approaches. |
| USR-HIK-TASTE-010 | **Company is neutral.** Solo or together, no standing preference. | HIGH | Stated | No value adjustment. Companion disposition stays a safety output only. |
| USR-HIK-TASTE-011 | **Route shape doesn't matter;** terrain does. | HIGH | Stated | Pick loop, out-and-back, or point-to-point by payoff, logistics, and bailout. |
| USR-HIK-TASTE-012 | **Loved places (reference anchors):** Pine Barrens (Wharton SF), and Middlesex Fells and/or Claremont Canyon. Not selected: Wissahickon, Dolly Sods/Canaan (not hiked, or not loved; unknown which). | MED | Past-places pick | Use these for "same feeling as X" matching. Pine Barrens is flat, sandy, and remote-feeling with dark-water rivers, which shows that *remote feel plus water* can deliver without elevation. |

### 4.2 Demoted or weakened hypotheses

| Former | Status | Why |
|---|---|---|
| D8 Exploration/novelty as a driver | **Weakened → LOW** | "Strangeness/novelty" not picked for heath; monotony not a veto |
| D9 Low friction as a value | **Weakened → tiebreaker only** | 4 h open heath chosen over a 40 min train gorge. Transit access stays a *tiebreaker* and a "best low-friction" portfolio role, not a main value driver |
| D4 Subtle ecology (prairie, savanna, wetland) | **Weakened → LOW** | Not picked as a landscape that lights him up. Ecology may still add value through distinctive *open* or *water* ecosystems (heath, pine barrens) |
| D6 Crowds | **Superseded** by TASTE-009 | |
| D1, D3, D11 | **Promoted** into TASTE-002, TASTE-001, and §1 rules | |
| D5 Rarity/timing | **Held → MED**; ranks *below* progression (TASTE-002) | |
| D2 Restorative/immersive, D10 Wonder/awe | **Still UNKNOWN**: untested this session | |

### 4.3 Value-scoring heuristic (provisional weights, recalibrate after outings)

For a route that passes the gates, start at **Worthwhile**. Then:
- **+1 tier** for each strong hit on:
  - openness/remoteness (TASTE-001)
  - water adjacency or swim access in season (TASTE-004/005)
  - a meaningful, well-designed progression dimension (TASTE-002)
- **+½ tier** for:
  - views/bluffs (TASTE-006)
  - good flow terrain with payoff stops (TASTE-003)
- **−1 tier** for each material veto exposure (TASTE-008), or unavoidable crowding without an exceptional payoff (TASTE-009).
- **Cap at Strong** unless at least two major drivers hit. **Exceptional** needs openness/remoteness *and* water, or either one *plus* a rare-timing window.
- Always name which records drove the tier.

### 4.4 Remaining UNKNOWNs (next calibration targets)
- Whether it was Fells or Claremont (or both) that he loved, and why. What made Wissahickon not qualify (not hiked, or hiked and meh)?
- Whether Dolly Sods has been hiked. If yes and not loved, that directly tests TASTE-001.
- How much restorative/immersive and wonder/awe matter
- How much cultural or historic features add
- Heat threshold (what temperature or humidity turns a summer hike into a veto)
- Tolerance for trail-side infrastructure short of road noise (rail trails, visible buildings)

### 4.5 Ongoing calibration
After each outing, collect 1–5 ratings on enjoyment, openness/remoteness, water, views, flow, exertion, veto exposure, and repeat desire, plus the "best moment" and "what would have made it better". Keep these separate from the symptom log. Revise the weights in §4.3 once there are ≥5 rated outings, and log each revision with its date.
