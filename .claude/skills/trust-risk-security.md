---
name: trust-risk-security
description: >-
  Applies trust/risk/security guidance: Responsible AI governance-by-design,
  ISO/IEC 42001 and EU AI Act awareness, India's DPDP Act and data-principal
  rights workflows, LLM guardrails, and HITL authority boundaries. Use when the
  user asks about RAI, ISO 42001, EU AI Act, DPDP, consent/erasure, OWASP LLM,
  guardrails, or HITL.
---

# Trust, Risk & Security

Portable skill for any repo. Awareness only — not legal advice or certification. Cross-cut every engagement stage; share HITL gates with `agentic-systems` and Assurance with `delivery-ops-llmops`.

## Hard rules

- This skill is **awareness / delivery design**, not a compliance opinion or certificate.  
- Named humans retain material decision authority (**HITL**).  
- Systems remain **advisory** unless an explicit, gated scope says otherwise.  
- Synthetic/demo data in training contexts — never real secrets in prompts/logs.

## ISO/IEC 42001 (AIMS) — what FDEs must internalize

- AI Management System standard (published Dec 2023) — inventory, risk, lifecycle controls, roles, continual improvement.  
- Implementation is organizational and ongoing (surveillance/recertification cycles exist for certified orgs).  
- For delivery: map your system into an **AI inventory**, risk classification, impact assessment hooks, audit logs, and incident response path — even when the client is “not certifying yet.”

## EU AI Act — what FDEs must internalize

- Risk-based regulation (prohibited / GPAI / high-risk / transparency obligations) with phased applicability through 2025–2028.  
- Know whether the use case looks like **prohibited**, **high-risk Annex III-style**, **GPAI**, or lower risk — then escalate to legal/compliance owners.  
- Deployer vs provider obligations differ; do not self-classify silently.  
- Literacy, transparency, post-market monitoring, and documentation show up as delivery constraints.

## India DPDP Act — what FDEs must internalize

- The Act gives **Data Principals** rights including access, correction, completion, updating, and erasure; the 2025 Rules
  operationalize rights handling and response expectations. Consent, notice, and retention obligations sit alongside them.
- A "DPDP chatbot" brief is almost always a **rights-handling workflow agent**: verify identity → inspect consent state
  across every system that holds it (CRM, lead portals, partner uploads, campaign platforms, call-centre notes, consent
  logs) → check retention obligations → trigger downstream workflows → **preserve evidence** → route grievances →
  escalate exceptions. Nominee and opt-out paths are part of scope, not edge cases.
- Delivery consequences: a defensible response record per request, an evidence trail that survives audit, and no silent
  auto-erasure without the named human owner. Escalate legal interpretation — do not self-classify.
- Where a client is subject to multiple regimes, keep an explicit map of which obligation drives which control.

## Governance evidence to collect

A governance assistant is an evidence pipeline, not a Q&A bot. Track: use-case → **risk class** mapping, **model cards**,
**DPIA / AIA documents**, approvals and who granted them, **evaluation results**, **supplier attestations**, and the
**missing-control flags** raised before audit rather than during it.

## Accountability precedent

**Air Canada's chatbot** — the operator was held to what its assistant told a customer. An ungrounded, unaudited, or
over-confident answer is an enterprise liability, not a UX defect. Design the audit trail as though it will be read back
to you.

## Guardrails & security checklist

- [ ] Prompt injection / untrusted content paths identified  
- [ ] Data leakage risks (prompts, logs, traces, retrieval) reviewed  
- [ ] Tool allowlists + schema validation + side-effect control  
- [ ] Excessive agency constrained; high-impact nodes are HITL  
- [ ] Rate limits / cost abuse considered  
- [ ] Supply-chain / plugin trust considered  
- [ ] UI shows uncertainty; humans confirm material acts  

## HITL / authority checklist

- [ ] Written recommend vs decide boundary  
- [ ] Material/conflicted cases require named human approval  
- [ ] Roles from an authority matrix  
- [ ] No silent write to operational/financial systems  

## Governance artefacts to leave behind

AI inventory · risk/data classification · impact assessment (DPIA/AIA) · approval records · evaluation results · supplier attestations · audit logs · incident response · model/system cards (ties to the handover layer).

## Workflow

1. Classify the use-case risk posture at awareness level; list open legal questions.  
2. Design layered guardrails (policy + UX + technical).  
3. Place HITL gates on high-impact edges/tools.  
4. Ensure observability can support audit/incident response.  
5. Document assumptions; never claim “Act compliant” / “42001 certified” from this skill alone.

## Do / Don’t

- **Do:** governance-by-design; escalate classification; keep humans accountable  
- **Don’t:** dump regulatory text as an answer; bypass HITL; treat awareness material as legal sign-off  
