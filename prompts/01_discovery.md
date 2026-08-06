# Prompt 01 — Discovery (AI FDE Inputs)

**Lifecycle stage:** Discover  
**Framework derived:** Prerequisite evidence base (AI FDE inputs from the Lean–DMAIC mental model)  
**Core question:** What exists, how does it connect, and what can we trust?  
**Prerequisites:** Access to the repository, codebase, and/or source materials (may be scarce).  
**Does not derive yet:** SCQA narrative, DDD model, C4, ADR, full Lean plan, or target architecture.

---

## Intent

Establish the factual foundation for every later framework. Collect **business context, user workflow, constraints, evidence, and stakeholder needs** without proposing a solution architecture.

When materials are thin, Discovery still runs — but it must **score sufficiency**, produce an **evidence acquisition backlog**, and declare whether Prompt 02 may be **decision-ready** or **hypothesis-only**.

Lean/DMAIC starts here as a **thin Measure/Define lens** (not the full Prompt 09 workshop).

---

## Entry criteria

- Whatever source materials exist are available for inspection (complete pack not required).
- Engagement scope (systems / repos in bounds) is stated.
- Known access gaps (no prod data, no SME, no SoT docs) are listed up front if known.

---

## Produce

1. **Repository and source-system map** — what exists, where it lives, and how it connects.
2. **Entities, identifiers, and timestamp semantics** — what is tracked, how it is named, and what time means in each context (event time vs report time if observable).
3. **Evidence ownership and authority** — source of truth for each material data class; who or what may assert it.
4. **Material inconsistencies, gaps, and conflicts** — where data disagrees, is missing, or cannot be trusted.
5. **Stakeholder decisions and decision horizons** — decided, pending, and timeframes.
6. **Constraints register** — technical, risk, compliance, security, privacy, and operational constraints already visible in evidence.
7. **Current-state workflow sketch** — how work is done today (as observed, not redesigned). Mark inferred steps as assumptions.
8. **Fact / derivation / assumption / question register** — classify every material finding into exactly one category.
9. **Top ten investigation hypotheses** — ranked by impact on later framing and design.

10. **AI FDE input sufficiency score** — rate each input **Strong / Partial / Missing**:

    | AI FDE input | Score | What exists | What is missing |
    |--------------|-------|-------------|-----------------|
    | Business context | | | |
    | User workflow | | | |
    | Constraints | | | |
    | Evidence (data, logs, research) | | | |
    | Stakeholder needs | | | |

    **Overall framing mode (required):**
    - `decision-ready` — Situation/Complication can be written mainly from facts/derivations; no critical inventing.
    - `hypothesis` — one or more inputs are Partial/Missing such that framing must proceed as a testable hypothesis, not a locked decision.

    Rule of thumb: if **Evidence** or **User workflow** is Missing, or two+ inputs are Missing, default to `hypothesis` unless a reviewer explicitly overrides.

11. **Evidence acquisition backlog** — ordered list of what to obtain next. For each item: artifact needed, likely owner/source, why it blocks (which later prompt), and priority (blocks framing / blocks design / blocks production).

12. **Early waste signals (Lean preview — not full DMAIC)** — while inspecting the current workflow, note observed or hypothesized wastes for Prompt 09. Use DOWNTIME letters and/or AI-specific waste names where visible (e.g. Waiting on approvals, Extra processing, Token/Retrieval waste). Mark each as **observed** vs **hypothesized**. Do **not** run full DMAIC or redesign here.

### Lean / DMAIC lens (spine — thin)

**DMAIC focus this stage:** **Measure** (baseline signals) + light **Define** (what improvement space exists).

In `dmaic_lens.md` (short — not a full waste workshop), record:

1. What can already be measured (cycle time, error rate, backlog, token/cost signals, review lag)?  
2. What baselines are **Unknown**?  
3. Top 3 early waste signals (DOWNTIME or AI-specific) with observed vs hypothesized.  
4. What must Prompt 09 Measure before scaling automation?

---

## Exit criteria (handoff to Prompt 02)

- [ ] Sources of truth and trust gaps are explicit.
- [ ] No target architecture, tool selection, or full risk model is proposed.
- [ ] Assumptions and open questions are separated from facts.
- [ ] Sufficiency scores and **framing mode** (`decision-ready` or `hypothesis`) are declared.
- [ ] Evidence acquisition backlog exists whenever any input is Partial or Missing.
- [ ] Early waste signals and `dmaic_lens.md` are listed (even if “none observed — revisit in Prompt 09”).
- [ ] If `decision-ready`: enough evidence exists to write Situation and Complication without inventing facts.
- [ ] If `hypothesis`: Situation/Complication may use labeled assumptions; inventing unlabeled “facts” is still forbidden.

---

## Constraints

- Do not propose a target architecture or solution design.
- Do not invent domain language; quote or flag ambiguous terms for Prompt 04 (DDD).
- Prefer evidence citations (path, system, artifact) over unsupported claims.
- Do not upgrade `hypothesis` to `decision-ready` without new evidence.
- Do not treat early waste signals as measured baselines.
- Do not run full Prompt 09 Lean workshop here.

---

## Output

Write under `participant-outputs-v2/01-discovery/`:

- `evidence_register.md` (includes sufficiency scores and framing mode)
- `evidence_acquisition_backlog.md` (required if any input is Partial or Missing; otherwise note “none”)
- `early_waste_signals.md`
- `dmaic_lens.md`
