---
name: domain-and-architecture
description: >-
  Applies the domain/architecture spine: Discovery → SCQA → DDD → C4 → ADRs with
  decision-ready/hypothesis modes, architecture review gates, Gen AI boundaries,
  reference architectures, integration smells, and effort/confidence estimation.
  Use when the user asks about SCQA, DDD, C4, ADRs, discovery, estimation, or
  ubiquitous language. PRD, Feature Specs, and Technical Design live in
  spec-driven-delivery.
---

# Domain & Architecture

Portable skill for any repo. Merges architecture teaching depth with engagement gates.

## Enforce this spine (order matters)

```text
Discovery → SCQA → PRD → DDD → Feature Specs → C4 → ADRs (+ architecture review) → Technical Design → …
```

This skill **owns** Discovery, SCQA (shared with `exec-communication`), DDD, C4, and ADR/review.  
**PRD, Feature Specs, and Technical Design** are owned by `spec-driven-delivery` — do not skip them between DDD and C4, or after review.

Do **not** jump to agents/RAG before language, boundaries, and the decision question are clear.  
Do **not** propose target architecture inside Discovery (stage 01) — Anchor/Decode/Commit happen after evidence and Framing, when scoping and architecture stages allow.

## Discovery

Produce / demand:

1. Repository/source-system map (what is actually running — deploy bill & pipeline beat the wiki)  
2. Entities, identifiers, timestamp semantics  
3. Evidence ownership & authority  
4. Gaps/conflicts register  
5. Stakeholder decisions & horizons  
6. Constraints register  
7. Current-state workflow sketch (mark inferred steps as assumptions)  
8. Fact / derivation / **Assumption** / question register  
9. Top investigation hypotheses  

10. **AI FDE input sufficiency** — Strong / Partial / Missing for: Business context · User workflow · Constraints · Evidence · Stakeholder needs  

**Overall framing mode (required):**

- `decision-ready` — Situation/Complication mainly from facts/derivations  
- `hypothesis` — framing must be a testable hypothesis, not a locked decision  

Rule of thumb: if Evidence or User workflow is Missing, or two+ inputs are Missing → `hypothesis` unless a reviewer overrides.

11. **Evidence acquisition backlog** — artifact, owner, which later stage blocked, priority  
12. **Early waste signals** (Lean preview) — DOWNTIME / AI waste names; observed vs hypothesized  

13. **`dmaic_lens.md` (thin — Measure + light Define)** — what can already be measured; Unknown baselines; top 3 early wastes; what stage 09 must Measure before scaling automation  

Outputs: `participant-outputs-v2/01-discovery/` (`evidence_register.md`, `evidence_acquisition_backlog.md`, `early_waste_signals.md`, `dmaic_lens.md`).

Four moves after Framing/PRD when decoding a vague brief: **Discover → Anchor (reference arch) → Decode (bounded scope) → Commit (canvas, estimate, confidence, spikes)**.

For every integration capture: contract, direction/trigger, volume/latency (peak), failure behaviour, owner, auditability.

Draw integrations as a **context diagram, not a component diagram** — one box for your system, one per external party, one
labelled arrow per contract. *If an arrow has no named owner, it is not an integration — it is a risk with an optimistic label.*

### Integration smells that reprice a project

- "It's just a CSV drop" — an unversioned contract, no owner, no schema check.  
- "We have an API" — undocumented, unversioned, rate-limited at a number nobody knows.  
- "The nightly batch" — your real-time AI feature just inherited a 24-hour freshness floor.  
- "IT will give us access" — an unscheduled dependency on a team with its own backlog.  
- "We'll just read the database directly" — coupling to someone else's schema; breaks on their next release.

**Integration discovery is estimate discovery.** The AI work is rarely what moves the date; procurement, licensing and
access do. Also run a scoped **technical-debt audit** — not the estate's health, only: which debt stands between *this
brief* and production?

## Reference architectures — borrowed judgement, used well

Read three sources **in this order**:

1. **Vendor-neutral agent patterns** — a *complexity brake*; mostly tells you to build less than you planned.  
2. **Named baseline architectures** — a *starting topology*; then document every deliberate departure as an ADR.  
3. **A well-architected framework** — a *question bank and review gate*; it tells you what you forgot, not what to build.

Reversing that order produces an over-engineered system that passes a checklist.

### How they go wrong

**Cargo-culting** (copying the diagram because it is official — you inherited its costs without its reasons) ·
**checklist theatre** (passing every question on paper while the real risk — no ground truth, no owner — is not on the
checklist) · **vendor gravity** (the publisher sells the components; its build-vs-buy default is not neutral).

### Three questions to ask of any reference architecture

1. **What context did this assume?** Scale, regulation, team size, residency. If yours differs on any, the diagram is a
   hypothesis, not an answer.  
2. **Which parts are load-bearing?** Separate the structure from the shopping list.  
3. **What would I have to believe** for this to be right *here*? Write those beliefs down — they are your assumptions
   register and your spike list.

**The defendable sentence:** "We started from *&lt;named baseline&gt;*. We kept *&lt;layers&gt;* as published. We departed on *&lt;X&gt;*
because *&lt;constraint&gt;*, accepting *&lt;consequence&gt;*. We would revisit if *&lt;trigger&gt;*." If you can say that, no architecture
review can corner you.

## Estimating effort & confidence

T-shirt sizing is coarse on purpose (S = known pattern, known systems, one integration, ground truth exists). State the
**uncertainty cone** — the range *and the date it narrows* — and attach **spikes** to the assumptions that would move it.
**An estimate without a stated confidence is not an estimate — it is a hostage.**

## SCQA (Frame — stage 02)

Carry Discovery **narrative class** (`decision-ready` | `hypothesis`) at the top of the narrative.

- **Situation** — normal operations & desired outcomes; label assumptions  
- **Complication** — compound across operational/technical/people/resource/commercial/security/data  
- **Question** — one bounded decision/engineering question  
- Define user, decision horizon, evidence boundary, **authority boundary**  
- **Answer** — capability-level, no premature architecture; if `hypothesis`: recommended experiment + falsifiers + acquisition needs  
- Measurable outcomes + explicit exclusions  
- Minto pyramid: governing answer → MECE points (3–7) → support  

**Framing handoff pack:** decision question for PRD/DDD · success metrics for DMAIC Measure/Control · open questions blocking design · whether later artifacts must be **provisional**.

**`dmaic_lens.md` (Define):** waste in Complication; Measure targets known vs Unknown; what must not be automated yet; how Answer reduces waste.

Output: `participant-outputs-v2/02-scqa/` (`scqa_minto_decision_narrative.md`, `dmaic_lens.md`) — also see `exec-communication`.

## DDD — non-negotiables

- **Artifact status:** `stable` | `provisional` (provisional under `hypothesis` or open SoT/language)  
- Prefer **rules + HITL** over autonomous AI when provisional  
- Business-domain language first; Gen AI boundaries are designed **after** language/contexts exist, still before C4 boxes  
- Advisory only; prohibited actions never implied  
- Human authority always named  
- Evidence & provenance first-class (source vs receipt time, conflicts, missing ≠ normal)  
- Priority/safety rules never overruled by commercial urgency  
- Domain ≠ source-system or table names  
- Required contexts include **Evidence & Provenance** and **Decision Authority & Accountability**  
- No giant catch-all "operations" context — merge or split only with a stated business reason  
- **Do not resolve the operational exceptions** in the case; carry them as domain gaps, exception states and invariants  
- Do not assume the most commercially visible problem is the most important one  
- Stages: framing → subdomain map → ubiquitous language → bounded contexts → context map (defend each relationship) → event storming → domain model, invariants & policies → **Gen AI boundary design** (rules vs AI, RAG from DDD artefacts, agent authority/stops, HITL, audit, eval cases in DDD vocabulary) → minimum governed workflow  
- **Stage 15 (pilot/refine)** is **executed** in Deliver as `pilot_learnings.md`  
- **Stage 16 (production readiness)** is **executed** in Assurance/Proposal as `production_readiness.md`  
- Link open SoT/language items to Discovery acquisition backlog to de-provisionalize  

**`dmaic_lens.md` (Analyze):** invariants vs Defects; HITL vs review waste; RAG/agent token/context waste; ambiguities → Extra processing/Motion.

Outputs: `participant-outputs-v2/04-ddd/` (`domain_model.md`, `context_map.md`, `gen_ai_boundaries.md`, `dmaic_lens.md`).  

### Ubiquitous language

Define the language **as used in this case**, not a universal domain dictionary. Capture core terms, subdomain terms,
status/exception/approval terms, terms interpreted differently by different roles or source systems, and terms that
**must not be used loosely** because they imply safety, authority, release, fitness or completion.

Emit as a table, one row per term: `term · definition_in_this_case · bounded_context · owner_role · valid_context ·
ambiguity_risk · must_not_be_used_loosely`.

### Bounded-context canvas — the fields that make a boundary defensible

One canvas per context: business purpose · primary human participants · owned language · owned information/statuses ·
**decisions owned** · **decisions *not* owned** · upstream inputs · downstream outputs · policies/rules it must respect ·
anti-corruption/translation needs · known gaps touching it · audit/evidence needs · **safety-authority risk if the
boundary is misunderstood**.

The two fields teams skip — *decisions not owned* and *risk if misunderstood* — are the ones that prevent a context from
silently absorbing another's authority.

### Context map — name the relationship type

Use DDD relationship language where it fits: **partnership · shared kernel · published language · anti-corruption layer**,
plus upstream/downstream direction. Identify shared-kernel terms, the published handoff vocabulary, and the boundaries
where one context's (or a source system's) language would distort another's meaning.

**Defend the map:** every relationship carries a one-line rationale — why this type, why this direction, why this boundary
rather than merging or splitting — and names the translation, safety or authority risk the boundary protects against.

### Event-storming board

One row per domain event: **domain event · triggering command/activity · primary human actor · bounded context ·
governing policy/rule · evidence source · failure/exception condition · audit need.** Keep exceptions unresolved.

### Domain model, invariant and policy registers

Classify candidates into **entities · value objects · aggregate roots · policies/rules · evidence/audit artifacts ·
external references**, then keep two registers with stable IDs — downstream ADRs trace their guardrails to these:

- **Invariant register (`INV-*`)** — invariant ID · statement · aggregate/context · source rule or case fact ·
  human owner · failure risk · audit evidence required.
- **Policy register (`POL-*`)** — policy ID · "when X then Y must happen" · triggering domain event · bounded context ·
  accountable human owner · source rule or case fact · audit evidence required.

### DDD quality gate

- [ ] Every context has distinct language and a named human owner; none silently owns another's decision  
- [ ] Every invariant and policy traces to a case fact or stated rule, and names the human owner of the decision it guards  
- [ ] Every context-map relationship carries its defence and the risk its boundary protects  
- [ ] No rule permits the priority/safety rule to be violated  
- [ ] Provenance modelled explicitly (source id, source vs receipt time, timezone, conflicts, missing data)  
- [ ] No architecture, source-system or dataset names used as domain concepts  
- [ ] Every operational exception appears as a gap, exception state or invariant — none resolved  
- [ ] Language table and context map are consistent with the canvases  

## C4

- People, external systems, system boundary, deployable containers, critical workflow components  
- Data/trust/privacy/authority/connectivity boundaries; degraded mode  
- Map containers ↔ bounded contexts; note which **FR-IDs** land in which container/component  
- Show **PROHIBITED** write paths explicitly  
- **Gen AI runtime sketch** — where retrieval, model calls, tools, and human review sit (structure only; justify in ADRs)  
- On platform-scale work go to **level 4 (code-level contracts)**  

**`dmaic_lens.md`:** Transportation/Integration waste; Waiting bottlenecks; Observability/Context waste; Overproduction vs minimum governed workflow.

Outputs: `participant-outputs-v2/06-c4/` (`c4_context.md`, `c4_containers.md`, `c4_components.md`, `boundary_and_degraded_mode.md`, `adr_candidates.md`, `dmaic_lens.md`, optional `c4_code.md`).

### Diagram conventions that keep a view reviewable

- Each view is its own self-contained fenced `plantuml` block: `@startuml` … `@enduml`.  
- Plain PlantUML shapes only — `rectangle`, `package`, `boundary`, `cloud`, `database` — each carrying a stereotype:
  `<<Person>>`, `<<System>>`, `<<Container>>`, `<<External>>`. **No `!include` and no C4-PlantUML macros** (`Person()`,
  `System()`, `Rel()`, …) — nothing outside the diagram text should need fetching to render it.  
- Relationships are plain labelled arrows (`-->`). A relationship the system is **forbidden** to have is drawn
  `-[#red,dashed]->` with the label starting `PROHIBITED:`.  
- **Every person, system and container named in the prose must appear as a labelled shape in at least one diagram** —
  no architecture element may exist only in text.

## ADRs

Run two scopes deliberately. A **prototype** set (≥5) covers the business/domain forks: entity–process–event identity;
source-event vs report vs receipt time; canonical model and per-source translation (ACL); rules, analytics and
explainability; persistence and evidence snapshots; online/intermittent/offline operation; role and authority
enforcement; decision audit; external integrations; deployment and observability.

A **production** set (≥8) keeps all of those and adds: deploy topology and runtime (environments, IaC); live ingestion
(delivery semantics, idempotency, back-pressure, schema evolution, replay/backfill — **read-only toward every source
system**); scalability and performance budgets; availability, resilience and DR; security and an explicit threat model
for the integration surface; data protection, retention and residency; observability and operations; release and change
management; cost and sustainability.

**At production scale the non-negotiables are strengthened, never relaxed** — the system stays advisory, authority stays
visible, evidence discipline holds. Where a production choice differs from the prototype, note the **migration path**.

### Required content per ADR

- **Status / Date / Owners**, and the related requirements, bounded contexts and C4 elements  
- **Evidence basis** — fact / derivation / assumption (tie to Discovery)  
- **Context** and **decision drivers**, including the relevant NFRs  
- **Options considered** — ≥3 realistic alternatives, each with its trade-off stated  
- **Decision** and **rationale**  
- **Non-functional targets** — concrete and measurable: p95/p99 latency, availability %, RPO/RTO, ingestion lag,
  maximum data staleness surfaced to users  
- **Security & privacy impact** — threats addressed, data classes touched, controls applied  
- **Operational impact** — deploy/rollback story, monitoring signals, alert conditions, runbook note  
- **Consequences** — positive, negative, and **risks introduced**  
- **Guardrails** — traced to the `INV-*` / `POL-*` registers; assert that prohibited write paths are absent
  *by construction*  
- **Validation** — tests **and** production checks: load, chaos, failover, security, an SLO monitor, and an
  architecture/dependency check proving no source-write path exists  
- **Revisit trigger** — quantified where possible ("when ingestion lag p95 > N min", "when a new source family onboards")

`decision_index.md` must list which ADRs are blocked on the evidence acquisition backlog.

**`dmaic_lens.md`:** which ADRs prevent named waste; Waiting/Human-review/Token risk; Validation+revisit as Control; review open issues as waste risks.

### ADR quality gate

- [ ] Every listed decision area is covered by at least one ADR  
- [ ] Every ADR states measurable NFRs plus security/privacy and operational impact  
- [ ] Every guardrail traces to an `INV-*` or `POL-*`  
- [ ] Every prohibited write path is absent by construction **and asserted by a test**  
- [ ] Every revisit trigger is quantified  
- [ ] ADRs are internally consistent with the C4 views and with each other  

### Architecture review / defense (required gate before Technical Design)

After key ADRs are recorded, produce `architecture_review.md` under `participant-outputs-v2/07-adrs/` (mirror `specs/architecture/`):

| Field | Values |
|---|---|
| Review status | `pass` \| `conditional` \| `fail` |
| Defensibility | C4↔DDD↔FRs; ADRs for trade-offs; trust/HITL/prohibited writes; out-of-scope not smuggled |
| Open issues | blocker vs residual |
| Go-forward | Technical Design only if `pass` or `conditional`; `fail` → loop C4/ADR |

Under `hypothesis` / `provisional`, prefer `conditional` unless evidence supports `pass`.  
Keep material ADRs **`proposed`** until evidence supports `accepted`. Also produce `decision_index.md`.

C4 outputs under `participant-outputs-v2/06-c4/` (see C4 section). ADR/review outputs under `participant-outputs-v2/07-adrs/`: `ADR-*.md`, `decision_index.md`, `architecture_review.md`, `dmaic_lens.md` (mirror `specs/architecture/`).

### At platform scale

Eight is a floor for a system, not a ceiling for a platform — an enterprise GenAI platform can justify a **40+ ADR register
plus a trade-off matrix**, including serving-runtime decisions ("track prefill and decode separately", "paged KV cache")
held to the same template as the domain ones. Keep the register as one navigable artifact, tag each ADR with its **C4
level**, and give every entry a **rollback** line. Sequence them against a **phased roadmap** where later phases do not
force a redesign of earlier ones.

## Workflow

1. Restate the decision question (SCQA).  
2. Run discovery/inventory if brownfield; map integrations as contracts with owners.  
3. Build DDD artifacts before C4.  
4. Anchor to a named baseline; answer the three questions before adopting it.  
5. Draw C4; forbid write paths visually.  
6. Freeze forks in ADRs (with departures from the baseline); assemble SDD/PRD.  
7. Commit with canvas, estimate, stated confidence, and spike list.

## Do / Don’t

- **Do:** progressive ambiguity reduction; defend context-map relationships; name an owner per arrow; state confidence with every estimate  
- **Don’t:** architecture-as-domain; cargo-cult a vendor diagram; auto-approve material decisions; skip “not in scope”  
