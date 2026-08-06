# Prompt 07 — Architecture Decision Records + Review / Defense (Decide)

**Lifecycle stage:** Decide + Architecture review / defense  
**Framework derived:** ADR — Architecture Decision Records; C4+ADR “review / defense” step  
**Core question:** Why does the system look that way — and can we defend the map before contracts and coding?  
**Prerequisites:** Prompt 06 C4 views and `adr_candidates.md`; Prompt 04 Gen AI boundaries; Prompt 05 feature risks as needed.  
**Primary output type:** Decision memory behind the C4 map + architecture review record.

---

## Intent

Derive the **ADR framework**: for each significant choice, record Context → Decision → Consequences → Status, plus alternatives, guardrails, validation, and revisit triggers. Together with C4: **Structure + Rationale**.

If C4/DDD are `provisional` or Prompt 02 is `hypothesis`, keep material ADRs in **`proposed`** until validation evidence exists; do not mark them `accepted` without evidence or explicit interim assumption + revisit trigger.

Lean/DMAIC continues here as a **thin Analyze/Control lens** (waste implications of decisions + revisit triggers).

---

## Entry criteria

- C4 map exists and exposes real trade-offs.
- C4 artifact status (`stable` | `provisional`) is known.
- ADR candidates are listed (expand if discovery reveals more).

---

## Produce

Create **at least five** ADRs. Prefer decisions that affect identity, evidence, authority, AI behavior, or operability.

### Suggested decision themes (use what applies)

- Entity identity and identification across systems  
- Event time versus report time  
- Canonical models and source translation  
- Rules vs analytics/AI vs explainability  
- Data persistence and evidence snapshots  
- Online, intermittent, and offline operation  
- Role and authority enforcement (including HITL)  
- Decision audit  
- RAG / retrieval and model-use boundaries  
- Agent tool permissions and stop conditions  
- External integrations  
- Deployment and observability  

### Required fields per ADR

- Title and **status** (proposed, accepted, deprecated, superseded)
- **Evidence basis** — fact / derivation / assumption (tie to Prompt 01)
- **Context** — situation or forces
- **Decision** — what was chosen
- **Alternatives considered** — and why rejected
- **Drivers** — primary influencing factors
- **Consequences** — easier / harder / riskier
- **Guardrails** — constraints that must not be violated
- **Validation** — how the decision will be tested or verified
- **Revisit triggers** — when to re-examine (required if status is `proposed` or evidence basis is assumption)

Also produce a one-page **decision index** linking each ADR to C4 elements and DDD contexts, and listing which ADRs are blocked on the evidence acquisition backlog.

### Architecture review / defense (required)

Per C4+ADR workflow: after key choices are recorded, run an **architecture review / defense** before technical contracts and tasks lock in.

Produce `architecture_review.md` with:

1. **Review status:** `pass` | `conditional` | `fail`  
2. **Defensibility checks**
   - C4 map matches DDD bounded contexts and in-scope features  
   - Material trade-offs have ADRs  
   - Trust, authority, privacy, degraded-mode, prohibited writes are visible  
   - Gen AI / HITL / rules boundaries are placed on the map  
   - Out-of-scope from PRD is not smuggled into containers  
3. **Open issues** — blockers vs accept-as-residual  
4. **Go-forward decision** — may proceed to Prompt 08 only if status is `pass` or `conditional` with named conditions; `fail` loops to Prompt 06/07  

Under `hypothesis` / `provisional`, prefer `conditional` unless evidence supports `pass`.

### Lean / DMAIC lens (spine — thin)

**DMAIC focus this stage:** **Analyze** trade-offs that create or remove waste; set **Control** revisit triggers.

In `dmaic_lens.md` (short), record:

1. Which ADRs explicitly prevent a named waste (e.g. rules-before-LLM → Defects/Model waste)?  
2. Which decisions risk new Waiting / Human-review / Token waste?  
3. Validation + revisit triggers that serve DMAIC Control later?  
4. Architecture review open issues that are really waste risks?

---

## Exit criteria (handoff to Prompt 08)

- [ ] At least five ADRs cover the material trade-offs on the C4 map.
- [ ] Rules/AI/HITL/authority choices from DDD are reflected in decisions where relevant.
- [ ] Each ADR has validation and revisit triggers (supports later DMAIC Control).
- [ ] Status values are explicit; under `provisional`/`hypothesis`, material ADRs are `proposed` unless evidence supports `accepted`.
- [ ] Architecture review status is `pass` or `conditional` (not `fail`).
- [ ] “Proposed” items needing sponsor input or data access are flagged for Prompt 13.
- [ ] `dmaic_lens.md` is complete (feeds Prompt 09).

---

## Constraints

- Do not silently change the domain model; if a decision requires domain change, note a Prompt 04 revision.
- Do not write full API schemas here — that is Prompt 08 (but ADRs may constrain them).
- Do not start implementation detail that belongs in Prompt 11 unless needed to make the decision testable.
- Do not mark assumption-based decisions `accepted` without interim assumption + revisit trigger called out.
- Do not skip architecture review / defense.
- Do not run full Prompt 09 here.
- Prefer fewer sharp ADRs over many vague ones.

---

## Output

Write under `participant-outputs-v2/07-adrs/` **and mirror** to `specs/architecture/`:

- `ADR-001-....md` … (one file per ADR)
- `decision_index.md`
- `architecture_review.md`
- `dmaic_lens.md`
