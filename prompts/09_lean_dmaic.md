# Prompt 09 — Lean & DMAIC (Improve Lens)

**Lifecycle stage:** Improve before scale (also feeds later Control)  
**Framework derived:** Lean (DOWNTIME + AI-specific wastes) and DMAIC  
**Core question:** Where is waste, and how will we Define → Measure → Analyze → Improve → Control?  
**Prerequisites:** Prompts 01–08 (evidence, framing, PRD, domain, features, C4, ADRs, technical contracts).  
**Primary output type:** Waste register and DMAIC improvement plan.

---

## Intent

**Consolidate** the Lean / DMAIC operating spine before tasks and coding. Prior prompts (01–08) already produced thin `dmaic_lens.md` files — **do not ignore them**. Start from those lenses + Prompt 01 early waste signals, then produce the **full** DOWNTIME + AI-waste registers and a complete DMAIC plan.

Reference guidance: use waste lenses before automating, orchestrating, or scaling AI workflows.

**Scarce-data rule:** if Prompt 01 baselines are Missing/Partial or narrative class is `hypothesis`, DMAIC is **Measure-first** — instrumentation, sampling, and evidence acquisition outrank new AI features.

---

## Entry criteria

- SCQA/PRD measurable outcomes exist (baselines may be unknown).
- Prompt 01 sufficiency scores, evidence acquisition backlog, and **early waste signals** are available.
- **`dmaic_lens.md` from Prompts 01–08** are available (or gaps noted).
- Architecture review from Prompt 07 is `pass` or `conditional`.
- Feature ACs and technical contracts exist for the governed slice.
- Minimum governed workflow (DDD) and C4 path are defined.
- ADRs state what must be validated.

---

## Produce

### 0. Lens roll-up (required first)

Create `lens_rollup.md`:

- Table of prior `dmaic_lens.md` paths (01–08) with DMAIC focus and top findings  
- Merged list of wastes already named (dedupe)  
- Gaps where a prior lens was missing or shallow  

Then deepen into the full registers below — do not restart from a blank page.

### A. DMAIC plan

1. **Define** — problem/scope for improvement (aligned to Prompt 02/03 Question/Answer and PRD scope; incorporate Define notes from lenses 02–03).
2. **Measure** — current-state metrics and target metrics (baseline from Prompt 01 / lenses where possible). Explicitly list **unknown baselines**. Tie targets to feature ACs where applicable.
3. **Analyze** — root causes and gaps (link to evidence register, prior lenses, and waste findings). Mark analyses that rest on assumptions.
4. **Improve** — design/pilot changes to remove waste (what Prompts 10–11 must implement or explicitly defer).
5. **Control** — standards, governance, monitoring ownership, and revisit triggers (feeds Prompt 12; reuse ADR revisit triggers from lens 07).

**If baselines are unknown or framing mode is `hypothesis`:**

- Put **instrumentation / sampling / evidence acquisition** at the top of Improve.
- Do not schedule scale-out of agents, retrieval, or automation ahead of Measure capability.
- Cross-link Improve items to `evidence_acquisition_backlog.md`.

### B. DOWNTIME waste register (AI FDE)

For each waste, note: where observed (current and/or proposed), **observed vs hypothesized**, impact, and eliminate/simplify action.

| Code | Waste | Focus |
|------|-------|--------|
| D | Defects | Hallucinations, bad classifications, malformed outputs, missing citations, failed tool calls |
| O | Overproduction | Unused reports/features/model outputs |
| W | Waiting | Data access, approvals, environments, APIs, human review, model latency |
| N | Non-utilized talent | SMEs on repetitive checks vs complex exceptions |
| T | Transportation | Cross-system moves, spreadsheet exports, repeated ETL |
| I | Inventory | Backlogs, unreviewed AI outputs, stale embeddings, pending exceptions |
| M | Motion | Screen switching, prompt copying, context reconstruction |
| E | Extra processing | Duplicate validation, repeated retrieval, agent loops, excess approvals |

### C. AI-specific waste register

Assess and plan actions for:

1. Token waste  
2. Retrieval waste  
3. Model waste  
4. Human-review waste  
5. Evaluation waste  
6. Integration waste  
7. Context waste  
8. Observability waste  

### D. Build constraints from Lean

List **must-fix-before-build** vs **fix-in-pilot** vs **accept-as-residual-risk** items for Prompts 10–13.

### E. Structural change gate (required)

If Improve actions require changes to **C4 structure, ADRs, or technical contracts**, do **not** proceed silently to Prompt 10.

Produce `structural_reopen.md`:

1. **Reopen required?** `yes` | `no`  
2. If `yes`: which of Prompts **06 / 07 / 08** must be re-run (list files/ADRs/contracts to update)  
3. **Status flip** — mark affected ADRs `proposed` or `superseded` as needed; architecture review may return to `conditional`  
4. **Gate decision**
   - `blocked` — stop; complete reopen loop; re-pass architecture review / contracts  
   - `cleared` — no structural reopen, or reopen completed and documented  

**Prompt 10 entry requires `cleared`.**

---

## Exit criteria (handoff to Prompt 10)

- [ ] Lens roll-up from Prompts 01–08 exists.
- [ ] DMAIC Define/Measure targets align with Prompt 02/03 outcomes and feature ACs.
- [ ] Unknown baselines are listed; Measure-first actions exist when baselines are missing.
- [ ] Material DOWNTIME and AI wastes are registered with actions and observed vs hypothesized labels.
- [ ] Prompt 10 task order can prioritize assumption tests, waste removal, and risk reduction.
- [ ] Control/monitoring ownership is named for Assurance.
- [ ] `structural_reopen.md` exists with gate decision `cleared` (or reopen completed).

---

## Constraints

- Do not pretend wastes are fixed without a Measure baseline or explicit assumption.
- Do not expand architecture casually; if waste removal needs a structural change, open/update an ADR **and** set structural reopen.
- Prefer removing waste over adding agents/models.
- Under scarcity, do not prioritize feature scale over instrumentation.
- Do not ignore prior `dmaic_lens.md` files — consolidate them.
- Do not hand off to Prompt 10 while structural reopen is `blocked`.

---

## Output

Write under `participant-outputs-v2/09-lean-dmaic/`:

- `lens_rollup.md`
- `dmaic_plan.md`
- `waste_register_downtime.md`
- `waste_register_ai_specific.md`
- `build_constraints_from_lean.md`
- `structural_reopen.md`
