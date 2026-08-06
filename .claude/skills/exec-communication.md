---
name: exec-communication
description: >-
  Applies executive-communication craft: Minto/SCQA for decision-ready or
  hypothesis narratives, solution-proposal synthesis, agentic-pod operating model,
  workflow-redesign value framing, executive lenses (Board/COO/CIO/CFO), and the
  30/60/90 mandate. Use when the user asks about boardroom briefings, proposals,
  steering-committee decks, framing AI value, or agentic pods.
---

# Executive Communication

Portable skill for any repo. Merges boardroom craft with engagement Framing (02) and Proposal (13).

## Thesis

Technical correctness does not survive a boardroom on its own. The FDE's job in the room is to convert evidence into a
**decision**, at the altitude the audience actually owns.

## Answer first — Minto + SCQA (stage 02 Frame)

Respect Discovery framing mode:

| Mode | Answer form |
|---|---|
| `decision-ready` | Capability-level recommendation (no vendor/C4 lock-in) |
| `hypothesis` | Recommended **experiment** — what to test, falsifiers, evidence to acquire |

- Lead with the **answer**, then support it. Never narrate the investigation chronologically.  
- State narrative class + evidence boundary + blocking acquisition items at the top.  
- **S**ituation → **C**omplication → **Q**uestion → **A**nswer, with the Question as one bounded decision.  
- Group supporting points MECE at each level.  
- Every claim is cited, or labelled **Assumption**. Numbers carry their formula and source.  
- State explicitly what is **not** being asked for and what is **out of scope**.  
**Framing handoff pack:** decision question for PRD/DDD · success metrics for DMAIC Measure/Control · open questions blocking design · whether later artifacts must be **provisional**.

**`dmaic_lens.md` (Define):** waste in Complication; Measure targets known vs Unknown; what must not be automated yet; how Answer reduces waste.

Output: `participant-outputs-v2/02-scqa/` (`scqa_minto_decision_narrative.md`, `dmaic_lens.md`).

## The value frame: workflow redesign, not tool adoption

**AI maturity starts when workflow redesign begins.** Adoption metrics (seats, usage, PRs) show the threshold has been
crossed; they do not show advantage. Advantage appears only when work is rebuilt around agents.

- **The workflow, not the task, is the unit of automation.** The biggest wins remove handoffs, approvals, rework, tool
  switching and vendor dependence — not just make one step faster.
- Report **elapsed-time collapse on real, messy, multi-system work**, and note that elapsed time *understates* the value
  when approvals and vendor spend also disappear.
- **Discovery is the bottleneck**, not model quality. Process diagrams capture the nominal path; shadowing reveals the
  exception path and the real decision logic. The best opportunities sit beside the operator, not inside the documentation.
- **Model routing is a margin lever** — winners route complexity, token cost, and risk better, not merely use more agents.

## The agentic-pod operating model (≈10 days)

| Days | Step | Purpose |
|---|---|---|
| 1–2 | **Shadow the operator** | Observe each step; surface tacit decisions; document exceptions |
| 3 | **Prioritize the workflow** | Rank by scale, repetition, business impact |
| 4–5 | **Build with the expert** | Create alongside the practitioner for minutes-fast feedback |
| 6–9 | **Test for generalization** | Validate across multiple practitioners, not one hero workflow |
| 10 | **Ship and measure** | Operational proof while context and attention are fresh |

Why it beats a top-down rollout: it captures tacit knowledge that SOPs and vendor demos miss, produces working proof before
the change-management machinery starts, and ties value to a **named workflow owner** rather than an innovation budget.

**Generalization is the real quality gate — if several practitioners cannot use it, it is still a pilot.**

Pairing matters: one AI-native engineer with one domain-native expert forms a bilingual cell that collapses translation
loss. The pod, not the platform intake queue, is the minimum viable transformation unit.

## Blueprint — six moves

**Embed** → **Diagnose** (workflow, exception paths, handoffs, data dependencies, economics — before tooling) → **Route**
(small models for repetitive operations, frontier reasoning for judgment) → **Govern** (token cost, context reuse, approval
boundaries, risk classification from the start) → **Validate** (several practitioners) → **Scale** (reusable playbooks,
prompts, connectors, model–task maps).

The winning internal team is not a generic centre of excellence — it is a portfolio of embedded strike teams with codified reuse.

## Executive lenses — same model, four readings

| Audience | Frame | Their first priority |
|---|---|---|
| **Board** | An operating-model investment, not a software experiment | Fund the capability with portfolio accountability |
| **COO** | Remove friction from operational decision loops | Pick workflows where time-to-decision damages service or growth |
| **CIO / CTO** | Orchestration discipline, not just model access | Build a model–task map across support, research, coding, ops, docs |
| **CFO** | Value measured at **workflow P&L** level, not tool licences | Baseline economics *before* each pod sprint starts |

Prepare answers to the questions they will actually ask: which workflows carry the highest hidden friction and decision
latency; where are we funding experimentation without workflow proof; what portfolio metrics show wins generalize.

## The 30/60/90 mandate

- **Days 0–30** — select 3–5 workflows with scale, repetition and decision impact; assign AI-native builders and named
  domain experts; define baseline cycle time, handoffs, error rate, cost-to-serve.  
- **Days 31–60** — run pod sprints; create the model–task map and token-economics dashboard; capture reusable prompts,
  connectors and controls.  
- **Days 61–90** — expand only what generalizes across operators; rationalize the tooling the new workflow makes obsolete;
  stand up a durable team with portfolio ownership.

**Risks to name out loud:** scaling pilots without routing discipline or token controls; automating tasks without
redesigning approvals and handoffs; centralizing AI away from the operator and losing discovery fidelity.

## Final Solution Proposal (stage 13)

Synthesize the engagement for sponsors. Under hypothesis / provisional / scarce-data: lead with **what is unknown**, the **evidence acquisition plan**, and **sponsor data-access decisions**.

Include: evidence confidence · compressed SCQA · governing answer · PRD scope · operating workflow (HITL) · measurable outcomes · domain ownership · feature/AC summary · C4 (mark provisional) · key ADRs · contract highlights · safety/privacy/governance · data/integration · **Lean spine summary** (top wastes removed vs still open from Prompt 09 + **`control_lens_rollup` / 12**; Measure Unknowns sponsors unlock; Control owners from **`production_readiness.md`**; next DMAIC loop; **pilot learnings from 11**) · adoption model · phased roadmap · delivery assumptions · residual risks · **sponsor decisions required** · **DDD stage 16 handover** (owners and production blockers from Prompt 12).

Labels: Demonstrated in PoC vs Required for production · Known / Assumed / Unknown · artifact appendix index.

Also write thin `dmaic_lens.md` (executive Control story) under `participant-outputs-v2/13-proposal/`.

Output: `participant-outputs-v2/13-proposal/solution_proposal.md` (+ `dmaic_lens.md`).

## Workflow

1. Identify the decision and who owns it; write the Question before the deck.  
2. Declare narrative class; lead with the answer; structure support as a pyramid; complete handoff pack + Frame `dmaic_lens`.  
3. Frame value at workflow level with a measured baseline and an after number.  
4. Translate into the specific lens of the audience in the room.  
5. After Assurance, synthesize the proposal using `control_lens_rollup`, `production_readiness`, and `pilot_learnings`; close with a dated, owned ask.

## Do / Don’t

- **Do:** answer first; quantify against a baseline; name the workflow owner; state assumptions and revisit triggers; lead with unknowns under scarcity; include Lean spine close and DDD stage 16 handover  
- **Don’t:** narrate the journey; present adoption metrics as value; present hypothesis as a committed production decision; demo without a generalization result; ask for approval without naming the decision, the date, and the owner  
