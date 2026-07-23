# VC-Funded RL Environment / Task / Verifier Companies (2022 – Jul 2026)

> Exhaustive market inventory. Two-pass method (run 2026-07-02): **8 independent
> discovery lenses** (news, VC portfolios, funding databases, analyst maps,
> accelerators, global, verifiers-specific, rebrands/M&A) → **59 new companies**
> on top of a ~20-company seed → **76 enriched** for funding-in-window, scope,
> tier, status, and a one-sentence differentiation claim.
>
> **Scope:** companies building (a) RL **environments**/gyms, (b) agentic
> **tasks**/data-for-RL, or (c) **verifiers**/reward-models/RLVR — for LLM/agent
> training. **Excluded per your instruction:** robotics/AV/embodied-RL/physical
> simulation. Global. Accelerator-stage included; bootstrapped listed separately.
>
> **Result:** **60 qualifying companies** (in-scope, VC/accelerator-funded, round
> in-window) across 3 tiers; 2 bootstrapped/public; 11 excluded (out of scope).
> `ᵃᶜ` = since acquired. Full funding rounds, founders, sources per company in
> `rl-env-funded-companies.csv`.
>
> **Caveats:** many are seed/pre-seed with **undisclosed** amounts (YC/accelerator
> deals); several figures come from aggregators (Crunchbase/Tracxn/StartupHub) not
> primary filings — confidence is per-row in the CSV. Same-name disambiguation was
> applied throughout (Refresh, Lucid, Theta, Dojo, Matrices, Composio are common
> names); notable identity flags are in each row's redFlags.

---

## Tier 1 — Pure-plays (core product is RL environments / tasks / verifiers) — 35

| Company | Cat | Geo | Total raised | Key round | Differentiation (their claim) |
|---|---|---|---|---|---|
| **Andon Labs** | mixed | San Francisco | ~$500K | YC Winter 2024 batch (pivoted… | Builds long-horizon agent benchmarks/environments (Vending-Bench, Butter-Bench, Blueprint-Bench) that measure agentic coherence and safety, and runs … |
| **Andromede** | mixed | Lausanne | Undisclosed | Backed by Unusual Ventures (s… | RL data lab that programmatically generates environments, tasks, and verifiers from real-world data for post-training and evaluation of frontier agen… |
| **Aviro** | mixed | San Francisco | Undisclosed (YC… | Pre-seed round (amount, lead … | Builds RL environments and benchmarks (e.g. Enterprise Search Benchmark) for long-horizon tool use across ML research, live web, and enterprise knowl… |
| **Axiom Math** | verif | US (Bay Area … | $64M | Seed: $64M at ~$300M valuatio… | Builds a self-play 'conjecturer + prover' loop that generates and mechanically proves math problems, outputting machine-checkable Lean proofs (AxiomP… |
| **BenchFlow** | mixed | San Francisco | ~$1M (seed, rep… | Seed round ~$1M (per aggregat… | Open-source 'environment lab' providing a universal framework to run agents against RL environments (SkillsBench, ClawsBench mock-workplace envs) plu… |
| **Bespoke Labs** | mixed | Mountain View | $40M | $40M total announced July 6, … | Pairs world-class data-curation research (OpenThoughts dataset, Bespoke Curator, Terminal-Bench) with best-in-class RL environments to train and veri… |
| **Chakra Labs** | env | Brooklyn | ~$10.1M | Seed round ~$10.1M, reported … | Builds high-fidelity, deterministic computer-use RL environments (SPA/app clones) and human trajectory datasets — its Dojo suite brings frontier-lab-… |
| **Collinear AI** | mixed | San Francisco | Undisclosed (se… | Seed round (undisclosed amoun… | SimLab builds sandboxed, stateful enterprise RL environments (simulating tools like Jira, ServiceNow, Shopify, EMR, airline/hotel systems) that emit … |
| **Datacurve** | mixed | San Francisco | ~$17.7M | Series A: $15M, announced Oct… | An expert-curated coding data foundry (gamified 'Shipd' bounty platform with 14,000+ vetted programmers, paying for outputs not hours) supplying fron… |
| **Deeptune** ᵃᶜ | env | New York | $43M (pre-acqui… | Series A: $43M, closed/announ… | Builds high-fidelity RL 'training gyms' that simulate real professional workflows (accounting, customer support) across apps like Slack and Salesforc… |
| **Dojo (by Chakra Labs)** | env | Brooklyn | N/A (rolls up t… | No standalone financing — Doj… | A collaborative/open RL-environment suite giving computer-use agents deterministic, frame-accurate clones of production software plus crowd-sourced h… |
| **Fleet** | env | San Francisco | ~$15M closed se… | Series A REPORTED/CLOSING Apr… | Builds RL training 'gyms' — high-fidelity simulated replicas of enterprise software like Salesforce and Excel — that frontier labs pay to train agent… |
| **General Reasoning** | mixed | London | ~$10.9M | Seed: $10,904,992 in equity p… | Builds open reasoning-data and RL-environment infrastructure — reasoning datasets and verifiable-reward (RLVR) tooling/environments — for frontier fo… |
| **Habitat** | env | New York | Undisclosed | A Crunchbase seed funding-rou… | Builds RL environments for white-collar / agentic work automation — code and desktop (computer-use) interaction environments offering hundreds of div… |
| **Haize Labs** | verif | New York City | ~$12.5M | Seed: $12.5M led by General C… | Builds Verdict, a declarative framework for composing scalable LLM judges / automated verifiers and reward models, paired with large-scale automated … |
| **Halluminate** | mixed | San Francisco | Undisclosed (ag… | Y Combinator S25 (Summer 2025… | Builds computer/browser-use RL gyms — a fully-simulated internet ('Westworld') of synthetic consumer/enterprise apps — with verifiable rewards, narro… |
| **Harmonic AI** | verif | Palo Alto | ~$295M+ | Series C: $120M at $1.45B val… | Builds 'Mathematical Superintelligence' via its Aristotle model that translates natural-language math into Lean 4 and formally verifies every proof s… |
| **HUD** | mixed | San Francisco | Undisclosed (YC… | Seed (undisclosed amount, ~20… | Open-source SDK + hosted gateway to wrap real software as isolated, agent-callable RL environments and evals specifically for computer-use and browse… |
| **Idler** | env | San Francisco | Undisclosed (YC… | Pre-seed / accelerator: Y Com… | Builds reinforcement-learning training environments from real-world, expert-level coding problems so foundation labs can train and evaluate code-gene… |
| **Judgment Labs** | verif | San Francisco | $32M | $32M total across a Seed and … | Builds a 'continuous improvement layer' / evaluation-and-verifier infrastructure for deep AI agents that scores long reasoning traces, tool use and m… |
| **Lucidic AI** | mixed | San Francisco | ~$500K | YC Winter 2025 (W25) batch; $… | A training/eval platform that ingests real agent logs and uses controlled simulations plus RL, genetic algorithms and Bayesian optimization — scored … |
| **Maingen** | env | San Francisco | Undisclosed (YC… | Y Combinator S26 accelerator … | Builds RL environments for industrial operations (framed as a ~$5T slice of the US economy) so frontier labs can train models that run factories. |
| **Mechanize** | mixed | San Francisco | ~$9.1M | Seed: $9.1M at $500M post-mon… | Builds robust, high-fidelity RL environments, benchmarks, and training data ('digital office' simulations) for frontier coding/agentic tasks, working… |
| **Micro1** | task | San Francisco… | ~$41.6M | Series A $35M led by 01 Advis… | Runs an AI-vetted, top-1% expert network (PhDs, senior engineers) supplying on-demand RLHF and agentic training data to frontier AI labs, positioned … |
| **Plato** | env | San Francisco | Undisclosed (pr… | Pre-seed/seed (2025) — invest… | Builds simulated 'worlds' — high-fidelity replicas of real websites/software (Amazon/Airbnb/Gmail-style) plus a full Linux desktop 'Computer Use' tar… |
| **Preference Model** | env | San Francisco | Undisclosed | Seed round (amount undisclose… | Builds high-quality RL training environments that reflect real-world complexity with diverse tasks and robust reward functions, partnering directly w… |
| **Proximal** | mixed | San Francisco | Undisclosed (se… | Seed round (amount undisclose… | Builds high-fidelity, long-horizon RL coding environments grounded in real codebases using software-driven data engines (not human contractors), plus… |
| **Refresh** | mixed | San Francisco | Undisclosed (YC… | Y Combinator X25 (later relab… | Builds simulation-environment 'training gyms' with deterministic and rubric-based verifiable rewards that turn real software-engineering and computer… |
| **Rubric AI** | verif | San Francisco | ~$500K (reporte… | Seed / YC standard deal — par… | Turns credentialed expert judgment into rubric-based reward signals and RL environments for non-verifiable/high-stakes domains where ground-truth ver… |
| **Sepal AI** ᵃᶜ | mixed | San Francisco | ~$500K (pre-acq… | YC Summer 2024 batch; ~$500K … | Data-research company producing high-quality training data, expert-graded evaluation benchmarks and RL environments for frontier LLMs, drawing on a n… |
| **Taste Labs** | mixed | New York | $18.5M | Seed: $18.5M, June 2026, co-l… | Builds the 'taste layer' — preference datasets, rubrics, evaluation environments and RL post-training data to give frontier models and agents subject… |
| **The LLM Data Company (TLDC / doteval)** | mixed | San Francisco | $500K–$3.6M (co… | YC X25 (Spring 2025) + pre-se… | Builds post-training data and RL environments for frontier labs in critical/expert domains, plus 'doteval' tooling to write, version and execute eval… |
| **Theta (Theta Software)** | env | San Francisco | Undisclosed (YC… | Y Combinator X25 (Spring 2025… | Translates real-world enterprise workspaces/software into high-fidelity simulation environments to train and post-train expert-level computer/browser… |
| **Veris AI** | env | San Francisco | $8.5M | Seed: $8.5M, closed/announced… | Trains enterprise AI agents through high-fidelity simulated experience (RL-style learning by doing) rather than prompt engineering or human-labeled d… |
| **Vmax** | mixed | San Francisco | Undisclosed (ea… | Backed by Race Capital and So… | Automates converting a customer's proprietary data and evals into RL environments for LLM-based agents, targeting long-horizon and coding tasks (e.g.… |

---

## Tier 2 — Incumbent data/eval companies with an RL-environments line — 7

| Company | Cat | Geo | Total raised | Key round | Differentiation (their claim) |
|---|---|---|---|---|---|
| **Alignerr (Labelbox)** | task | San Francisco | ~$189M (parent … | Alignerr is not separately fi… | Positions itself as an on-demand marketplace of 2.6M+ vetted domain experts generating RLHF, complex-reasoning and multimodal reward signals for fron… |
| **Centific** | env | Redmond / Sea… | $60M | Series A: $60M, June 2025, le… | Launched 'RL Environments-as-a-Service' — configurable, industry-authentic simulated enterprises for training and evaluating enterprise AI agents aga… |
| **Huzzle Labs** | mixed | London | ~$6M (reported) | ~$6M raised (aggregator-repor… | Human-intelligence 'data foundry' bundling long-horizon RL environments, expert trajectory data, and contextual evals for code/tool-use/computer-use/… |
| **Invisible Technologies** | env | New York | ~$144M | $100M growth round, Sep 16 20… | Builds production-grade RL environments from real enterprise workflows with domain-expert-designed reward functions and fully logged, inspectable, re… |
| **Pareto AI** | task | San Francisco | ~$14M (aggregat… | Seed: $4.5M closed 14 Mar 202… | Talent-first expert human-data platform positioning itself as 'the verification layer for reinforcement learning on real-world expertise,' supplying … |
| **SuperAnnotate** | env | San Francisco | ~$50M+ | Series B: $36M, Nov 2024, led… | Data-annotation/data-management incumbent now designing and running end-to-end RL environment programs — collecting human trajectories and building r… |
| **Toloka** | mixed | Amsterdam | $72M disclosed … | May 7, 2025: $72M (~€64M) str… | A large established AI-data/eval provider that has added RL-gyms and multi-user virtual-organization environments producing high-fidelity trajectorie… |

---

## Tier 3 — Adjacent infrastructure (RL training infra / agent sandboxes; in the ecosystem, not a core env/task/verifier product) — 18

*Included for completeness because they're frequently cited in this market, but
they sell training infra or sandboxes rather than environments/tasks/verifiers
as the product.*

| Company | Cat | Geo | Total raised | Key round | Differentiation (their claim) |
|---|---|---|---|---|---|
| **Adaptive ML** | verif | New York | $20M | $20M seed (announced March 12… | Adaptive Engine is an enterprise RLOps platform that fine-tunes, evaluates and serves open-source LLMs using RLHF/RLAIF, generating reward signals an… |
| **AgileRL** | mixed | London | ~$7.5M | Seed: £5.5M / ~$7.5M, announc… | Open-source RL framework plus a managed full-stack RLOps product (Arena) that speeds up reinforcement learning ~10x with distributed training and env… |
| **Composio** | env | San Francisco | ~$29M | Series A: $25M led by Lightsp… | Positions as the 'learning layer' for agentic AI — providing tool-calling infrastructure (200+ app integrations) plus RL-style environments and skill… |
| **Coval** | env | San Francisco | ~$31M | Series A $28M led by Norwest … | Applies autonomous-vehicle-style simulation (millions of simulated test runs) to stress-test, evaluate and monitor voice and chat AI agents for relia… |
| **E2B** | env | San Francisco | ~$32M (aggregat… | Series A: $21M led by Insight… | Provides secure, isolated cloud code-execution sandboxes as the runtime substrate for AI agents — increasingly adopted as the execution environment l… |
| **Gray Swan AI** | verif | Pittsburgh | ~$45M+ (Series … | Series A: $40M, closed ~May/J… | AI-security company whose Arena red-teaming community (15,000+ researchers) and Shade adversarial-testing engine generate the adversarial data and gr… |
| **Kaizen (Kaizen Automation)** | env | San Francisco | ~$4M+ | Seed: 'over $4M' (reported ~O… | Builds RL environments that simulate real operational 'work' — legacy web-portal/back-office tasks across healthcare, logistics, and financial servic… |
| **Maxim AI** | verif | San Francisco | $3M | Seed: $3M, announced Jun 2024… | End-to-end agent simulation, evaluation and observability platform with a configurable graders/evaluators engine to test AI agents across scenarios w… |
| **Morph Labs** | mixed | San Francisco | ~$5.75M | Seed: $5.75M led by Khosla Ve… | Builds Infinibranch, a rapid compute-branching / snapshot environment infrastructure for massively parallel agents, aimed at autoformalization and 'v… |
| **Nous Research** | env | New York / Un… | ~$65M (≈$15M ea… | Series A $50M led by Paradigm… | Publishes Atropos, an open-source LLM reinforcement-learning environments framework (1,200+ tasks across math/code/tool-use) for collecting and evalu… |
| **OpenPipe** ᵃᶜ | verif | Seattle / Bel… | $6.7M disclosed… | Acquired by CoreWeave (announ… | Open-source Agent Reinforcement Trainer (ART) that RL-fine-tunes agents via rollouts, custom reward functions (RULER), and GRPO to teach agents to re… |
| **Osmosis** | mixed | San Francisco | $6.3M | Seed: $6.3M, announced Oct 20… | A forward-deployed reinforcement fine-tuning platform that captures customers' real-world feedback, converts it into structured reward functions, and… |
| **Periodic Labs** | verif | San Francisco | $300M (confirme… | Seed: $300M, announced Sept 3… | Building an autonomous physical lab so that real experiments serve as the RL environment and produce experimentally-verified reward signals ('nature … |
| **Predibase** ᵃᶜ | verif | San Francisco | ~$28M pre-acqui… | Acquired by Rubrik, announced… | End-to-end reinforcement fine-tuning (RFT) platform that lets teams fine-tune open-source models using user-defined reward functions/graders instead … |
| **Prime Intellect** | mixed | San Francisco | >$150M | Seed extension: $15M in Feb 2… | Runs an open 'Environments Hub' ('Hugging Face for RL environments', 2,500+ community environments plus verifiers and the PRIME-RL framework) alongsi… |
| **Runloop** | env | San Francisco | $7M | Seed: $7M, closed/announced J… | Provides enterprise-grade 'Devboxes' — secure isolated micro-VM sandboxes plus GitHub integration, snapshots, blueprints, and public coding benchmark… |
| **RunRL** | mixed | San Francisco | ~$500K | Seed / accelerator round ~$50… | RL-as-a-service platform where users define a metric/reward and RunRL trains their model or agent with reinforcement learning without them managing G… |
| **TrainLoop** | mixed | San Francisco | ~$500K | Seed: ~$500K, early/March 202… | Post-training research/product lab that turns enterprise data and evals into RL-fine-tuned ('reasoning fine-tuning') expert models for long-horizon d… |

---

## Bootstrapped / public (RL-env work, no qualifying venture round) — 2

- **AIChamp** (bootstrapped, San Francisco, CA…) — Builds custom RL environments and 'Virtual Gym' simulations for training and evaluating tool-using agents on …
- **Innodata** (public, Ridgefield Park, …) — Data-engineering incumbent offering custom RL gyms/environments as a managed service with deterministic evalu…

> Also relevant but not enriched in this pass: **Surge AI** (bootstrapped;
> operates an internal RL-environments org but has taken no qualifying VC — its
> reported ~$1B raise was still unclosed as of this session) and **Invisible
> Technologies** (bootstrapped/profitable; builds RL environments from enterprise
> workflows). Both belong in this "does the work, no qualifying VC" bucket.

---

## Excluded — out of scope (11)

Surfaced by discovery but filtered out on inspection, with the reason:

- **Applied Compute** — inScope=false: core product is a vertically-integrated enterprise RL AGENT (customer-facing 'Specific Intelligence'), not a saleable RL environment /…
- **Cekura (formerly Vocera)** — Product is agent QA/testing/observability (simulated-user eval + production monitoring of deployed voice/chat agents), not RL environments/tasks/rewa…
- **Cua (trycua)** — Agent-sandbox/container infrastructure, not a core RL-environment/task/verifier product (though it ships benchmarks and is used for RL/eval), hence a…
- **Cyberdesk** — Scope=false: Cyberdesk is a virtual-desktop sandbox / computer-use-agent infrastructure and production RPA-style automation product, not an RL-enviro…
- **Daytona** — Sandbox/compute infrastructure provider, not a core RL-environment/task/verifier product — RL is a use case its sandboxes serve, hence adjacent-infra…
- **General Intuition** — OUT OF SCOPE: General Intuition is a frontier foundation-model lab building action/world models for embodied/spatial-temporal reasoning (gaming-to-ro…
- **Gensyn** — OUT OF SCOPE as an env/task/verifier vendor: Gensyn builds decentralized RL COMPUTE INFRASTRUCTURE (RL Swarm) for post-training, not RL environments,…
- **Hamming AI** — Same scope reasoning as Cekura: automated testing/simulation/monitoring/governance for deployed AI voice agents (eval + reliability), not RL environm…
- **Lucid** — Scope=false: Lucid's learned world-model 'RL gym' targets robotics (embodied training) and gaming, i.e. physical-world/embodied and game simulation, …
- **Matrices** — Major scope/identity discrepancy: concrete public product evidence (Tracxn, Crunchbase, bizapedia) describes an AI-powered spreadsheet agent product,…
- **TensorZero** — OUT OF SCOPE as an env/task/verifier product: TensorZero is an LLM OPTIMIZATION GATEWAY / LLMOps stack. It uses RL feedback loops (RLHF/DPO) to optim…

---

## What the landscape shows (synthesis)

- **The category is real and crowded fast.** ~60 venture-funded companies now
  explicitly sell RL environments, tasks, or verifiers — most founded 2024–2026,
  most seed/pre-seed, heavily YC-originated (HUD, Refresh, Aviro, Idler, Maingen,
  Rubric AI, RunRL, Cyberdesk, Lucidic, TLDC, Halluminate, Osmosis).
- **Three sub-markets are forming:** (1) **environments/gyms** — the largest,
  computer-use & coding-agent focused (Fleet, Mechanize, DeepTune, Chakra, HUD,
  Refresh, Runloop, Plato); (2) **verifiers/RLVR & formal reward** — the fastest-
  scaling on capital (Harmonic ~$875M val, Axiom Math $64M seed, Judgment Labs
  $32M, Gray Swan $40M); (3) **task/expert-data foundries** adding RL-env lines
  (Mercor, Turing, Snorkel, Toloka, SuperAnnotate, iMerit, Micro1).
- **Biggest rounds ≠ pure-plays.** The heaviest capital sits with verifier/reasoning
  and world-model-adjacent plays; the environment pure-plays are mostly small
  seeds except Fleet (~$725–750M val) and DeepTune ($43M Series A, a16z).
- **Consolidation already started:** Sepal→Mercor, OpenPipe→CoreWeave,
  Predibase→Rubrik — the pattern the Scale/Surge incumbents predicted.
- **Global but US-dominated:** UK (AgileRL, Huzzle, General Reasoning), France/CH
  (Andromede, Adaptive ML), NL (Toloka), India (Composio, Maxim, iMerit) present,
  but the center of gravity is SF.
