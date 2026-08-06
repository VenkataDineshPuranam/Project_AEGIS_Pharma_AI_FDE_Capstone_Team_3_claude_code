# Prompt 11 — Deliver (Execute Tasks / AI Coding + Tests)

**Lifecycle stage:** Deliver / Spec-Driven Development — AI Coding **and** Tests (intentionally merged)  
**Framework applied:** Executes Prompt 10 tasks against PRD, features, C4, ADRs, technical contracts, and Lean constraints  
**Core question:** How do we ship the governed slice by executing one task at a time — with AC-linked tests?  
**Prerequisites:** Prompt 10 task index + `ac_test_plan.md`; Prompts 03–09 artifacts as referenced by each task; Prompt 09 structural reopen `cleared`.  
**Primary output type:** Working implementation + test evidence + updated traceability.

---

## Intent

**Implement** the minimum governed workflow by executing **Prompt 10 tasks in order** — one task (or small batch) per agent run. Load only the specs each task lists. Do not invent contracts, ACs, or architecture during coding.

**SDD note:** Spec-Driven Development lists **Tests** as its own stage. This library **intentionally merges** Coding + Tests into Prompt 11 (AC verification continues in Prompt 12), same style as Architecture-before-Technical. Do not skip the AC test plan.

**DDD stage 15 (pilot, learn & refine):** treat this build as the pilot slice — capture learnings that would change the domain model.

**Scarce-data rule:** if narrative class is `hypothesis` or artifacts are `provisional`, finish assumption-test / Measure tasks before feature enrichment.

---

## Entry criteria

- Task index and `ac_test_plan.md` exist; blocked tasks are labeled.  
- Technical traceability matrix exists.  
- Prompt 09 structural reopen gate is `cleared`.  
- Lean build constraints and (if needed) assumption-test priorities are ranked.  
- Out-of-scope from PRD remains visible.

---

## Produce / do

1. **Execute tasks in order** from `task_index.md` — for each task, load only its listed specs.  
2. **Assumption-test / Measure tasks first** when required by hypothesis/provisional/Lean.  
3. **Implement** per module rules (Prompt 08) inside the C4 shape.  
4. **Add/update tests** per `ac_test_plan.md` that prove the task’s ACs/BRs/NFRs **before** moving on; update the plan with pass/fail/deferred.  
5. **Prohibit operational write-back** unless ADR/technical design explicitly authorizes it.  
6. **Keep specialist authority visible** — HITL for domain-critical decisions remains obvious in UX and logs.  
7. **Update traceability** — FR → contract → AC → task → code/test paths.  
8. **PoC vs production label** — mark what is demonstrated vs still required.  
9. **Explanation & uncertainty behavior** — implement as specified in features/technical design (do not invent silently).  
10. **Pilot learnings (DDD stage 15)** — write `pilot_learnings.md`: what would change in domain model, features, or contracts after this pilot.
### Lean / DMAIC lens (spine — thin)

**DMAIC focus this stage:** **Improve** execution — remove waste while building; do not introduce new AI wastes.

In `dmaic_lens.md` (short), record:

1. Which Prompt 09 must-fix items were actually implemented?  
2. New wastes introduced during build (token bloat, extra agent loops, duplicate validation)?  
3. Measure instrumentation shipped (or still missing)?  
4. Deferrals that should return to DMAIC Analyze/Improve?

---

## Exit criteria (handoff to Prompt 12)

- [ ] All non-blocked tasks for the governed slice are done or explicitly deferred with risk.  
- [ ] `ac_test_plan.md` updated: in-scope ACs are pass, fail, or deferred with risk (none silently skipped).  
- [ ] AC-linked tests exist for completed features.  
- [ ] ADR guardrails and prohibited write paths are respected (or deviations logged).  
- [ ] Traceability matrix is updated with code/test links.  
- [ ] `pilot_learnings.md` exists (DDD stage 15).  
- [ ] PoC vs production gaps are listed for Assurance and Proposal.  
- [ ] `dmaic_lens.md` is complete.

---

## Constraints

- Do not invent API shapes, thresholds, or error codes — fix Prompt 08 (or 05) instead.  
- Do not hard-code conclusions for specific entities from source data.  
- Do not silently override ADRs, domain invariants, or PRD out-of-scope.  
- Do not scale features Lean marked as overproduction/token/model waste.  
- Do not expand beyond the minimum governed slice while critical assumptions remain untested (unless throwaway spike).

---

## Output

Write under `participant-outputs-v2/11-build/`:

- `task_execution_log.md` (task ID → status, PR/commit, notes)
- `traceability_matrix_updated.md`
- `poc_vs_production.md`
- `assumption_test_results.md` (if applicable; else “n/a”)
- `ac_test_plan_results.md` (updated from Prompt 10 plan)
- `pilot_learnings.md`
- `dmaic_lens.md`
- application source (as applicable)
