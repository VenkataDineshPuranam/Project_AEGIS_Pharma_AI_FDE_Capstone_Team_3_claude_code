---
name: spec-driven-delivery
description: >-
  Applies Spec-Driven Development: progressive layered specs with Architecture
  before Technical Design, artifact mirrors, matching/confidence checklists,
  Specs-to-load tasks, PoC vs production labeling, and gated AI coding. Use when
  the user asks about spec-driven development, PRD/FRD/SRS, agentic coding from
  specs, or acceptance criteria.
---

# Spec-Driven Delivery

Portable skill for any repo. Merges layered-spec teaching with engagement artifact contracts.

## Failure mode to avoid

One enormous document that answers everything badly → nobody (including the agent) reads it; retrieval pulls noise; review dies.

## Principle

**Do not write everything down. Reduce ambiguity progressively.**  
Each layer answers exactly one question; AI value rises as ambiguity falls.

## Five layers (chosen order)

| Document | Answers | Audience | AI value |
|---|---|---|---|
| **PRD** | What problem are we solving? | Product/stakeholders | Medium |
| **FRD / Feature spec** | What should the system do? (one feature/file) | BA/devs | High |
| **Design / Architecture (C4)** | How will we build it? / where does code belong? | Engineers | Very high |
| **SRS / Technical Design** | Exactly how should it behave? (I/O, validation, errors) | Devs/QA/agents | Very high |
| **Implementation tasks** | What code needs writing? | Devs/agents | Very high |

**Architecture before Technical Design.** Placement before contracts reduces silent wrong-layer implementations. Some SDD slides reverse this — this consolidated skill **intentionally does not**.

### Layer rules

- **PRD** omits workflows/screens/endpoints/data models on purpose. Carry narrative class; mark provisional under `hypothesis`.  
- **FRD**: actor, preconditions, happy path, exceptions, BRs, ACs, HITL/AI boundaries, ambiguities — **one feature per file**.  
- **Architecture**: topology, boundaries, degraded mode, prohibited paths (ties to C4/ADRs + review gate).  
- **SRS / Technical Design**: exact payloads, validation **with numbers**, status codes, NFRs, error envelope, module rules, pre-build traceability, ambiguity closure — entry only after architecture review `pass` or `conditional`.  
- **Tasks**: small units with **Specs to load** (exact paths); nothing left to guess.

The question is never PRD *or* FRD *or* SRS. It is **which question this particular file is answering.**

## Upstream spine

Before coding agents run:

```text
Discovery → SCQA → PRD → DDD → Feature Specs → C4 → ADRs (+ review) → Technical Design
→ Lean → Tasks → Deliver → Assurance → Propose
```

Chat transcripts are not specs. Specs are version-controlled beside code and reviewable in one sitting.

## Artifact mirrors (required)

| Layer | Trail | Mirror | Also write |
|---|---|---|---|
| PRD / Vision | `participant-outputs-v2/03-prd/` | `specs/product/` | `vision.md`, `prd.md`, `scope_in_out.md`, `dmaic_lens.md` |
| Feature Specs | `participant-outputs-v2/05-features/` | `specs/features/` | FR files, registers, `matching_confidence_checklist.md` (or N/A), `dmaic_lens.md` |
| C4 / ADR / review | `06-c4/`, `07-adrs/` | `specs/architecture/` | (see `domain-and-architecture`) |
| Technical Design | `participant-outputs-v2/08-technical/` | `specs/api/`, `specs/data/`, `specs/testing/` | `api_contracts`, `data_model`, `state_transitions`, `nfrs`, `error_and_security`, audits below |
| Tasks | `participant-outputs-v2/10-tasks/` | `tasks/` + `specs/testing/ac_test_plan.md` | `task_index.md`, `ac_test_plan.md`, `dmaic_lens.md` |
| Deliver | `participant-outputs-v2/11-build/` | application source | results + `pilot_learnings.md` |

**Tests stage:** intentionally merged into Deliver (11) with AC verification in Assurance (12) — same documentation style as Architecture-before-Technical.

## PRD outputs (stage 03)

`vision.md`, `prd.md`, `scope_in_out.md`, `dmaic_lens.md` (Define: which in-scope capabilities remove waste vs add capability; exclusions preventing overproduction; metrics → Measure list; what would create token/model/review waste if built too early).

## Matching / confidence checklist (when applicable)

If a feature involves matching, classification, detection acceptance, or confidence-gated decisions:

1. Priority order of strategies (e.g. exact → alias → fuzzy) — fixed, not “best effort”  
2. Numeric thresholds per stage (or Unknown → discovery backlog + `spec_ambiguities.md`)  
3. Rejection behavior below threshold  
4. Dedup / quantity rules  

Do not leave “validate confidence” without a number or an explicit Unknown.

Also produce: `feature_index.md`, `business_rules_register.md`, `acceptance_criteria_register.md`, `spec_ambiguities.md`, **`matching_confidence_checklist.md`** (or “N/A — no confidence-gated features”), `dmaic_lens.md`.

## Technical Design (stage 08)

Entry: architecture review `pass` or `conditional`.

**Core contracts** (mirror to `specs/api/`, `specs/data/`, `specs/testing/` as applicable):

- `api_contracts.md` (or OpenAPI YAML set)  
- `data_model.md`  
- `state_transitions.md`  
- `nfrs.md`  
- `error_and_security.md`  
- `module_rules.md`  

**Traceability & closure:**

- `traceability_matrix.md` — columns: Feature/FR · Endpoint · BR · AC · ADR · Ambiguity status  
- **`traceability_gap_audit.md`** — flag: FR without AC; BR without verifying AC/threshold; AC without endpoint; Endpoint without FR; Matching rule without number; Error/security rule without AC/NFR — each fixed now, assumed with revisit, or open-blocked (**no unmarked orphans**)  
- `ambiguity_closure.md`  
- `matching_thresholds.md` (or N/A)  
- `dmaic_lens.md` (contract caps on Token/Retrieval/Context; retries vs Model waste; Control NFRs)

## Implementation tasks (stage 10)

**Entry:** Prompt 09 `structural_reopen.md` gate is **`cleared`**.

Prioritize:

1. Assumption tests / Measure instrumentation (if hypothesis/provisional/Measure-first)  
2. Foundational contracts  
3. Features in dependency order  
4. **Tests mapped to ACs** (required)  
5. Docs/deployment as needed  

Each `task-00N.md`: Goal · Specs to load · Out of scope · Steps · Acceptance checks · Test expectations · Done when. Mark `blocked` if ambiguities remain.

**`ac_test_plan.md`:** table `AC ID | Test task ID(s) | Test type | Status` — every in-scope AC has ≥1 test task or explicit deferral. Mirror to `specs/testing/ac_test_plan.md`.

Also: `task_index.md`, `dmaic_lens.md`.

## Deliver (stage 11) — Coding + Tests merged

1. Execute tasks in order; load only listed specs.  
2. Add/update tests per `ac_test_plan.md`; update plan with pass/fail/deferred — none silently skipped.  
3. Prohibit operational write-back unless ADR/tech design authorizes; keep HITL visible.  
4. Update traceability; label **PoC vs production**.  
5. Produce **`pilot_learnings.md`** (DDD stage 15 — what would change in domain model, features, or contracts).  
6. Produce `ac_test_plan_results.md`, `assumption_test_results.md` (or n/a), `dmaic_lens.md`, `task_execution_log.md`, `traceability_matrix_updated.md`, `poc_vs_production.md`.

## Spec → implement → gate loop

1. Write/update the correct layer for the open question only.  
2. Add testable acceptance criteria.  
3. Spec quality review (second pair of eyes).  
4. Architecture review must be `pass` or `conditional` before Technical Design locks.  
5. Lean structural reopen must be **`cleared`** before tasks.  
6. Break into tasks + `ac_test_plan.md`.  
7. Deliver: implement + tests per plan; pilot learnings.  
8. CI eval/test gates fail closed; run Assurance (`delivery-ops-llmops`) against ACs/ADRs.  
9. Architecture drift → ADR (+ reopen if needed), not silent merge.

## Spec quality checklist

- [ ] One job / one question per file  
- [ ] In scope and out of scope both listed  
- [ ] Authority/advisory limits stated  
- [ ] Exceptions and error cases included  
- [ ] Acceptance criteria verifiable  
- [ ] Assumptions vs open questions separated  
- [ ] Consistent ubiquitous language  
- [ ] Thresholds numeric or Unknown  
- [ ] Traceability: FR → contract → AC → task → code/test  
- [ ] `traceability_gap_audit` has no unmarked orphans  
- [ ] Every AC mapped in `ac_test_plan`  
- [ ] Thin `dmaic_lens.md` present for this stage  

## Design-document shape

When producing an SDD/design doc, include at least: purpose, in/out scope, numbered architecture principles (`AP-1`, `AP-2` —
so later sections and reviews can cite them), components/APIs, data model outline, non-functionals, prohibited paths, and
acceptance mapping — without inventing unstated product facts. VisionScan-style: module rules (e.g. UI never bypasses API), standard error envelope, transactional checkout rules with rollback.

## Do / Don’t

- **Do:** progressive layers; Architecture before Technical Design; one feature per FRD; Specs-to-load; Tests merged into Deliver via `ac_test_plan`; clear structural reopen before tasks  
- **Don’t:** 200-page mega-spec; contracts before review gate; invent APIs from a PRD alone; skip AC test plan; hand off to tasks while reopen is `blocked`  
