# Prompt 03 — PRD / Vision (Product Intent)

**Lifecycle stage:** Spec-Driven Development — Vision / PRD  
**Framework derived:** Spec-Driven Development (layered specs); complements SCQA framing  
**Core question:** What problem are we solving, for whom, and what does success look like?  
**Prerequisites:** Prompt 02 SCQA/Minto narrative (decision-ready or hypothesis).  
**Primary output type:** Product vision + PRD (business intent only — no APIs, screens, or data models).

---

## Intent

Turn the framed ask into a **PRD / Vision** artifact: problem, users, goals, success metrics, and **in-scope / out-of-scope**. This layer establishes whether the thing is worth building.

Per Spec-Driven Development: useful for reasoning about the business; **not yet** useful for writing code. An agent given only this must not invent workflows, endpoints, or schemas — those come later.

---

## Entry criteria

- Prompt 02 narrative class is stated (`decision-ready` | `hypothesis`).
- One bounded question / governing answer (or experiment) exists.
- Evidence boundary from Prompt 01/02 is known.

---

## Produce

### A. Vision (short)

- Product name / working title  
- One-paragraph problem statement (aligned to SCQA Situation/Complication)  
- Governing outcome (aligned to SCQA Answer / experiment)  
- Narrative class carried forward (`decision-ready` | `hypothesis`)

### B. PRD

1. **Users / personas** — who uses or is affected (roles, not tech actors only).  
2. **Goals** — what users/stakeholders need to achieve.  
3. **Success metrics** — measurable; mark baselines known vs unknown.  
4. **In scope (this version)** — numbered capabilities at product level (not endpoint lists).  
5. **Out of scope (this version)** — explicit exclusions (estimation load-bearing; later prompts must not silently pull these in).  
6. **Constraints & non-goals** — from evidence (compliance, platforms, timeboxes).  
7. **Open questions** — what must be resolved before Feature Specs harden.

### C. Spec hygiene

- **One question this file answers:** “What problem are we solving?”  
- Do **not** include: workflows, API shapes, DB schemas, UI wireframes, folder trees.  
- Write **values, not adjectives** for any metric you can already state; otherwise mark Unknown.

### Lean / DMAIC lens (spine — thin)

**DMAIC focus this stage:** **Define** (scope of improvement) + **Measure** targets.

In `dmaic_lens.md` (short), record:

1. Which in-scope capabilities are meant to remove waste vs add capability?  
2. Which out-of-scope exclusions prevent overproduction / extra processing?  
3. Success metrics → DMAIC Measure list (baseline known/unknown).  
4. Any scope item that would create token/model/human-review waste if built too early?

---

## Exit criteria (handoff to Prompt 04)

- [ ] Vision + PRD exist and cite Prompt 02.  
- [ ] In-scope and out-of-scope are both explicit.  
- [ ] Success metrics are listed (with known/unknown baselines).  
- [ ] No APIs, data models, or architecture invented here.  
- [ ] If `hypothesis`: PRD labeled provisional; success metrics may be experiment KPIs.  
- [ ] `dmaic_lens.md` is complete (feeds Prompt 09).

---

## Constraints

- Do not design features in flow detail (that is Prompt 05).  
- Do not draw C4 or choose vendors unless evidence forces a hard constraint (then note for ADR).  
- Do not run full Prompt 09 here.  
- Keep the document short enough to review in one sitting.

---

## Output

Write under `participant-outputs-v2/03-prd/` **and mirror** to `specs/product/`:

- `vision.md`
- `prd.md`
- `scope_in_out.md`
- `dmaic_lens.md`
