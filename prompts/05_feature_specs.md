# Prompt 05 — Feature Specifications (FRD)

**Lifecycle stage:** Spec-Driven Development — Feature Specification  
**Framework derived:** Spec-Driven Development (modern FRD); VisionScan-style functional requirements  
**Core question:** What should the system do — per feature?  
**Prerequisites:** Prompt 03 PRD/scope; Prompt 04 DDD (ubiquitous language, contexts, invariants, Gen AI boundaries).  
**Primary output type:** One feature specification file per capability (plus index).

---

## Intent

Derive **feature specifications**: workflows, business rules, edge cases, and acceptance criteria — **one feature per file**. Use DDD language; do not invent technical contracts yet (APIs/schemas belong in Prompt 08).

SDD rule: Authentication does not belong in the same document as the assessment engine — keep features isolated and reviewable.

---

## Entry criteria

- PRD in/out scope is locked (or explicitly provisional).  
- Ubiquitous language and bounded contexts exist.  
- Rules vs AI vs HITL boundaries are available when features involve AI.

---

## Produce

### A. Feature index

List every in-scope feature for this version with: ID (e.g. FR-001), name, owning bounded context, priority, and status (`stable` | `provisional`).

### B. One file per feature

For each feature, include:

1. **Feature ID & name**  
2. **Actor(s)**  
3. **Preconditions** — what must already be true  
4. **Happy path flow** — ordered steps (business language)  
5. **Exceptions / alternate paths**  
6. **Business rules** — numbered testable sentences (e.g. BR-00N) tied to this feature  
7. **Acceptance criteria** — binary, testable (e.g. AC-00N); no meeting required to adjudicate  
8. **HITL / AI boundaries** — if applicable: what AI may do vs rules vs human  
9. **Out-of-scope notes** — what this feature file deliberately excludes  
10. **Ambiguities** — unspecified thresholds, missing values, undefined rejection behavior (must not be left silent)

### C. Matching / confidence checklist (when applicable)

If the feature involves product matching, classification, detection acceptance, or any confidence-gated decision (VisionScan-style), also specify or flag as ambiguity:

1. **Priority order** of match strategies (e.g. exact → alias → fuzzy / domain equivalent) — fixed order, not “best effort”  
2. **Numeric acceptance threshold(s)** per stage (or Unknown → Prompt 01 backlog + `spec_ambiguities.md`)  
3. **Rejection behavior** when below threshold (error code intent in business language; exact HTTP codes in Prompt 08)  
4. **Dedup / quantity rules** if repeated detections are possible  

Do not leave “validate confidence” or “fuzzy match” without a number or an explicit Unknown.

### D. Spec hygiene

- **One question per file:** “What should *this* feature do?”  
- Prefer precise values (“confidence ≥ 0.85”) over adjectives (“high confidence”). If unknown, record in ambiguities and Prompt 01 acquisition backlog.  
- Do not embed OpenAPI schemas or table DDLs here.

### Lean / DMAIC lens (spine — thin)

**DMAIC focus this stage:** **Analyze** (failure/rework paths) + **Improve** by specifying less wasteful flows.

In `dmaic_lens.md` (short), record:

1. Per critical feature: which AC/BR prevents Defects or Extra processing?  
2. Where do exceptions create Waiting / Inventory (queues, unreviewed outputs)?  
3. Confidence/matching ambiguities that would cause retries, false accepts, or review waste?  
4. Features that look like Overproduction relative to PRD scope?

---

## Exit criteria (handoff to Prompt 06)

- [ ] Every in-scope PRD capability maps to at least one feature file (or an explicit deferral).  
- [ ] Each feature has actor, flow, exceptions, BRs, and ACs.  
- [ ] Ambiguities are listed (thresholds, errors, state rules).  
- [ ] Matching/confidence checklist completed or marked N/A for each feature.  
- [ ] Features use DDD ubiquitous language.  
- [ ] No API/data-model invention beyond business fields named in language.  
- [ ] `dmaic_lens.md` is complete (feeds Prompt 09).

---

## Constraints

- Do not produce C4 diagrams or endpoint tables here.  
- Do not merge unrelated features into one file.  
- Do not pull PRD out-of-scope items back in without changing Prompt 03.  
- Do not run full Prompt 09 here.

---

## Output

Write under `participant-outputs-v2/05-features/` **and mirror** to `specs/features/`:

- `feature_index.md`
- `FR-001-<slug>.md` … (one file per feature)
- `business_rules_register.md` (all BRs across features)
- `acceptance_criteria_register.md` (all ACs across features)
- `spec_ambiguities.md`
- `matching_confidence_checklist.md` (or “N/A — no confidence-gated features”)
- `dmaic_lens.md`
