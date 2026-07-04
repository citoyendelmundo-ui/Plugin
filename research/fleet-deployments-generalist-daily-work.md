# Fleet Deployments Generalist — What the Daily Work Actually Looks Like

> Built from the real job description (uploaded 2026-07-02) + Fleet's **actual
> public GitHub artifacts** (github.com/fleet-ai), fetched and verified for this
> doc. The four worked examples are reconstructed from Fleet's own published
> environments (EnterpriseOps-Gym, gym-anything, mcp-bench, harbor-train) and the
> RL/rubric research corpus from earlier in this project — so the *mechanics,
> numbers, and artifacts are verified*, while the exact hour-by-hour choreography
> is a faithful reconstruction, clearly marked where it is.

---

## Part 1 — The real shape of the role (from the JD)

The posting resolves the ambiguity from my earlier inference. Cleaned up, "In
your role you will":

1. **Perform failure analyses** — find what models are bad at, then drive work to
   close the gap. *"genuine intuition for what pushes models further — not just
   project-manage around the edges."*
2. **Improve environment & seed-data quality** — test, iterate, raise the bar on
   what ships.
3. **Propose practical research directions** from patterns across environments,
   customer needs, and model behavior.
4. **Wrangle the expert contractor workforce as a systems problem** — tooling,
   specs, quality frameworks; *not* brute-force coordination.
5. **Talk to customers directly** — understand data needs, report eval-run
   observations, build trust through delivery quality.
6. **Look at data with a critical eye** — define "good," spot quality issues.
7. **Build operational systems that scale** delivery.

**The three anti-patterns they explicitly reject** (this is the real signal):
- The PM "who coordinates but doesn't do the technical work — dig into the data,
  find the issue, and **fix it**, not just file a ticket."
- Treating expert wrangling as brute force ("more people = more output") instead
  of "AI-first systems: better tooling, clearer specs, smarter allocation."
- No strong opinions on data/environment quality — *"you should look at an
  environment and have a hypothesis on whether it's going to be useful for
  training."*

**How the week actually feels** (their words): *"this role is whatever it needs
to be, some weeks that's failure analysis, some weeks it's customer calls, some
weeks it's building an internal tool."* Plus a values tell that matters for the
day-to-day: *"a single detail in an environment can be the reason for
unintentional failures within major training runs… we don't cut corners; we cut
scope."* — meticulous, high-stakes QA is the emotional core of the job.

### The verified toolbox you'd work in (Fleet's real repos)

| Repo | What it is | You'd touch it for |
|---|---|---|
| **EnterpriseOps-Gym** | ServiceNow env: **1,150 expert-curated tasks**, 8 domains (Calendar, CSM, Drive, Email, HR, ITSM, Teams, Hybrid), 512 tools, **SQL verifiers checking final state**, ~5.3 conditions/task, best model only **34.1%** | Failure analysis, verifier QA, customer evals |
| **gym-anything** | "Turn any Software into an Agent Environment." 3 parts: Core runtime, Benchmarks (`cua_world`), Agents. A task = **description + setup script + automatic checker** | Building/QA'ing new environments |
| **mcp-bench** | Benchmarks tool-use agents over 28 MCP servers; JSON tasks; scored on rule-based schema + **LLM-judge (o4-mini)** task completion + tool use + planning (0–1) | Eval runs, judge-quality auditing |
| **harbor-train** | GRPO training loop (SkyRL + SkyPilot) that **consumes** your environments as RL training signal | Understanding downstream impact of env quality |
| **zeroboot** | Sub-millisecond VM sandboxes (Rust) — the infra that runs thousands of rollouts | Ops systems that scale delivery |
| **researcher-scrape** | Nightly arXiv scraper for RL/post-training/world-model researchers | Proposing research directions (it's literally tooled) |

---

## Part 2 — Four verified, step-by-step worked examples

Each maps to JD responsibilities and to one of your strengths (rubric design,
qualitative research, customer discovery, ops).

---

### Example A — Failure analysis on a ServiceNow ITSM agent
**JD map:** #1 failure analysis · #3 research directions · #6 critical eye
**Verified anchor:** EnterpriseOps-Gym — best model scores **34.1%** success;
tasks average 9.15 steps, verified by SQL checks on final DB state.

**The situation (real):** A frontier-lab customer is training an agent to operate
enterprise IT-service-management workflows. On Fleet's ServiceNow environment,
even the best model completes only ~34% of tasks. The lab doesn't just want a
number — they want to know *which capability to train next*. That diagnosis is
your job.

**Step by step:**

1. **Run the eval and pull the transcripts.** Launch the ITSM task suite (a slice
   of the 1,150) through the harness; each run produces an action trace + the
   final SQL-verifier results (which of the ~5.3 conditions per task passed).
   *This is data collection, not yet analysis.*

2. **Bucket the failures — the qualitative-research move.** Read losing
   transcripts and open-code them the way you'd code customer interviews. You're
   looking for *recurring failure modes*, not one-offs: e.g. "agent resolves the
   incident but never links it to the parent problem record" (a foreign-key
   relationship — recall the env has 1.7 FK deps/table), or "agent stops after
   the visible UI action and misses the required state change 3 tables deep."

3. **Separate capability gaps from environment artifacts.** Critical
   discrimination: is the model *bad at multi-hop state changes*, or is the task's
   verifier checking something the instructions never told the agent to do? The
   first is a training signal (valuable); the second is an environment bug (also
   valuable — feeds Example B). You cannot tell without reading the verifier
   conditions against the transcript.

4. **Quantify the pattern.** "62% of ITSM failures share one root cause:
   the agent doesn't propagate a status change to dependent records." Now it's a
   targeted finding, not a vibe. *This is the "genuine intuition for what pushes
   models further" the JD demands — expressed as evidence.*

5. **Drive the fix.** Propose the seed data / new tasks that isolate and drill
   that skill: a set of tasks whose *only* difficulty is correct multi-hop state
   propagation, with verifiers that check exactly those FK relationships. That
   set becomes RL training signal via harbor-train.

6. **Report up and out.** One-paragraph observation to the customer ("your model's
   ITSM gap is cross-record state propagation, not tool selection; here's the
   evidence and the environment we're building to close it") — which is
   simultaneously Example D.

**Why you'd be good at it:** Steps 2 and 4 *are* qualitative research —
open-coding a corpus, finding the latent theme, quantifying it. Most engineering
candidates skip straight to step 5 and guess.

---

### Example B — Auditing whether an environment's reward is real or hackable
**JD map:** #2 environment quality · #6 critical eye · the "cut scope not corners" value
**Verified anchor:** EnterpriseOps-Gym verifiers check **final environment state,
not action sequences**, with ~5.3 conditions per task; gym-anything tasks ship a
"description + setup script + automatic checker."

**The situation (real):** Before an environment ships into a lab's training run, a
single bad verifier can teach the model the wrong thing — the JD's "single detail…
reason for unintentional failures within major training runs." Reward hacking is
*the* known failure mode of RL environments (it's the bear case insiders cite).
Your job is to break the reward before the model does.

**Step by step:**

1. **Read the task as an adversary.** Take a CSM task: "escalate the customer's
   billing complaint and notify the account owner." Look at its ~5 SQL verifier
   conditions. Ask the rubric-designer's question: *what is the cheapest way to
   satisfy every condition without doing the task correctly?*

2. **Hunt for the gap between "checked" and "intended."** Because verifiers check
   *final state*, a classic hole: the checker confirms a notification row exists
   and a status = "escalated", but **not** that the notification is linked to the
   right account owner. An agent that notifies *everyone* passes. That's a
   reward-hackable spec — high verifier-pass-rate, zero real capability.

3. **Prove it empirically.** Write (or prompt an agent to write) a degenerate
   solution that games the checker — the brute-force notify-all. Run it. If it
   passes, you've verified the hole, not just theorized it. *This is the JD's
   "dig in and fix it, not file a ticket" in its purest form.*

4. **Tighten the criterion.** Add the missing condition: notification.recipient =
   the specific account owner FK. Re-run the degenerate solution — it should now
   fail — and re-run a known-good trajectory — it should still pass. You've
   closed the gap without breaking legitimate solutions. (This two-sided check —
   *false-positive AND false-negative* — is exactly HealthBench-style judge
   validation applied to a SQL verifier.)

5. **Decide scope vs. corner.** Maybe fully verifying "the account owner was
   *appropriately* notified" is genuinely hard (tone, timing). The value says cut
   *scope* (ship a narrower task that's fully verifiable) not *corners* (ship the
   broad task with a leaky checker). Documenting that call is part of the craft.

6. **Generalize it (Example C hook).** If this hole appears once, it appears
   across the contractor-authored task bank. Now it's a systems problem: a lint
   rule / automated adversarial check that flags "verifier checks existence but
   not relationship" across all tasks.

**Why you'd be good at it:** This is literally rubric design — decompose the
intended outcome into verifiable criteria, then adversarially test the rubric for
gameability and validate it against known-good and known-bad cases. You have a
documented corpus on exactly this (RaR weighting, HealthBench judge validation,
RRD failure modes). Almost no generalist candidate can do step 4 credibly.

---

### Example C — Turning expert-contractor wrangling into a systems problem
**JD map:** #4 workforce-as-systems · #7 operational systems · #2 quality
**Verified anchor:** gym-anything's task contract (description + setup script +
checker) is the unit contractors produce; Fleet explicitly frames the workforce
as a tooling/spec problem, not headcount.

**The situation (real):** A lab orders a new environment class — say, 300 tasks
over a CRM app. Experts (ex-CRM admins) author tasks and verifiers. The
brute-force path is a coordinator chasing 300 Google-sheet rows. The JD
*explicitly rejects that person.* The systems path:

**Step by step:**

1. **Author the spec, not the tasks.** Write the task-authoring standard: what a
   good task description contains, the required setup-script shape, and — hardest
   — how to write a **final-state verifier with no gap between checked and
   intended** (the Example B lesson, encoded as a rule the workforce follows).
   One clear spec replaces a hundred one-off corrections.

2. **Build the QA gate as code.** A submitted task shouldn't reach a human
   reviewer until it passes automated checks: (a) schema valid, (b) setup script
   runs in a zeroboot sandbox, (c) a known-good solution passes all verifier
   conditions, (d) — the clever one — a *degenerate agent* that tries trivial
   shortcuts does **not** pass. Gate (d) catches reward-hackable verifiers
   automatically, at authoring time, across the whole workforce.

3. **Instrument quality.** Track per-contractor verifier-pass-rate-on-degenerate
   (leakiness), rework rate, and reviewer overrides. Now allocation is
   data-driven: route the multi-hop HR tasks to the three authors whose verifiers
   never leak, not to whoever's free.

4. **Close the loop.** Feed reviewer rejections back into the spec and the
   automated gate so the same class of error can't recur. The system gets tighter
   without adding coordinators — "smarter allocation, tighter feedback loops," in
   the JD's words.

5. **Measure the win in throughput-per-reviewer-hour,** not tasks-shipped. That's
   the metric that proves you solved a systems problem instead of grinding one.

**Why you'd be good at it:** This is product-ops / program design — turning a
messy human process into tooling + specs + metrics. Your ops-management
background is the direct fit; the twist Fleet wants is that the "product" you're
managing is a data-quality pipeline, and you can reason about the quality bar
technically (Examples A/B) rather than delegating it.

---

### Example D — A customer eval-run report for a frontier lab
**JD map:** #5 talk to customers · #1 failure analysis · #6 critical eye
**Verified anchor:** mcp-bench scores agents 0–1 across rule-based schema
understanding + LLM-judged (o4-mini) task completion + tool use + planning; GPT-5
scored 0.749. This is the report format Fleet already produces.

**The situation (real):** A lab is deciding whether their new model is ready to
ship as a tool-using agent. They ask Fleet to evaluate it. The deliverable is an
observation report that builds trust — the JD's "report observations from
evaluation runs… build trust through the quality of what you deliver. Clarity of
thought is a must-have."

**Step by step:**

1. **Translate the customer's question into an eval spec.** "Is our model good at
   multi-tool workflows?" → run mcp-bench's two- and three-server tasks (multi-tool
   coordination), plus a relevant gym-anything slice. *This is customer discovery:
   turning a vague need into a measurable one.*

2. **Run it and disaggregate the score.** Don't report "0.71." Report the
   sub-dimensions: schema understanding 0.9 (fine), planning 0.55 (weak). The
   headline number hides the actionable finding.

3. **Read behind the number — audit your own judge.** Since task-completion is
   LLM-judged (o4-mini), spot-check that the judge is right: sample cases it
   marked complete and confirm they actually are. If the judge is lenient, your
   report is wrong — and a lab will catch it, destroying trust. *Reporting a
   number you haven't validated is the fastest way to lose a frontier customer.*

4. **Write the observation, not just the dashboard.** "Your model plans poorly
   when a task needs 3+ tools in sequence — it picks correct tools but wrong
   order. On single-tool tasks it's at parity with GPT-5. Recommend training
   signal on multi-step planning; we can build that environment." Concrete,
   honest, and it opens the next engagement.

5. **Bring an observation they didn't ask for.** The value "deliver value beyond
   what is contracted" — e.g. "we also noticed your model silently retries failed
   tool calls without backoff, which will hammer production APIs." That
   unrequested, sharp observation is what turns a vendor into a partner.

**Why you'd be good at it:** Steps 1, 4, and 5 are customer discovery + crisp
written synthesis — your B2B research and writing background. Step 3 is the
quality-skeptic instinct (validate the judge before you trust it) that your rubric
work trained.

---

## Part 3 — How to use this in the interview

- **Speak in their nouns.** "final-state SQL verifiers," "reward hacking,"
  "verifier pass rate vs. success rate," "seed data," "failure buckets," "GRPO
  training signal." You now have them from their own repos.
- **Lead with Example B.** If they ask "how would you assess an environment's
  quality?", the adversarial-verifier audit (find the gap, prove it with a
  degenerate solution, tighten without breaking good trajectories) is the single
  most differentiating answer you can give, and it's your genuine strength.
- **Have one crisp opinion ready.** They *require* "a hypothesis on whether an
  environment is going to be useful for training." Pick one — e.g. "an
  environment whose verifier checks existence but not relationships will produce a
  model that games rather than learns" — and defend it.
- **Name the anti-pattern and disown it.** "I know the failure mode here is the PM
  who files tickets instead of fixing data — the reason I'm a fit is I can read
  the transcript, find the leaky verifier, and rewrite it myself."
- **Diligence you still owe yourself** (unchanged from the brief): confirm the
  round/valuation, headcount + how early you'd be in the non-eng org, customer
  concentration, and the equity terms behind "highly competitive."

### The honest line on "verified"
Verified from primary artifacts: every repo, mechanic, number, and quote in Parts
1–2 (Fleet's public GitHub, fetched 2026-07-02). Reconstructed (faithful but not
from Fleet's internal playbook): the exact ordering of steps within each example —
these are how this work is done in practice given the tools, not a leaked SOP. In
the interview, present them as "here's how I'd approach it," not "here's how you
do it."
