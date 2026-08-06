# Prompt 12 — Assurance & Control (Deliver & Evaluate)

**Lifecycle stage:** Deliver & Evaluate / DMAIC Control / Spec-Driven Development — Tests & Review  
**Framework derived:** Assurance against prior artifacts + DMAIC Measure/Control + AC verification  
**Core question:** Does the system match the design and the claims we make about it?  
**Prerequisites:** Prompt 11 build, task execution log, and updated traceability; Prompts 02–10 artifacts.  
**Primary output type:** Evaluation report with residual risk and control actions.

---

## Intent

Close the loop: audit the built system against **SCQA/PRD outcomes**, **feature ACs/BRs**, **technical contracts**, **DDD** rules/AI/HITL boundaries, **C4** structure, **ADR** decisions, and **Lean/DMAIC** measures. Separate **offline evaluation** (domain/AC cases) from **online/operability assurance** (runtime, security, degraded mode).

**DDD stage 16 (production readiness & handover):** assess what is production-ready vs still PoC; name handover owners.

**Lean spine close:** after scoring, produce `control_lens_rollup.md` consolidating `dmaic_lens.md` from Prompts **10–12** (and referencing Prompt 09 Control plan).

---

## Entry criteria

- Governed slice is runnable.
- Traceability matrix (FR → contract → AC → task → code/test) and PoC-vs-production list exist.
- DMAIC Measure targets and Control owners are defined.

---

## Assess

### Design fidelity

- Architecture-to-code consistency with C4 and DDD  
- ADR implementation (followed, violated, or deferred)  
- Technical contracts honored (APIs, validation values, error envelope)  
- Module rules respected (e.g. UI does not bypass API)  
- Ubiquitous language reflected in UX, APIs, and logs where claimed  
- Feature ACs and BRs verified or explicitly failed/inconclusive  

### Data & authority

- Data-contract handling (enforced, versioned, documented)  
- Identifier and timestamp behavior (stability, timezone/event vs report time)  
- Conflict and freshness visibility  
- Authority and prohibited-language / source-of-truth controls  
- Privacy; security and remote-access handling  

### AI / decision quality

- Deterministic behavior where claimed  
- Explainability of outputs  
- False-positive and false-negative examples documented  
- HITL paths exercised for domain-critical decisions  
- Evaluation cases use DDD vocabulary and feature AC IDs (from Prompts 04–05)  
- Lean evaluation waste check — metrics tied to release/risk decisions  

### Operability

- Degraded-mode operation  
- Critical user workflows end to end  
- Performance under expected load (vs NFRs in Prompt 08)  
- Observability useful for failure explanation (avoid observability waste)  

### Control & risk

- DMAIC Control: standards, monitors, owners, revisit triggers  
- Residual risk — accepted, deferred, or requiring sponsor decision  
- Open items from `spec_ambiguities` / `ambiguity_closure`  

---

## Produce

1. Evaluation report with **pass / fail / partial / `inconclusive (data scarcity)`** per assessment area (including each material AC).  
   Use `inconclusive (data scarcity)` when the claim cannot be verified because required evidence, baselines, or environments were unavailable — not when the test failed.
2. Evidence sampling notes (what was tested, what was not, what could not be tested due to scarcity).  
3. Defect & waste findings that should re-enter DMAIC Analyze/Improve.  
4. Updated residual risk register (include unresolved acquisition backlog items).  
5. Assumption-test results summary (from Prompt 11), if applicable.  
6. Go / conditional-go / no-go recommendation for demo vs production path.  
   **Production go is disallowed** while material areas remain `inconclusive (data scarcity)` unless sponsors explicitly accept that residual risk.

### Lean / DMAIC lens (spine — thin)

**DMAIC focus this stage:** **Control** (+ Measure verification).

In `dmaic_lens.md` (short), record:

1. Were Prompt 09 Measure targets actually checked? Pass / fail / inconclusive.  
2. Are Control owners and revisit triggers operating (or only documented)?  
3. Defect & waste findings to re-enter Analyze/Improve.  
4. Evaluation waste check — metrics that do not affect release decisions?

### Control lens rollup (close the spine)

Produce `control_lens_rollup.md`:

1. Table of `dmaic_lens.md` from Prompts **10, 11, 12** (+ summary link to Prompt 09 Control section)  
2. Measure targets: met / missed / inconclusive  
3. Wastes still open after build  
4. Next Discover/Frame loop recommendation (if any)  
5. Control owners for handover (feeds Prompt 13 / DDD stage 16)

### Production readiness & handover (DDD stage 16)

In `production_readiness.md` (short):

- What is production-ready vs PoC-only  
- Domain / ops / support owners  
- Open ADRs, open ambiguities, residual risks blocking production  
- Handover checklist status

---

## Exit criteria (handoff to Prompt 13)

- [ ] Claims in SCQA/PRD/ADRs/ACs are verified, falsified, partial, untested, or `inconclusive (data scarcity)`.
- [ ] PoC vs production gaps are evidence-based.
- [ ] Residual risks and sponsor decisions (including data-access needs) are explicit.
- [ ] Control owners and revisit triggers are named.
- [ ] `control_lens_rollup.md` consolidates lenses 10–12.
- [ ] `production_readiness.md` covers DDD stage 16 handover concerns.
- [ ] `dmaic_lens.md` Control focus is complete.

---

## Constraints

- Do not hide failed ADR or AC compliance; record deviations.
- Do not invent production readiness — distinguish demonstrated vs required.
- Do not treat `inconclusive (data scarcity)` as a pass.
- Prefer concrete FP/FN examples over generic quality statements.

---

## Output

Write under `participant-outputs-v2/12-evaluation/`:

- `evaluation_report.md`
- `dmaic_lens.md`
- `control_lens_rollup.md`
- `production_readiness.md`
- Optional: `control_plan.md`, `fp_fn_examples.md`, `ac_results.md`
