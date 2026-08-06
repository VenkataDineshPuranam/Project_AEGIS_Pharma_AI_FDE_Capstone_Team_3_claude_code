---
name: process-and-lean-discovery
description: >-
  Applies Lean/DMAIC as an operating spine: thin dmaic_lens.md on every stage,
  stage-09 lens_rollup + full waste registers, structural_reopen gate before
  tasks, Measure-first under scarce data, CTQ/RCA/future state. Use when the
  user asks about DMAIC, Lean, waste, Measure-first, or structural reopen.
---

# Process & Lean Discovery

Portable skill for any repo. Synced to `prompts_v2` Lean/DMAIC spine.

## Core thesis

Find and measure waste **before** automating with AI. Many “AI problems” are intake, waiting, handoffs, or controls — prove that with numbers.

**Scarce-data rule:** if Discovery baselines are Missing/Partial or narrative class is `hypothesis`, DMAIC is **Measure-first** — instrumentation, sampling, and evidence acquisition outrank new AI features. Do not schedule agent/retrieval scale-out ahead of Measure capability.

## Thin lens contract (every stage except 09)

Each stage 01–08 and 10–13 writes a short `dmaic_lens.md` in that stage’s `participant-outputs-v2/NN-*/` folder. Do **not** run a full Lean workshop except at stage 09.

| Stages | Lens focus |
|---|---|
| 01 | Measure + light Define |
| 02–03 | Define (+ Measure targets) |
| 04–05 | Analyze |
| 06–08 | Improve-by-design + Control triggers |
| 10–11 | Improve (prioritize / execute) |
| 12 | Control (plus `control_lens_rollup`) |
| 13 | Control (executive) |

## Stage 09 — full consolidation

**Prerequisites:** lenses 01–08 available (or gaps noted); architecture review `pass`/`conditional`; feature ACs + contracts; early waste from Discovery.

### 0. Lens roll-up (required first)

Create `lens_rollup.md`:

- Table of prior `dmaic_lens.md` paths (01–08) with DMAIC focus and top findings  
- Merged list of wastes already named (dedupe)  
- Gaps where a prior lens was missing or shallow  

Do **not** restart from a blank page — consolidate prior lenses.

### A–D. Full DMAIC + waste registers

Then deepen into full DMAIC plan, DOWNTIME register, AI-specific waste register, and build constraints (below).

### E. Structural reopen gate (required)

If Improve needs changes to **C4, ADRs, or technical contracts**, do not proceed silently to tasks.

Produce `structural_reopen.md`:

1. Reopen required? `yes` | `no`  
2. If yes: which of 06 / 07 / 08 to re-run  
3. Status flip — ADRs `proposed`/`superseded`; review may return to `conditional`  
4. Gate: `blocked` | **`cleared`**  

**Prompt 10 / task entry requires `cleared`.** Do not hand off while `blocked`.

### Stage 09 outputs

`participant-outputs-v2/09-lean-dmaic/`:

- `lens_rollup.md`  
- `dmaic_plan.md`  
- `waste_register_downtime.md`  
- `waste_register_ai_specific.md`  
- `build_constraints_from_lean.md`  
- `structural_reopen.md`  

## DMAIC spine

| Phase | Job |
|---|---|
| **Define** | Problem/goal/scope/stakeholders/CTQ — without assuming an AI answer |
| **Measure** | Baseline metrics with formulas + sources (or open measurement) |
| **Analyse** | Root causes vs symptoms (Pareto, fishbone, 5 Whys) |
| **Improve** | Risk-tiered future state; non-AI fixes first where evidence says so |
| **Control** | How gains stick (gates, dashboards, review policy) — closed in Assurance via `control_lens_rollup` |

### Measure set to cover (charter)

End-to-end lead time · touch vs wait · first-pass yield · rework · handoffs · false-positive/quality · human-review effort · AI groundedness/citation rate · **cost per successful decision** — segment where needed (product, region, language, risk tier).

State the **definition and formula** for each metric. Define **first-pass yield** and **cost per evidence-complete
decision** precisely for the use case at hand — they are the two most often quoted loosely. Every baseline number cites
its source; a number that cannot be computed from the data is recorded as an **open measurement**, not estimated.

Include a **CTQ tree**: customer needs → drivers → measurable requirements → targets. Without the tree, the metric set is
a list rather than an argument.

## Traditional waste — DOWNTIME register

For each: where (current and/or proposed) · **observed vs hypothesized** · magnitude · impact · VA / business-required NVA / pure waste · eliminate/simplify action:

**D**efects · **O**verproduction · **W**aiting · **N**on-utilised talent · **T**ransportation · **I**nventory · **M**otion · **E**xtra processing  

Finish with Pareto of dominant lead-time waste.

## AI-specific waste register

One row per category: waste type · where/how it appears · evidence (trace file/field) · magnitude (tokens, retries, cost,
latency) · impact · **recommended treatment**.

| Waste | What it looks like |
|---|---|
| **Token** | Oversized prompts/context, redundant tokens |
| **Retrieval** | Obsolete, duplicated or low-relevance chunks |
| **Model** | Over-tiered models, or calls a rule/validation could replace |
| **Human-review** | Output always reviewed, adding cost without changing decisions |
| **Evaluation** | Missing or wasted eval effort; ungrounded/uncited outputs |
| **Integration** | Fragile tool chains, retries, failed tool calls |
| **Context** | Leakage, missing context, re-fetching |
| **Observability** | Cannot distinguish failure types — data vs retrieval vs model vs process |

Call out **overproduction of AI outputs**: a summary or recommendation was generated and no business action followed —
cite the trace field. Finish with the evidence that would show model accuracy **is or is not** the dominant bottleneck.

## Root cause analysis

1. **Pareto** — which few causes drive most of the delay/defects/cost, with the numbers.  
2. **Fishbone across eight branches** — process · people · source documents/inputs · reference/master data · retrieval ·
   model behaviour · integration · control design. Naming the branches is what stops every cause landing under "model".  
3. **5 Whys** on the top two or three issues, each traced to a root cause.  
4. **Root-cause register** — cause · category · evidence · symptom produced · whether it is a **process / data / model /
   control** cause · **candidate treatment class**.

### Treatment classes — the bridge from Analyse to Improve

Standardisation · deterministic validation · entity/master-data resolution · risk-tiered review · evidence packaging ·
constrained (grounded) AI · selective tool use.

Explicitly test the hypothesis: **is model accuracy the dominant root cause, or is it intake quality, waiting, handoffs or
controls?** State what the evidence shows, and which causes are **not** AI-solvable.

## Future state

1. **Options compared** — per root cause, the candidate treatment and its trade-off; show which are non-AI fixes and
   should come first.  
2. **Future-state process map** — deterministic checks and rules on low-risk paths; human specialists reserved for
   genuine exceptions.  
3. **Risk-tiering / triage policy** — how cases route by risk, and the human-review policy per tier.  
4. **Where AI is applied — and where it is not.** For each touchpoint: the capability, whether AI may
   **recommend / execute / must stay human**, the grounding and citation requirement, and the fallback.  
5. **Expected impact** — projected movement of each baseline metric, with assumptions stated.

Do **not** recommend an autonomous agent unless the evidence demands it — and if you don't, say why.

## Build constraints from Lean (handoff to tasks)

Classify for implementation:

- **must-fix-before-build**  
- **fix-in-pilot**  
- **accept-as-residual-risk**  

Task order should prioritize assumption tests, waste removal, and Measure instrumentation when Measure-first applies.

## Handing the findings upward

This skill supplies the **evidence** — baseline, waste Pareto, root cause — that a recommendation stands on.
For the decision-ready framing (answer-first, executive lenses), hand off to `exec-communication`.
Control owners and revisit triggers feed Assurance in `delivery-ops-llmops`.

## Workflow

1. Ensure thin `dmaic_lens.md` exists for stages 01–08 (or note gaps).  
2. Build `lens_rollup.md` first — do not ignore prior lenses.  
3. Map process; classify DOWNTIME + AI waste with observed vs hypothesized.  
4. Write DMAIC charter + baselines (or open measurements); Measure-first under scarcity.  
5. Root-cause; design future state; emit build constraints.  
6. Produce `structural_reopen.md` with gate **`cleared`** before tasks.  
7. Hand Control close to Assurance (`control_lens_rollup` at stage 12).

## Do / Don’t

- **Do:** quantify wait vs touch; Pareto wastes; constrain AI touchpoints; Measure-first under scarcity; consolidate lenses before the full workshop; clear structural reopen before tasks  
- **Don’t:** AI-wash a broken process; skip measurement; invent baselines; scale agents before Measure capability; re-run full stage 09 after every earlier step; ignore prior `dmaic_lens.md`; hand off to tasks while reopen is `blocked`  
