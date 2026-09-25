# Aaron — Hiking & Outdoor Delight Profile (source of truth)

Version 0.1 · 2026-09-25 · Status: capability layer **accepted**, taste layer **hypothesis — not yet elicited**

## 0. Provenance and authority

| Source | Authority | What it contributes |
|---|---|---|
| *Outdoor Opportunity Intelligence System — Product & Engineering Specification* (Google Doc, last edited 2026-09-22), §§2–5, 8.1–8.3, 8.6 | **Normative.** It wins on any conflict. | Decision contract, origin/envelope, physical state, safety, hiking capability, terrain matrix |
| Same spec, cycling (§8.4) and surfing (§8.5) sections | Accepted for those lanes; **cross-activity inference only** here | Crowd, traffic, exploration and progression signals |
| Trail maps saved to Drive (2020–2026) | Weak behavioral signal | Where Aaron has hiked or planned to. Saving a map doesn't mean he loved the place. |
| Co-authored "PM-ASK co-creation" planning sheet (2024, shared) | Weak; co-authored | "Wonder and awe", "sleep under the stars", hiking/camping on a shared idea list |

Confidence labels: **HIGH** = stated and accepted by Aaron · **MED** = he designed the system to track this, but gave no weight · **LOW** = inferred from behavior or a co-authored source · **UNKNOWN** = calibration target. Don't fill it with a default (spec FR-AIP-002).

**Key finding:** the spec deliberately deferred hiking taste (AIP-09). Almost everything below about *delight* is inference. Treat §4 as hypotheses to disconfirm, not as preferences.

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

## 4. Sources of delight — HYPOTHESES (taste layer not yet elicited)

Each hypothesis has a confidence label and a **disconfirmation test**, meaning what would prove it wrong. Use these to rank candidates *tentatively*, state the value tier as "provisional", and lower personal-fit confidence.

| # | Hypothesis | Conf. | Basis | Would be wrong if… |
|---|---|---|---|---|
| D1 | **Controlled challenge and felt progress** is a primary satisfaction: a route that teaches him something about his body or skill beats an equally pretty route that doesn't. | **HIGH** | Risk posture "actively identify controlled challenge"; rehab objective; surf value is centered on progression reps; cycling outing modes | He rates an easy scenic stroll above a well-run progression hike |
| D2 | **Immersion / restoration** is a distinct valued mode, not a lesser one ("Best restorative or immersive choice" is a named portfolio role). | MED | Portfolio role he defined | He never picks it, or rates it as filler |
| D3 | **Wildness gradient:** "more wilderness" is a desired direction of refinement. He prefers places that *feel* remote over manicured parks, holding travel constant. | MED | "Same feeling with less driving, more wilderness" is a named interaction | He prefers amenity-rich parks, or wildness adds no value once travel cost is counted |
| D4 | **Scenery, ecology, and solitude are separate axes** he wants to feel. Ecology (distinctive ecosystems, not just views) is plausibly strong. | MED on existence, **UNKNOWN on weights** | Outing-history fields he specified: enjoyment, scenery, ecology, solitude | Post-hike ratings show one axis dominating or one irrelevant |
| D5 | **Rarity and timing:** he values windows that are only good *now* (seasonal phenomena, rare conditions) more than evergreen options. | MED | "Rare-condition window" role; watches on seasonal phenomena and condition regimes | He ignores rare-window alerts in favor of known favorites |
| D6 | **Crowds:** light-to-moderate is fine, and dense or competitive crowding lowers fit. He's probably *not* someone for whom solitude is essential. | LOW-MED | Surf lineup preference (explicit, but a different activity); disliked traffic environments in cycling | He seeks empty trails and rates busy trails sharply lower (→ solitude stronger), or doesn't care |
| D7 | **Water and distinctive landforms** (streams, gorges, lakeshore, dunes, bogs/heath barrens) add delight. | LOW | Saved maps skew to stream gorges (Wissahickon, Patapsco) and unusual ecosystems (Pine Barrens, Dolly Sods/Canaan Valley); lake-oriented activity lanes | He's indifferent to water, or prefers ridges and views |
| D8 | **Exploration / novelty:** new places and route-finding are rewarding, and strong navigation makes this cheap. | LOW | Cycling "exploration" objective; the depth of his navigation skills | He repeats favorites and rates repeats as high as new places |
| D9 | **Low friction is itself a value:** a good transit-reachable hike can beat a better drive-to hike. | MED | Multimodal "may be prioritized"; "Best low-friction choice" role | He always trades more driving for a better place |
| D10 | **Wonder and awe**, plus an interest in overnight/under-the-stars options. | LOW | Co-authored planning sheet | — (co-authored; don't weight without confirmation) |
| D11 | **Ethical access** is part of the pleasure, not only a constraint: public, legitimate, low-impact access, and no secret or sensitive spots. | HIGH | Explicit exclusion rules | — (treat as a rule) |

### 4.1 Explicit UNKNOWNs (calibration targets; do not default)
- Relative weights of scenery vs ecology vs solitude vs challenge vs novelty
- Preferred hike *shape*: loop vs out-and-back vs point-to-point; summit/destination vs journey
- Seasonal preferences (heat and humidity tolerance, bugs, fall color, winter hiking appetite)
- Tolerance for trail-side infrastructure (roads, noise, buildings, rail trails)
- Solo vs companion *preference* (as opposed to safety disposition)
- Whether cultural or historic features add value
- Pace and dwell style (steady mileage vs stops for photography, botany, birding)
- What happened on the named places (Fells, Wissahickon, Pine Barrens, Claremont, Dolly Sods/Canaan): did he hike them, and did he love them?

### 4.2 Fastest path to "no" (elicitation, ≤10 min)
1. **Rate 3–5 past outings** (Patapsco first) on enjoyment, scenery, ecology, solitude, exertion, and repeat desire, 1–5 each. Add one sentence each on *the moment it was best* and *what it would have taken to be better*.
2. **Forced-choice pairs** (answer on instinct):
   - Wissahickon-style wooded gorge 40 min by train vs Dolly Sods-style open heath barrens 4 h by car
   - Hard hike that teaches you something vs easy hike at a rare seasonal peak
   - Busy iconic trail vs quiet unremarkable trail
   - Lakeshore/dunes vs river gorge vs prairie/savanna vs bluff views
   - Loop vs point-to-point via transit
3. **One veto list:** things that reliably ruin a hike for him.

Once answered, promote hypotheses to **accepted USR-HIK-TASTE records** and fold them back into the spec as the hiking AIP-09 packet.
