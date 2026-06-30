# Validated Anchored Rubrics for Under-Covered Qualitative Domains — Focused Report

> Focused second-pass deep-research on the five domains the first report under-covered.
> 6 search angles, 30 sources fetched, 100 claims extracted, top 25 adversarially
> verified (3-vote each) → 24 confirmed, 1 refuted. Date: 2026-06-30.

**Headline:** Validated, anchored/multi-criteria instruments were *verified* in only **two**
of the five target domains — **creativity/originality** and **aesthetic judgment**. For the
other three — **persuasiveness/argumentation**, **epistemic calibration**, and **pedagogical
quality** — the search surfaced credible candidate instruments, but none survived into the
adversarial verification budget, so they are reported below as **unverified leads**, not
confirmed findings. This is itself a useful signal: rigorously *validated* anchored rubrics
with reported reliability are far thinner in those three domains than in creativity/aesthetics.

---

## Domain 1 — Creativity & Originality ✅ (verified)

| Instrument | URL | Domain | Named dimensions / scale | Validation | Wired into judge/RL? |
|---|---|---|---|---|---|
| **TTCW — Torrance Test of Creative Writing** | https://arxiv.org/abs/2309.14556 (orig, CHI 2024) | Creative writing | **14 binary tests** across Fluency / Flexibility / Originality / Elaboration | Per-metric **Fleiss κ ≥ 0.4** retained (Originality-Theme 0.66, Narrative Ending 0.48); LLM-judge agreement acc. 0.69–0.86 passing Alternative Annotator Test | **Yes — both.** LLM-as-judge in CreativityPrism; curiosity-driven RL+SFT judge on 5 TTCW dims (arXiv 2510.05135) |
| **CAT — Consensual Assessment Technique** | https://onlinelibrary.wiley.com/doi/full/10.1002/jocb.462 | Product/creative-work creativity | Holistic expert inter-rater consensus (not per-level descriptors) | Field "gold standard"; mean-rating **ICCs > .90** (61 raters, 90 items, 2 sessions) | Underpins TTCW's expert annotation |
| **MuseScorer / MuseRAG** | https://github.com/cssai-research/MuseScorer · https://arxiv.org/abs/2505.16232 | Idea originality (Alternative Uses Test) | **Frequency-based** originality (statistical infrequency), not anchored descriptors | EMNLP 2025; 5 datasets, 1,143 participants, 16,294 ideas; clustering **AMI=0.59**, participant-level **Pearson r=0.89** | LLM-judge pipeline (RAG + KNN codebook) |
| **CreativityPrism** | https://arxiv.org/html/2510.20091 | LLM creativity (9 tasks, 3 domains) | 3 named dims: **quality, novelty, diversity**; 20 metrics; bundles TTCT/TTCW/AUT/DAT/Creativity Index/CS4 | Per-metric Fleiss-κ filtering + LLM-judge accuracy + Alternative Annotator Test | Holistic LLM-judge framework |

---

## Domain 2 — Aesthetic Judgment / Taste ✅ (verified)

| Instrument | URL | Domain | Named dimensions / scale | Validation | Wired into judge/RL? |
|---|---|---|---|---|---|
| **PARA** | https://arxiv.org/abs/2203.16754 (CVPR 2022) | Image aesthetics | **13 named attributes** (9 objective: aesthetics, quality, composition, colour, DoF, content, light, object emphasis, scene; + 4 subjective: emotion, judgement difficulty, content preference, willingness to share); most on **discrete 1–5 anchored** scales | Large rich-attribute annotation schema | Used to train personalized IAA models |
| **EVA — Explainable Visual Aesthetics** | https://hal.science/hal-02934292v1 · https://github.com/kang-gnak/eva-dataset | Visual aesthetics | **4 attributes** (light/colour, composition/depth, quality, semantics) on **anchored 1–4** (1=very bad … 4=very good) + **11-point** beauty score (0=least … 10=most beautiful) | 4,070 images, 30+ votes each; attributes + weights **linearly explain overall MOS** | License CC0-1.0; basis for explainable IAA |
| **ImageReward** | https://arxiv.org/html/2304.05977v4 · https://github.com/zai-org/ImageReward | Text-to-image preference (alignment+fidelity+aesthetics) | Learned scalar reward (not descriptor rubric) | NeurIPS 2023; **137k expert comparisons**; 65.14% pref acc, beats CLIP/Aesthetic/BLIP | **Yes — RL.** Drives ReFL fine-tuning; ReFL-tuned SD wins **58.4%** in human eval |
| **LAION-Aesthetics predictor** | https://laion.ai/blog/laion-aesthetics/ · https://github.com/christophschuhmann/improved-aesthetic-predictor | Image "likeability" | MLP on CLIP ViT-L/14 → **1–10** "how much do you like this image" | Widely used to filter LAION/SD training data | De-facto aesthetic filter in T2I pipelines |
| **ArtiMuse** (context) | https://github.com/thunderbolt215/ArtiMuse · https://arxiv.org/abs/2507.14533 | Image aesthetics | MLLM, 8-dim attribute analysis + holistic score; ArtiMuse-10K (10k expert images) | Scoring model, not a textual per-level rubric | MLLM judge |

**Refuted during verification:** a claim that every TAD66K image carries ≥1200 *effective*
aesthetic annotations aggregated into a MOS (vote 1-2). TAD66K's public docs do **not**
specify an anchored scale with per-level descriptors or inter-rater reliability — so it is
**not** a validated anchored rubric.

---

## Domains 3–5 — Argumentation, Epistemic Calibration, Pedagogy ⚠️ (UNVERIFIED leads)

The search **found** candidate instruments for all three, but the 25-claim verification
budget was consumed by creativity/aesthetics, so **none of these were adversarially
confirmed**. Treat as starting points to verify, not established facts.

**Persuasiveness / argument & critical-thinking quality**
- **AAC&U VALUE — Critical Thinking rubric** — https://www.aacu.org/value/rubrics/value-rubrics-critical-thinking — widely-used 5-dimension education rubric, anchored 1–4 (Benchmark→Capstone) levels with per-level descriptors. *Verify: published inter-rater reliability.*
- arXiv 2412.05206 and arXiv 2404.09696 — surfaced as argument-quality / LLM-judge papers. *Verify scope & stats.*
- Webis Dagstuhl-15512 Argument Quality corpus — https://webis.de/data/dagstuhl-15512-argquality.html — classic 15-dimension argumentation-quality annotation (flagged "unreliable" fetch; verify directly).

**Epistemic calibration / intellectual honesty / hedging**
- arXiv 2410.20774, arXiv 2508.06225, arXiv 2511.11500 — surfaced as calibration/honesty/hedging-related. *None verified; confirm what each actually measures and whether anchored.*

**Pedagogical / tutoring / explanation quality**
- **UnifyingAITutorEvaluation** — https://github.com/kaushal0494/UnifyingAITutorEvaluation — unified tutor-evaluation taxonomy/rubric. *Verify dimensions & reliability.*
- arXiv 2507.10579 and arXiv 2502.18940 — surfaced as tutoring/pedagogy evaluation. *Unverified.*
- (Cross-ref first report: **MathTutorBench** — https://github.com/eth-lre/mathtutorbench.)

---

## Strongest validated anchored rubrics per covered domain

**Creativity:**
1. **TTCW** — the most validation-rich *and* the most clearly wired into both LLM-judge and
   RL pipelines. The reference instrument to copy.
2. **CAT** — gold-standard reliability (ICC > .90), though holistic not per-level.
3. **MuseScorer/MuseRAG** — best *automated, scalable* originality scorer (r=0.89), but
   frequency-based rather than anchored-descriptor.

**Aesthetics:**
1. **PARA** — closest to a true anchored multi-attribute rubric (13 attributes, 1–5 anchors).
2. **EVA** — validated weighted linear decomposition of overall aesthetics into named attributes.
3. **ImageReward (+ ReFL)** — the clearest case of an aesthetic/preference signal already
   used as an **RL reward**, with strong human-preference validation.

## What makes the validated ones effective
- **Decompose** the holistic quality into named sub-dimensions (TTCW's 14 tests; PARA's 13 attributes; EVA's 4 axes).
- **Keep only reliable dimensions** — TTCW/CreativityPrism explicitly *discard* dimensions below Fleiss κ ≥ 0.4. (Notably, most TTCW dimensions did **not** reach usable LLM-judge agreement — a ceiling signal for automated creativity grading.)
- **Validate against humans** with a reported statistic (ICC, Pearson r, Fleiss κ, preference accuracy) before trusting the instrument.
- **Anchor the scale** — PARA/EVA's discrete ordinal anchors beat free-form numeric scores for reproducibility.
- For RL: prefer instruments already shown to **move human-eval win-rates** (ImageReward/ReFL's 58.4%) and watch reward-hacking on the un-anchored learned scorers.

## Caveats
- **Three of five domains unconfirmed.** Argumentation, epistemic calibration, and pedagogy
  have candidate instruments (above) but **no verified claim** in this set — a real gap worth
  a dedicated third pass if those domains matter to you.
- **Terminology:** several "rubrics" here are frequency-based scorers (MuseScorer), holistic
  inter-rater methods (CAT), endpoint-anchored numeric scales (EVA overall, LAION 1–10), or
  learned reward models (ImageReward, ArtiMuse) — **not** true per-level descriptor rubrics.
  PARA and EVA's 1–4 attribute scale come closest.
- **Access:** arXiv/HAL/HF pages were frequently 403-blocked to direct fetch; confirmations
  leaned on WebSearch synthesis + official GitHub mirrors. Headline stats (ICC>.90, r=0.89,
  κ≥0.4, 58.4% ReFL win, 137k pairs) were independently corroborated.
- **Recency:** CreativityPrism and the curiosity-driven judge are Oct-2025 preprints at review
  stage; ArtiMuse's CVPR 2026 acceptance is self-reported.
