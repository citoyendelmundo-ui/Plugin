---
name: hike-finder
description: Identify, evaluate, and recommend hiking locations Aaron will love within any specified geography, using his accepted capability/safety profile and his (still-hypothetical) taste profile. Trigger on "where should I hike", "find hikes near/in X", "best hike this weekend", "evaluate this trail", "compare these hikes", or any request to rank or recommend walking/hiking places or routes.
---

# Hike Finder

**Source of truth:** `references/profile.md`. Read it in full before every run. If it conflicts with the Google Doc *Outdoor Opportunity Intelligence System — Product & Engineering Specification*, the spec wins. Flag the conflict.

## Procedure

### 1. Reset the frame before searching
- Pin down: geography, origin (default: Bryn Mawr Red Line, Chicago), date and time window, return-by time, car vs car-free, solo vs companion, and today's body state (Normal / Modify / Restricted).
- Ask only for what changes the answer. Otherwise state the assumption and proceed.
- Name the outing mode: **routine**, **controlled progression** (which *one* dimension?), **restorative/immersive**, or **rare-window**. The mode changes how value is ranked.

### 2. Build the candidate universe from research, not memory
- Use web search and official sources (land managers, state park and forest pages, trail databases, recent trip reports). Get current closures, hours, permits, and trail conditions.
- Enumerate **route configurations**, not parks. Give each: distance, gain (say what it measures), footing, exposure, markings, bailout points, access point, and door-to-door time by car *and* transit.
- A partial scan must say so. Never infer that a good hike doesn't exist from a thin search.

### 3. Gate in the contract order
Identity → legal access → safety → evidence → capability & equipment → time & logistics. Apply the terrain matrix per route feature, the progression rule (one dimension up), and hip-flexion handling (poles Recommended on sustained climbs). Output a readiness state for each candidate. Personal value can't rescue a failed gate.

### 4. Assess personal value separately
- Score against hypotheses D1–D11 in the profile. Say which hypotheses drove the tier.
- Label the tier **provisional** and give personal-fit confidence (Low while the taste layer is unelicited).
- Say what would change the ranking if a hypothesis turned out false.

### 5. Deliver a small portfolio, not a list
Fill three to five roles that apply: **Best overall · Best progression · Best low-friction (transit-friendly) · Best restorative/immersive · Rare-condition window**. For each:
- Route, place, best window, door-to-door time (car and transit)
- Readiness · value tier (provisional) · confidence (operational / fit)
- **Why it fits** (which delight hypotheses) · **why not** (dominant risk or uncertainty) · progression dimension if any
- Terrain axes outside Routine, companion disposition, gear callouts (only material ones), turnaround trigger, bailout
- Last-verified date for conditions and access, with a pre-departure recheck note

Also include a short **"excluded and why"** list for well-known places you dropped: closure, envelope, a stacked progression, or crowding.

### 6. Close the loop
- End with at most two questions from `references/profile.md` §4.2 whose answers would most change *this* ranking.
- After an outing, prompt for the symptom log (pre, during, post, same-day, next-day) *separately* from the taste ratings (enjoyment, scenery, ecology, solitude, exertion, repeat desire).
- When Aaron states a preference, update `references/profile.md`. Move the hypothesis to accepted with its date and source, and never silently change a safety rule.

## Hard rules
- Never merge readiness, value, and confidence into one score.
- Never present an untested terrain dimension as either capable or incapable.
- Never recommend closed, restricted, private, ecologically sensitive, or "secret" access.
- Never invent taste preferences. Unknown stays unknown.
