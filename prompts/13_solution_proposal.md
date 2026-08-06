# Prompt 13 — Final Solution Proposal (Synthesis)

**Lifecycle stage:** Synthesis / sponsor handoff  
**Framework derived:** Executive packaging of FDE frameworks + Spec-Driven Development artifacts  
**Core question:** What should leaders understand, fund, and decide next?  
**Prerequisites:** Prompts 01–12 outputs, especially Assurance.  
**Primary output type:** Combined executive and engineering proposal.

---

## Intent

Synthesize the toolkit into one proposal: **SCQA story**, **PRD scope**, **feature/AC summary**, **DDD ownership**, **C4 architecture**, **ADR trade-offs**, **technical contracts**, **Lean/DMAIC path**, **what was built**, and **what Assurance proved**. Clearly separate prototype/PoC from production-grade delivery.

If the engagement ran in **hypothesis / provisional / scarce-data** mode, the proposal must lead with **what is unknown**, the **evidence acquisition plan**, and **sponsor data-access decisions** — not only the solution vision.

---

## Entry criteria

- Evaluation report and residual risks exist.
- PoC vs production gaps are listed.
- Framing mode / artifact status history is known (`decision-ready` vs `hypothesis`; stable vs provisional).
- Open ADR statuses and sponsor-needed decisions are known.

---

## Produce

Include:

1. **Evidence confidence summary** — framing mode, sufficiency scores snapshot, and whether artifacts are stable or provisional.  
2. **Problem statement** — SCQA Situation/Complication compressed for sponsors; label assumption-heavy parts.  
3. **Governing answer** — Minto top of pyramid; MECE reasons summarized (`decision-ready` recommendation or governing experiment).  
4. **PRD scope** — in-scope / out-of-scope for this version.  
5. **Target operating workflow** — how the solution fits day-to-day operations (incl. HITL).  
6. **Measurable outcomes** — from SCQA/PRD + DMAIC Measure + AC results; call out unknown baselines.  
7. **Domain ownership** — bounded contexts, owners, decision rights.  
8. **Feature & AC summary** — what was specified vs verified.  
9. **Target architecture** — C4 views and how they meet requirements (mark provisional).  
10. **Key decisions and trade-offs** — consequential ADRs and what was sacrificed.  
11. **Technical contract highlights** — APIs/data/NFR/error posture.  
12. **Safety, security, privacy, and governance controls** — non-functional guarantees.  
13. **Data and integration strategy** — sources, flows, anti-corruption, prohibited writes.  
14. **Evidence acquisition & data-access plan** — what must be obtained next, from whom, and what it unblocks.  
15. **Lean summary** — top wastes removed or still open; Control approach; Measure-first items.  
16. **Human adoption and operating model** — how people will work differently.  
17. **Phased roadmap** — incremental milestones; front-load discovery/instrumentation when scarce.  
18. **Delivery assumptions** — what must remain true.  
19. **Residual risks** — accepted or deferred (include `inconclusive (data scarcity)` areas).  
20. **Sponsor decisions required** — especially **data access**, SME time, SoT authority, scope changes, and go/no-go on production path.

### Lean / DMAIC lens (spine — thin)

**DMAIC focus this stage:** executive **Control** story — what improved, what remains, what to fund next.

In `dmaic_lens.md` (short) *or* as a labeled subsection in the proposal, record:

1. Top wastes removed vs still open (from Prompt 09 + `control_lens_rollup` / 12).  
2. Measure baselines still Unknown that sponsors must unlock.  
3. Control owners after handover (from `production_readiness.md`).  
4. Next DMAIC loop recommendation (do not imply continuous improvement without owners).  
5. Pilot learnings (Prompt 11) that imply domain/feature/contract changes.

### Explicit labeling

- **Demonstrated in PoC / prototype** vs **Required for production**.  
- **Known / Assumed / Unknown** for material claims.  
- **DDD stage 16 handover** — owners and production blockers from Prompt 12.  
- **Framework & spec artifacts** appendix index (paths to Prompts 01–12 outputs; `specs/` / `tasks/` mirrors).

---

## Exit criteria

- [ ] Proposal is consistent with Assurance findings (no overclaiming).  
- [ ] Scarce-data / hypothesis status is visible near the top when applicable.  
- [ ] PoC vs production is unmistakable.  
- [ ] Sponsor decisions (including data access and scope) are actionable.  
- [ ] Lean/DMAIC spine summary is present (wastes, Measure gaps, Control owners, post-build rollup).  
- [ ] Production readiness / handover (DDD stage 16) is explicit.  
- [ ] Readers can navigate back to SCQA, PRD, features, DDD, C4, ADR, technical, Lean, and task artifacts.

---

## Constraints

- Do not introduce major new architecture without flagging a loop back to Prompts 06–08.
- Do not bury residual risk or data scarcity in appendix-only language if it blocks production.
- Do not present hypothesis framing as a committed production decision.
- Keep the governing answer visible near the top (Minto).

---

## Output

Write under `participant-outputs-v2/13-proposal/`:

- `solution_proposal.md`
- `dmaic_lens.md`
