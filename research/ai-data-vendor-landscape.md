# The AI Training-Data, RL-Environments & Evals Vendor Landscape

## A market inventory and job-fit analysis

> Deep-research run of 2026-07-02: 6 search angles, 23 sources fetched, 81 claims
> extracted, 15 load-bearing claims adversarially verified (3-vote each, all 15
> confirmed 3–0). The run hit a session token limit partway through verification,
> so remaining claims carry source citations but not formal verification — each
> item below is flagged accordingly.
>
> **Targeted second verification pass (2026-07-02):** the 6 decision-driving
> claims (OpenAI insourcing, Surge $25B talks, Mercor gig-rubric structure,
> Anthropic $1B env spend, Fleet financials, Handshake $1B run rate) were each
> attacked by 3 independent skeptic agents (primary-source, contradiction, and
> freshness lenses). **All 6 confirmed 18–0**, with material freshness updates
> incorporated below and marked "*Update (Jul 2026)*".
>
> **Legend:** ✅ = adversarially verified (3–0) · 📰 = sourced/reported, not
> formally verified · ◻ = roster entry from category knowledge, not verified
> this pass — confirm before relying on it.
>
> **Reader lens:** job seeker targeting full-time PM / product-research /
> program-ops roles; strengths in B2B/D2C customer discovery, qualitative
> research, rubric design, writing; SF Bay Area onsite acceptable.

---

## 1. Market context — the five facts that frame everything

1. **The market re-priced from "labeling" to "expert data + environments."** 📰 The
   data annotation market is projected to grow from $1.2B (2024) to $10.2B (2034);
   the RLHF-platform slice from $2.8B (2025) to $18.6B (2034)
   ([Lemon.io](https://lemon.io/blog/rlhf-platforms-for-data-annotation/)). But the
   growth is concentrating at the premium end.

2. **The Scale AI shock (June–July 2025).** 📰 Meta invested $14.3B for ~49% of
   Scale (~$29B valuation) and hired away CEO Alexandr Wang; within weeks OpenAI
   and Google began cutting ties, and Scale laid off 200 FTEs (14%) + 500
   contractors, concentrated in the labeling core
   ([TechCrunch](https://techcrunch.com/2025/07/16/scale-ai-lays-off-14-of-staff-largely-in-data-labeling-business/)).
   Neutrality is a real asset in this market; losing it is a real liability.

3. **RL environments are the new gold rush.** ✅ Anthropic leadership has discussed
   spending **>$1B on RL environments over the next year** (The Information, "How
   Anthropic and OpenAI Are Developing AI 'Co-Workers'", Sep 2025; echoed by
   [TechCrunch](https://techcrunch.com/2025/09/21/silicon-valley-bets-big-on-environments-to-train-ai-agents/)
   and [Epoch AI](https://epoch.ai/gradient-updates/state-of-rl-envs)).
   Investors are explicitly hunting for a "Scale AI for environments."
   *Update (Jul 2026):* no denial or walk-back; parallel reporting had OpenAI
   planning ~$1B on experts/RL environments in 2025, rising toward $8B by 2030,
   and TechCrunch reported General Intuition's $2.3B RL-environments bet (Jun 2026).

4. **The insourcing threat is live — but directional, not total.** ✅ OpenAI is
   building an in-house human-data team to reduce dependence on Surge, Mercor, and
   Handshake ([SemiAnalysis](https://newsletter.semianalysis.com/p/rl-environments-and-rl-for-science));
   corroborated by OpenAI's internal **Feather** contractor platform (USPTO
   trademark for data labeling/annotation; Tom's Guide) and an actively-hiring
   "Human Data" team on openai.com/careers (Software Engineer, Engineering Manager,
   TPM, **Program Manager Human Data**). *Update (Jul 2026):* insourcing runs in
   parallel with continued vendor use — labs still spend ~$1B/yr on external human
   data, and OpenAI was simultaneously deepening work with Handshake (TechCrunch,
   Jan 2026). Every vendor's biggest customers remain its most capable potential
   competitors.

5. **Credible insiders are split on the RL-env cluster's durability.** 📰 OpenAI's
   API eng head Sherwin Wu says he's "short" RL-environment startups; Karpathy is
   "bullish on environments… bearish on reinforcement learning specifically";
   Ross Taylor warns of reward hacking ([TechCrunch](https://techcrunch.com/2025/09/21/silicon-valley-bets-big-on-environments-to-train-ai-agents/)).

---

## 2. Cluster taxonomy

The critical business-model distinctions that emerged:

| Axis | Poles |
|---|---|
| **What is sold** | Human labor (tasks) ←→ human judgment (expertise) ←→ software artifacts (environments/evals) ←→ software platforms (SaaS) |
| **Workforce** | Anonymous crowd ←→ credentialed expert network ←→ in-house FTE engineers |
| **Revenue shape** | Per-task/hourly (linear, thin margin) ←→ managed-service contracts ←→ one-time artifact sales ←→ recurring SaaS |
| **Customer set** | 5–10 frontier labs (huge deals, brutal concentration) ←→ thousands of enterprises (small deals, diversified) |
| **Defensibility** | Near-zero (commodity crowd) ←→ workforce quality/reputation ←→ artifact IP & tooling ←→ workflow lock-in |

### Cluster A — Premium expert human-data networks
*Sell credentialed human judgment (SME data, RLHF, rubrics, evals) to frontier labs. Managed-service or marketplace revenue. The current center of gravity.*

| Company | Key facts | Status |
|---|---|---|
| **Surge AI** (surgehq.ai) | Founded 2020 (Edwin Chen), SF. Bootstrapped & profitable from day one ✅; ~$1.2B revenue 2024 ✅ (Sacra/Forbes-corroborated); July 2025 talks for ~$1B raise at **$25B+** (a16z, Warburg, TPG; JPM among banks on secondary) ✅ ([Bloomberg](https://www.bloomberg.com/news/articles/2025-07-30/scale-rival-surge-ai-in-talks-for-funding-at-25-billion-value)). *Update (Jul 2026):* talks moved **up to ~$30B** (Forbes, Sep 2025) but **no authoritative confirmation the round ever closed** — Crunchbase still lists it as rumored; say "in talks," not "raised." Customers incl. Anthropic, Google, Microsoft, Meta ✅. Built a new internal RL-environments org 📰. | Deep profile |
| **Mercor** (mercor.com) | SF HQ. $350M Series C at **$10B** (Oct 2025, Felicis; Benchmark, General Catalyst) 📰 ([CNBC](https://www.cnbc.com/2025/10/27/ai-hiring-startup-mercor-funding.html)); ~$450M run-rate mid-2025 📰. Major producer of grading rubrics; "Prompt-Rubric Pairing" methodology 📰. Rubric work is **contractor/gig** (Rubric Academy Fellowship: $50–150 stipend, 3–5 hrs, funnel to Expert Contributor gigs) ✅; corporate FTE roles at SF HQ. Pitching domain-specific RL envs 📰. *Update (Jul 2026) — risk flags:* contractor model under legal challenge (Oct 2025 CA class action vs. Mercor+OpenAI for misclassification; ~30k-expert TX class action May–Jun 2026); **~4TB supply-chain data breach April 2026 — Meta paused work**; five breach lawsuits. | Deep profile |
| **Handshake AI** (joinhandshake.com) | AI-data arm of the career network, launched Jan 2025. $0→~$1B run rate ✅ — corroborated by The Information ($5M → $550M Jan 2026 → ~$1B Apr 2026; Sacra: ~$1.1B gross, +349% YoY). **Caveat: that's *gross* revenue; 60–70% passes through to contractors → net ≈ $300M** ✅. ~$60M/month to 30k+ contributors is arithmetically consistent ✅. Claims every frontier lab as customer 📰. Hires PM & program-ops FTEs in SF ✅: Sr PM Operator Experience ($180–220K), Manager Strategic Projects; SPL band $125–160K 📰. *Update (Jul 2026) — risk flags:* contractor pay disputes (Business Insider: withheld-pay allegations, two lawsuits; "Project HH" workers reporting 20–50% payouts); acquired Cleanlab (Jan 2026) and Uplimit (Jun 2026). | Deep profile |
| **Turing** (turing.com) | Palo Alto. $110M raise at **$2.2B** 📰 ([Forbes](https://www.forbes.com/sites/richardnieva/2025/09/03/ais-next-job-recruiting-people-to-train-more-ai/)). Talent network pivoted hard to frontier-lab data services; also builds UI-gym environments 📰 (SemiAnalysis). | Deep profile |
| **Invisible Technologies** | Last valued $500M (2023) 📰; go-to ops partner for OpenAI/Microsoft 📰 (Forbes). Managed "process" workforce, higher-touch than crowd. | Profile |
| **Micro1** | Expert/talent-network model grouped with Turing/Mercor 📰 (Lemon.io, HeroHunt). | Profile |
| **Snorkel AI** (snorkel.ai) | Redwood City; Stanford AI Lab spinout (2019). $100M Series D at **$1.3B** (May 2025, Addition; $237M total) ✅. Pivoted from programmatic labeling to **Snorkel Evaluate + Expert Data-as-a-Service** ✅. Anthropic a named partner (Head of Revenue endorsement) ✅; 7 of top-10 US banks, USAF ✅. | Deep profile |
| ◻ Aboda.ai | Named by SemiAnalysis alongside Surge/Mercor/Handshake as expert-hiring firms for labs. | Roster |
| ◻ Pareto.AI, Sepal AI, Datacurve | Smaller expert-data shops serving labs (coding/SME data). Verify before use. | Roster |

**Cluster A strategy read:** Highest growth and margins in the human-data economy;
defensibility = expert-workforce quality + lab trust. Two structural risks: (1) lab
insourcing (OpenAI explicitly) 📰, (2) the gig-workforce model means most "rubric
design" work is contractor-side — the FTE org is a thin layer of PM/ops/eng on top
(directly relevant to job seekers: the FTE jobs exist but are far scarcer than the
contributor jobs).

### Cluster B — Commodity-scale labeling & BPO workforces
*Sell managed labor per task/hour. Anonymous or lightly-credentialed crowds. Thin margins, zero switching costs.*

| Company | Key facts | Status |
|---|---|---|
| **Scale AI** (scale.com) | ~$29B post-Meta 📰; 14% layoffs in labeling core; refocusing hiring on enterprise + government (incl. Scale Labs / SEAL evals); ~394 open roles July 2026 📰. Client defections post-Meta 📰. | Deep profile |
| **Appen** | The cautionary tale: Google terminated an $82.8M contract (~26–30% of revenue) with ~2 months' notice 📰 ([Rest of World](https://restofworld.org/2024/exporter-google-appen-ai-search/)); H1 revenue −18.4% 📰. 20+ yr crowd across 170+ countries 📰. | Profile |
| ◻ Sama, iMerit, TELUS Digital (ex-Lionbridge AI), TaskUs, Cogito Tech, CloudFactory, LXT (Clickworker), Shaip, Defined.ai, Innodata, Centific, Welocalize, e2f, DataForce (TransPerfect), Toloka (+ Mindrift brand), Humans in the Loop | Managed-workforce/BPO labeling vendors; Cogito 5,500+ annotators, TaskUs 50+ countries 📰 (Lemon.io). | Roster |
| ◻ Contributor-facing brands: Outlier & Remotasks (Scale), Alignerr (Labelbox), DataAnnotation.tech (reportedly Surge-linked), Prolific (research-participant panels) | The gig-side front doors of the majors — relevant as market signal, not as FTE employers at brand level. | Roster |

**Cluster B strategy read:** Structurally declining/commoditizing 📰 (Appen contract
loss triggered by a $14.50/hr wage increase; Scale poaching clients on price). M&A
consolidation already happened (Appen–Figure Eight, TELUS–Lionbridge, LXT–Clickworker) 📰
(HeroHunt). **Avoid for career ROI** except Scale's enterprise/gov and evals (SEAL)
units, which are where Scale itself says it's hiring 📰.

### Cluster C — RL environments-as-product
*Sell interactive training environments (UI gyms, software replicas, task sims) as artifacts or platforms. The 2025–26 boom cluster.*

| Company | Key facts | Status |
|---|---|---|
| **Fleet** (fleetai.com) | Founded 2024. Talks (Apr 2026) for $50M+ at **~$750M** post (Bain Capital Ventures; Sequoia, Menlo, SV Angel) ✅ — traced to The Information's own reporting (Stephanie Palazzolo, Apr 13 2026) and corroborated by Sacra, not just aggregators ([The Information](https://www.theinformation.com/newsletters/ai-agenda/reinforcement-learning-gym-startup-buoyed-labs-appetite-training-data-reaches-750-million-valuation)). Revenue ~$1M → **$60M+** annualized ✅ (Sacra estimate concurs). *Update (Jul 2026):* round reportedly closed at **$45M / $725M** led by insiders (ARR Club — single mid-tier source, unconfirmed); run rate ~$63M, ~$160M projected next quarter 📰-weak. Builds RL gyms: Salesforce/Excel replicas ✅. CEO disputes "tiny team" characterization: >20 FTEs, majority of frontier labs as customers 📰. | Deep profile |
| **Mechanize** | Working with Anthropic (2 sources) 📰; ~$750M reported valuation 📰; ex-Epoch AI founders; offering **$500K salaries** to env-building SWEs 📰 (TechCrunch). SWE-task focus. | Deep profile |
| **Prime Intellect** | $15M led by Founders Fund + Menlo; angels incl. Karpathy, Delangue, Dylan Patel, Tri Dao ✅; total >$20M ✅ (Tracxn suggests ~$50M Series B Dec 2025 📰-weak). Business = compute marketplace + open RL stack + **Environments Hub** ("Hugging Face for RL environments") ✅/📰 — monetizes compute, not env sales to labs. | Deep profile |
| **Patronus AI** | Founded 2023, ex-Meta AI. **$50M Series B** June 2026 (Greenfield; Notable, Lightspeed, Datadog, Samsung; $70M total) 📰; revenue **up ~15x YoY**; "virtually every frontier lab" a customer 📰 ([TechCrunch](https://techcrunch.com/2026/06/25/patronus-ai-lands-50m-to-build-digital-worlds-that-stress-test-ai-agents/)). Pivoted evals → "digital world models" (SWE + finance, expanding to long-horizon). Evidence the evals and environments clusters are converging. | Deep profile |
| 📰 Habitat, DeepTune, Vmax, Preference Model, Bespoke Labs, Veris.ai | Named by SemiAnalysis as env builders; field of **35+ companies**, mostly seed-stage, <20 employees, 1–3 customers each 📰. | Profile-lite |
| ◻ Kaizen (via Infra Startups sector map), General Reasoning, Osmosis, Applied Compute, Halluminate, Plato, Runloop | Additional env/RL-services startups surfaced in sector maps or category knowledge — verify each. | Roster |
| **Unit economics datapoint** 📰 | UI-gym website clones sell ~**$20K per site, one-time**; OpenAI bought hundreds for ChatGPT Agent training (SemiAnalysis). One-time artifact sales — not recurring revenue. | — |

**Cluster C strategy read:** Explosive demand (Anthropic $1B+ discussion; Fleet 60x
revenue), but: mostly one-time artifact revenue, extreme customer concentration,
skeptical insiders 📰, and reward-hacking technical risk. Barbell outcome likely — one
or two "Scale for environments" winners plus a consolidation wave through the 35+
seed-stage field. Teams are eng-first; PM/ops roles are scarce until companies pass
~50 headcount.

### Cluster D — Evals, benchmarks & safety testing (as a service/org)

| Company/org | Key facts | Status |
|---|---|---|
| **Patronus AI** | See Cluster C — the flagship example *escaping* this cluster into environments. | — |
| ◻ LMSYS / LMArena | Community benchmark → company (reported ~$100M seed 2025, a16z-led — verify). | Roster |
| ◻ Epoch AI | Nonprofit research org; benchmarks + market analysis (its own RL-env FAQ cited here). Note: its researchers quitting to build post-training tooling was cited as an eval-cluster symptom 📰. | Roster |
| ◻ METR, Apollo Research, FAR AI | Independent safety-eval orgs — the one durable niche 📰 (Liao). | Roster |
| ◻ Haize Labs, Gray Swan AI, Lakera, Virtue AI, Pattern Labs, Irregular, Robust Intelligence (Cisco), Vals AI, LayerLens, Artificial Analysis | Red-teaming / security-eval / benchmark firms. | Roster |

**Cluster D strategy read — the bear case is structural** 📰 ([Thomas Liao](https://thomasliao.com/eval-startups)):
eval revenue is capped at the largest eval contract while post-training deals reach
$100Ms–$Bs; customers technical enough to buy evals can build them; labs
adversarially hill-climb public benchmarks; talent attrits to the model stack. As of
May 2025 no independent eval startup had succeeded outside the safety niche 📰.
**Career implication: avoid pure-eval startups; safety-eval orgs are mission-driven
(nonprofit comp); the winners pivot to environments (Patronus) or data (Snorkel).**

### Cluster E — Eval/observability SaaS platforms
*Recurring-revenue software for enterprises running LLM apps — a different buyer (enterprise eng teams) than Clusters A–D (labs).*

| Company | Notes | Status |
|---|---|---|
| **Braintrust** (braintrust.dev) | Series B raised; positioning: continuous production eval infrastructure 📰 (company blog). Likely PM hiring. | Profile |
| ◻ LangSmith (LangChain), Langfuse, Arize AI, Galileo, HoneyHive, Freeplay, Confident AI (DeepEval), Giskard, Comet (Opik), W&B Weave (CoreWeave), Maxim AI, Vellum | Observability/eval SaaS field; Humanloop reportedly wound down/acqui-hired 2025 (verify). | Roster |

**Strategy read:** Real SaaS economics and classic PM career ladders, but crowded and
being commoditized from two sides (open-source + hyperscaler bundling). Safer
employment, lower equity variance than Cluster A/C leaders.

### Cluster F — Labeling software platforms (SaaS tools)

| Company | Notes | Status |
|---|---|---|
| **Labelbox** | Structured SaaS platform for feedback collection/QA 📰 (Lemon.io); 2025 RLHF/multimodal expansion + Alignerr contributor network 📰. | Profile |
| ◻ Encord, V7, Superb AI, Kili, SuperAnnotate, Dataloop, HumanSignal (Label Studio), Roboflow, Voxel51, Argilla (Hugging Face) | Data-engine/annotation tooling; several pivoting toward eval/RLHF workflows. | Roster |

### Cluster G — Synthetic data & data curation

| Company | Notes | Status |
|---|---|---|
| ◻ Gretel | Reported NVIDIA acquisition (2025) — the cluster's exit template. | Roster |
| ◻ SynthLabs, Datology AI, Mostly AI, Tonic.ai, YData, Synthesis AI, Hazy (SAS), Rendered.ai, Parallel Domain, Applied Intuition (AV sim, adjacent) | Synthetic-data generators & curation; NVIDIA/hyperscaler acquisition interest is the strategic story. | Roster |

---

## 3. Job-fit and ROI analysis (FTE · PM/product-research/program-ops · SF OK)

**ROI frame = equity upside × survival probability × role availability for your profile.**

### Strongest fits

1. **Handshake AI — best overall probability-weighted fit, now with eyes open.**
   The only company with *verified, currently-open* SF FTE roles matching your
   exact profile: Manager, Strategic Projects (program-ops leading delivery of AI
   data/eval projects — explicitly does **not** require prior AI experience ✅) and
   Sr PM, Operator Experience ($180–220K 📰). Growth is now independently
   corroborated, not just self-claimed: The Information tracked $5M → $550M →
   ~$1B gross annualized (Jan 2025–Apr 2026) ✅. Two verified caveats to carry into
   interviews: (a) **net revenue ≈ $300M** after 60–70% contractor pass-through —
   value the equity on net economics, not the headline; (b) contractor
   **withheld-pay allegations and two lawsuits** (Business Insider) — an
   operational-integrity question that a program-ops candidate can legitimately
   (and impressively) ask about.

2. **Surge AI — highest-quality organization; different equity math.** Verified
   Strategic PM opening whose stated requirements (market research, competitive
   analysis, insight synthesis ✅) read like your resume. Profitable, bootstrapped ✅,
   revenue ~$1.2B (2024) ✅. Valuation context for negotiation: talks rose from
   $25B to **~$30B** (Forbes, Sep 2025) but the round has **never confirmably
   closed** ✅ — so there is no market-cleared price; probe equity terms and any
   secondary program hard. Application is an email case study to
   careers@surgehq.ai 📰 — a writing-forward process that favors you.

3. **Mercor — high equity beta, rubric-native culture; risk profile just got
   sharper.** $10B valuation, ~$450M run-rate 📰, SF HQ, and rubric design is
   literally the product ("Prompt-Rubric Pairing" ✅). Target the *corporate* roles
   (product, ops, delivery leadership) — rubric work itself is verified gig-side ✅.
   *New verified risks (Jul 2026):* a ~4TB supply-chain **data breach** (Meta
   paused work; five lawsuits) and **misclassification class actions** (CA, TX)
   attacking the contractor model itself ✅. Both cut two ways for you: real
   company risk, but also exactly the kind of trust/quality/ops rebuild that
   creates senior product-ops mandates. Ask directly about both.

   *(New option surfaced by verification:)* **OpenAI Human Data team — the
   insourcing side of the trade.** OpenAI is hiring **Program Manager, Human
   Data** and TPM/ops roles in SF for the very function it's pulling in-house
   (Feather platform) ✅. If the insourcing thesis plays out, the safest seat is
   inside the lab rather than at its vendors — at lab-tier compensation. Directly
   matches your program-ops + rubric/quality profile.

4. **Snorkel AI — the mature, benefits-of-a-pivot play.** Redwood City; freshly
   capitalized ($1.3B val ✅); the Expert Data-as-a-Service + Evaluate pivot ✅ needs
   exactly PM/program people who understand rubric-driven expert workflows.
   Lower equity ceiling than Surge/Mercor but a calmer risk profile and a
   named Anthropic relationship ✅.

5. **Patronus AI — the evals→environments rocket.** 15x revenue growth, every
   frontier lab a customer 📰, post-Series-B scaling is precisely when the first
   product/program hires happen. Higher variance than 1–4; monitor their job board.

### Conditional / monitor

- **Fleet** — spectacular growth (60x 📰) and pre-Series-A equity would be
  life-changing if it wins, but eng-first and small; PM/ops openings will be
  few and fought-over. Worth a direct approach given your product-research angle
  on environment quality/fidelity.
- **Scale AI** — largest absolute PM/ops headcount in the sector (~394 openings 📰)
  and the enterprise/gov/evals units are the stated hiring focus 📰, but equity
  upside is largely spent and post-Meta client attrition is unresolved.
- **Turing, Invisible** — solid mid-tier options; less public hiring signal in this
  pass; check boards directly.
- **Braintrust / eval-SaaS cluster** — classic PM ladders, moderate upside, safer.

### Avoid (for this profile)

- **Commodity labeling/BPO (Cluster B)** — structurally declining 📰; program-ops
  roles exist but ride shrinking margins and contract-loss shocks (Appen precedent 📰).
- **Standalone eval startups (Cluster D, non-safety)** — capped revenue, talent
  attrition, adversarial customers 📰; join one only if it's actively pivoting
  (i.e., becoming Cluster A or C).
- **Sub-20-person RL-env seed startups** *for PM roles specifically* — eng-only
  cultures with 1–3 customers 📰; revisit each at Series A+.

### Where your rubric-design strength is worth the most

The market is telling you rubric/taxonomy skill is monetized in three tiers:
gig (Mercor fellowship, $50–150 📰) → FTE program-ops that *runs* rubric pipelines
(Handshake, Snorkel, Surge — $125–220K bands 📰) → product leadership over
evaluation platforms (Surge Strategic PM, Patronus, Snorkel Evaluate). Aim at
tiers 2–3; use tier-1 artifacts (your own published rubrics) as portfolio proof.

---

## 4. Meta-sources for extending this inventory

- SemiAnalysis, "RL Environments and RL for Science" — the "data foundries" framing + env-vendor roster 📰
- TechCrunch, "Silicon Valley bets big on 'environments'" (Sep 2025) — the defining cluster-C survey 📰
- Epoch AI, "An FAQ on RL Environments" — independent market-structure analysis 📰
- Thomas Liao, "Why are there so few independent eval startups?" — the eval bear case 📰
- Sapphire Ventures, "Reinforcement Learning: Learning by Doing" market map (Apr 2026) 📰
- NGP Capital, "Evals Are the New Moat" (Oct 2025) 📰
- Paweł Huryn, "Ultimate Guide to AI Observability & Evaluation Platforms" (Sep 2025) 📰
- HeroHunt "Top 10 Human Data Providers 2026" + "Ultimate AI Data Labeling Industry Overview" (vendor-adjacent; cross-check) 📰
- github.com/joylarkin/Awesome-AI-Market-Maps — 500+ curated market maps 📰

## 5. Caveats

- **Verification coverage.** First pass: 15 claims verified 3–0 (Snorkel, Prime
  Intellect, Surge careers, Handshake careers facts). Targeted second pass: the 6
  decision-driving claims (OpenAI insourcing, Surge valuation/financials, Mercor
  gig-rubric structure, Anthropic $1B envs, Fleet financials, Handshake run rate)
  each confirmed 3–0 by independent skeptic agents with primary-source,
  contradiction, and freshness lenses — 18/18 votes, zero refutations. Remaining
  📰 claims (Mechanize, Patronus, Scale/Appen event details, market-size
  projections, Turing/Invisible figures) carry citations but no formal pass.
- **Gross vs. net.** Handshake's ~$1B and similar expert-network "run rates" are
  gross bookings including 60–70% contractor pass-through; net revenue is ~⅓ the
  headline. Apply the same haircut mentally to Surge/Mercor figures.
- **Freshness.** Valuations/fundraises move monthly. As of July 2026: Surge's
  round (talks at ~$30B) has never confirmably closed; Fleet's reportedly closed
  at $45M/$725M per a single mid-tier source. Recheck before decisions.
- **◻ Roster entries** come from sector maps or category knowledge and were not
  verified this pass — several may have pivoted, been acquired, or shut down.
- **Fetch blocks.** mercor.com and several pages 403'd behind the proxy; those
  quotes come from search-index snippets of the same URLs.
