# RL Environments & Nuanced Qualitative Grading Rubrics — Research Report

> Generated via the deep-research harness (6 search angles, 27 sources fetched, 113 claims
> extracted, top 25 adversarially verified with 3-vote each → 25/25 confirmed, 0 refuted).
> Date: 2026-06-30.

**Bottom line:** There is a rich, fast-moving 2025–2026 ecosystem of open-source RL
environments/frameworks whose reward comes from **rubric scoring or LLM-as-judge** rather
than numeric game scores, plus several effective **anchored, named-scale rubrics** for
"unquantifiable" domains (medical communication, empathy, open-ended reasoning). The
strongest *infrastructure* is Prime Intellect's **Verifiers** and Qwen's **OpenRS**; the
strongest *rubric designs* are **RaR**, **HealthBench**, and **Kardia-R1**. Much of this
corpus is very recent and author-self-reported — see Caveats.

---

## Part 1 — RL environment repos / frameworks (judge- or rubric-based reward)

| Repo / framework | URL | What it is | License / activity |
|---|---|---|---|
| **Verifiers** (Prime Intellect) | https://github.com/PrimeIntellect-ai/verifiers | Library for building RL environments + evals where reward IS a `Rubric`. First-class `Rubric`, `JudgeRubric`, `MathRubric`, `RubricGroup` abstractions; one of three mandatory env components. | MIT, ~4.2k stars, active through 2026 |
| **OpenRS** (Qwen Apps) | https://github.com/Qwen-Applications/OpenRS | "Open Rubric System" — LLM-as-judge framework replacing scalar reward models with adaptive, query-type-specific rubrics; 50+ rubrics with weighted criteria (critical/core/important/highlight) → multi-dimensional verdicts. | Apache-2.0, new/low-star (~19) |
| **prime-rl** (Prime Intellect) | https://github.com/PrimeIntellect-ai/prime-rl | Distributed RL trainer that consumes Verifiers environments (rubric rewards in the loop). | Open source, active |
| **ART** (OpenPipe) | https://github.com/OpenPipe/ART | Agent RL trainer with **RULER** — a general-purpose LLM-as-judge reward that scores trajectories without hand-written reward functions. | Apache-2.0, active |
| **awesome-RLVR** (OpenDILab) | https://github.com/opendilab/awesome-RLVR | Curated index of RL-with-verifiable/rubric-reward papers and repos — good map of the field. | Curated list |
| **The Rules of the Game** survey | https://github.com/RUC-NLPIR/Rubrics_Survey | Survey formalizing rubrics, distinguishing them from reward models / RLVR / LLM-as-judge; 3-category taxonomy (construction, training, evaluation). | Paper + repo, May 2026 |

---

## Part 2 — Rubrics that put named scales on "unquantifiable" qualities

| Rubric / system | URL | Domain | Named dimensions / scale | Example anchor |
|---|---|---|---|---|
| **RaR — Rubrics as Rewards** (Scale AI, Gunjal et al.) | https://arxiv.org/abs/2507.17746 · https://scale.com/blog/rubrics-as-rewards | Real-world reasoning (medicine, science) without single ground truth | 7–20 binary criteria, each tagged **Essential / Important / Optional / Pitfall**; weights **1–5** positive, **−1/−2** for Pitfalls; reward = weighted-sum-normalized (Explicit) or holistic Likert judge (Implicit) | Pitfall criterion (e.g. "fails to flag drug interaction") scored −2 |
| **HealthBench** (OpenAI) | https://arxiv.org/html/2505.08775v1 | Medical communication | Physician-written, conversation-specific criteria across **5 axes**: accuracy, completeness, communication quality, context awareness, instruction following; point values **−10 (harmful) … +10 (ideal)** | 262 physicians, 48,562 criteria; GPT-4.1 grader macro **F1 = 0.71**, ≈ inter-physician agreement |
| **Kardia-R1 / Rubric-ERL** | https://arxiv.org/abs/2512.01282 · https://github.com/JhCircle/Kardia-R1 | Empathy / emotional-support dialogue | GRPO reward from **5 named axes**: Relevance, Empathy, Persona Consistency, Safety, Fluency; "no black-box reward model → fully interpretable" | Per-axis explainable rubric score replaces opaque RM |
| **RuscaRL** | https://arxiv.org/html/2508.16949v3 · https://github.com/IANNXANG/RuscaRL | Open-ended reasoning / medical | Checklist criteria with numeric `points`, can be negative | "+5" instruction-following; "−6" clinical error |
| **BiGGen-Bench** (Prometheus) | https://huggingface.co/datasets/prometheus-eval/BiGGen-Bench | Fine-grained LLM-as-judge (77 capabilities) | **Instance-specific 1–5 rubric**, explicit description for each of the 5 levels | Each of 765 instances ships its own per-level descriptors |
| **RULERS** | https://arxiv.org/abs/2601.08654 (code: https://github.com/LabRAI/Rulers) | Robust LLM evaluation | Compiles NL rubrics into versioned "locked" specs; forces judge to anchor each level to evidence | Evidence-anchored level scoring |
| **EQ-Bench creative-writing-bench** | https://github.com/EQ-bench/creative-writing-bench | Creative writing craft | Multi-criterion LLM-judge rubric over creative-writing dimensions | Closest item in this set on creativity/taste |
| **MathTutorBench** | https://github.com/eth-lre/mathtutorbench | Pedagogical quality (tutoring) | Rubric/judge scoring of tutor pedagogy | Pedagogy-focused benchmark |

**Methodology worth knowing:**
- **RRD** — https://arxiv.org/abs/2602.05125 — recursive decompose-filter rubric refinement
  with correlation-aware weighting; names the failure modes that wreck rubrics (lack of
  coverage, conflated dimensions, misaligned preference direction, redundant/correlated criteria).
- **GER-Eval** — https://github.com/Clemenciah/llm-generated-rubrics (MIT) — LLM-designed vs.
  human-defined rubrics.
- **Self-Rewarding Rubric RL** — https://arxiv.org/pdf/2509.25534 — policy mines/grades its own rubrics.
- **QuRL** — https://iclr.cc/virtual/2026/poster/10010742 (ICLR 2026) — auto-mines question-specific rubrics as GRPO reward.

---

## The 3–5 strongest examples (and why they work)

1. **RaR (Rubrics as Rewards)** — the canonical design. Decomposes holistic quality into
   7–20 *binary, instance-specific* criteria with **named importance tiers** (Essential→Pitfall)
   and explicit weights including negatives. +31% on HealthBench, +7% GPQA-Diamond over Likert baselines.
2. **HealthBench** — the gold standard for *validation*: 262 physicians authored 48,562 weighted
   criteria, and the LLM grader hit **F1 = 0.71 vs. physicians ≈ inter-physician agreement**.
   The load-bearing proof that an LLM-as-judge can approximate expert grading of a qualitative quality.
3. **Kardia-R1** — proves the pattern extends to a "soft" quality (empathy) via 5 explainable
   named axes, explicitly replacing a black-box reward model.
4. **Verifiers + OpenRS** — the infrastructure that makes rubric reward a *first-class primitive*
   you can train against (named weight tiers: critical/core/important/highlight).
5. **BiGGen-Bench** — best off-the-shelf example of *per-instance anchored 1–5 scales* with a
   described anchor at every level.

**What makes them effective (recurring design choices):**
- **Decompose** holistic quality into many *binary, instance-specific* checks rather than one global Likert score.
- **Attach named categorical weights/anchors** (importance tiers, per-level descriptors, point values including penalties).
- **Aggregate** via weighted normalization *or* delegate to a holistic LLM judge.
- **Validate judge–human agreement** (HealthBench's F1 is the model to copy).
- **Refine** to kill correlated/conflated/misaligned criteria (RRD).

---

## Caveats & gaps

- **Recency/maturity:** Much of this is brand-new (RaR Jul 2025; RuscaRL Aug 2025; Kardia-R1
  Dec 2025; OpenRS/RRD/GER-Eval/survey Feb–Jun 2026). Several repos are low-star and newly
  created; durability, adoption, and reproducibility are unproven. Most quantitative figures
  (50+ rubrics, point weights, F1=0.71) are author-self-reported.
- **HealthBench self-interest:** OpenAI grades with its own GPT-4.1, and 0.71 partly reflects
  high physician–physician disagreement on borderline cases, not high absolute accuracy.
- **Access:** Direct arXiv PDF fetches were 403-blocked via the egress proxy for several papers;
  some quotes came from search snippets + official author GitHub repos (still cross-corroborated).
- **Domain coverage gap:** The strongest *validated* rubrics cluster in **medicine and empathy**.
  For **creativity/originality, aesthetic taste, persuasiveness, epistemic calibration,
  pedagogical quality**, only weaker/less-validated instruments surfaced (EQ-Bench
  creative-writing-bench, MathTutorBench). A focused second pass on these domains is warranted.

## Open questions

- Are there rigorously validated anchored rubrics for creativity/aesthetics/persuasion/calibration/pedagogy?
- How robust are these LLM-judge rubric rewards to reward-hacking during RL training?
- Do LLM-*generated* rubrics match human-authored ones (HealthBench's 262 physicians) in reliability?
