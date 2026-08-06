# Prompt 02 — SCQA & Minto Pyramid (Frame)

**Lifecycle stage:** Frame  
**Framework derived:** SCQA + Minto Pyramid Principle (including MECE)  
**Core question:** Why does this matter, and what is the ask?  
**Prerequisites:** Prompt 01 evidence register (with framing mode and sufficiency scores).  
**Primary output type:** Decision narrative or hypothesis narrative (pyramid-structured).

---

## Intent

Derive the **framing framework**: turn discovery evidence into a clear, audience-ready narrative. Lead with the answer (Minto), structure the story as **Situation → Complication → Question → Answer** (SCQA), and support the answer with **MECE** key points and evidence.

Respect Prompt 01 **framing mode**:

| Mode | Meaning |
|------|---------|
| `decision-ready` | Narrative supports a capability decision; pyramid rests mainly on facts/derivations. |
| `hypothesis` | Narrative frames a **testable recommendation**; Answer is an experiment / learning plan, not a locked build mandate. |

---

## Entry criteria

- Prompt 01 exit criteria are met.
- Framing mode is declared (`decision-ready` or `hypothesis`).
- Facts vs assumptions are labeled; critical open questions are listed.
- Evidence acquisition backlog is available if mode is `hypothesis`.

---

## Produce

### 0. Narrative class (required)

State at the top of the output:

- **Narrative class:** `decision-ready` | `hypothesis` (must match Prompt 01 unless new evidence upgraded it — document the upgrade).
- **Evidence boundary:** what this narrative is allowed to claim.
- **Top blocking acquisition items** (from Prompt 01 backlog) that keep the class at `hypothesis`, if applicable.

### A. SCQA narrative

1. **Situation** — current state of operations, relevant facts, concise context. Prefer facts/derivations; label assumptions.
2. **Complication** — compound problem across applicable dimensions (operational, technical, financial, regulatory, human, environmental, security, data, or domain-specific).
3. **Question** — one bounded decision or engineering question that must be answered.
4. **Answer**
   - `decision-ready`: capability-level recommendation **without** preselecting architecture, vendor, or model.
   - `hypothesis`: capability-level **recommended experiment** — what to test, what would falsify it, and what evidence must be acquired before locking a decision.

Also define:

- desired outcomes and what “good” looks like;
- audience, decision horizon, evidence boundary, and authority boundary;
- measurable outcomes (baselines marked known vs unknown);
- explicit exclusions (what this decision does **not** cover).

### B. Minto Pyramid view of the Answer

Present the Answer as a pyramid:

1. **Governing answer** — one clear recommendation (or governing experiment in hypothesis mode).
2. **MECE key supporting points** (typically 3–7) — mutually exclusive, collectively exhaustive.
3. **Support under each point** — cite Prompt 01 facts/derivations; in `hypothesis` mode, assumptions are allowed **only if labeled** and tied to acquisition backlog items.

### C. Framing handoff pack

- Decision question locked for PRD / DDD (or provisional question if `hypothesis`).
- Success metrics that later PRD and DMAIC Measure/Control can use (note missing baselines).
- Open questions that block design (must be resolved or explicitly assumed).
- Whether later artifacts (PRD through ADR) must be marked **provisional**.

### Lean / DMAIC lens (spine — thin)

**DMAIC focus this stage:** **Define** (improvement problem and success measures).

In `dmaic_lens.md` (short), record:

1. What waste or rework does the Complication describe (map to DOWNTIME / AI waste names if clear)?  
2. Which success metrics are Measure targets for Prompt 09/12 (known vs Unknown baseline)?  
3. What must *not* be automated yet because Measure is missing (`hypothesis` → Measure-first)?  
4. One sentence: how the Answer reduces waste without adding model/process waste.

---

## Exit criteria (handoff to Prompt 03)

- [ ] Narrative class is stated and consistent with Prompt 01 (or documented upgrade).
- [ ] SCQA is complete; claims do not invent unlabeled facts.
- [ ] Pyramid is MECE; each support item is fact, derivation, or labeled assumption.
- [ ] In `decision-ready` mode: Answer is capability-level and evidence-backed.
- [ ] In `hypothesis` mode: Answer is an experiment with falsifiers and acquisition needs.
- [ ] Answer stays at capability level (no C4/tool lock-in).
- [ ] One bounded question is ready to drive PRD and domain modeling.
- [ ] `dmaic_lens.md` Define focus is complete (feeds Prompt 09).

---

## Constraints

- Do not write the full PRD, feature flows, bounded contexts, containers, or ADRs here.
- Do not expand scope beyond the evidence boundary without labeling new items as assumptions.
- Do not present a `hypothesis` narrative as if it were `decision-ready`.
- Do not run full Prompt 09 waste registers here.
- Think top-down; communicate so the audience sees answer → reasons → evidence/assumptions.

---

## Output

Write under `participant-outputs-v2/02-scqa/`:

- `scqa_minto_decision_narrative.md`
- `dmaic_lens.md`
