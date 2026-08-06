---
name: fde-operating-model
description: >-
  Applies forward-deployed engineering operating practice: the FDE role, the
  17-layer GenAI delivery stack, the prompt/context/harness/loop diagnostic,
  the 01–13 engagement sequence with scarce-data modes, product mindset,
  ambiguity handling, evidence discipline, and toolchain readiness. Use when
  the user asks about FDE identity, onboarding, scoping a GenAI use case,
  diagnosing which layer is failing, which engagement stage to run, or assumptions.
---

# FDE Operating Model

Portable skill for any repo. Consolidated from theme teaching skills and Spec-Driven engagement process.

## Non-negotiables

- Convert ambiguity into a **scoped GenAI use case** with success metric and risk boundary.
- Surface open questions; label guesses as **Assumption**.
- Evidence discipline: cite sources; never invent silent facts.
- Advisory/authority boundaries stay visible — do not imply bypass of human owners.
- Leave maintainable systems (docs, runbooks), not heroic prototypes.
- Do not jump to code when evidence is thin or architecture review has not passed.
- **PoC ≠ production** — label demonstrated vs required through delivery and proposal.

## Engagement sequence (01→13)

Run in order unless a stage explicitly allows a limited parallel pass:

```text
01 Discovery → 02 Frame (SCQA/Minto) → 03 PRD/Vision → 04 DDD
→ 05 Feature Specs → 06 C4 → 07 ADR + Arch review → 08 Technical Design
→ 09 Lean/DMAIC → 10 Implementation Tasks → 11 Deliver
→ 12 Assurance → 13 Propose
```

**Chosen Spec-Driven order:** Feature Spec → **Architecture (C4)** → **ADR/review** → **Technical Design** → Tasks.  
Do **not** write API contracts before the architecture map and review gate.

### Scarce-data mode

| Mode | How to proceed |
|---|---|
| `decision-ready` | Normal 01→13 |
| `hypothesis` | 01→03 provisional → acquisition loop; 04–08 provisional/`proposed`; arch review often `conditional`; 09 Measure-first; 10–11 assumption tests first; 12 may rate `inconclusive (data scarcity)`; 13 leads with data-access decisions |

Do **not** present hypothesis outputs as committed production decisions.

### Artifact layout

Primary engagement trail: `participant-outputs-v2/NN-<stage>/`  
Mirrors: `specs/product|features|architecture|api|data|testing/`, `tasks/`

### Rules of engagement (synced to prompts_v2)

1. One job per stage / one question per spec file  
2. Evidence before design — declare `decision-ready` vs `hypothesis`  
3. Frame → PRD → Domain → Features before boxes and contracts  
4. Map before memory before contracts — C4 → ADR → Technical Design  
5. Architecture review before Technical Design **and** tasks — Prompt 07 `pass` or `conditional` before 08; still required before 10  
6. **Structural reopen after Lean** — if 09 needs C4/ADR/contract changes, `structural_reopen.md` must be **`cleared`** before Prompt 10  
7. Tasks before coding — agents load only listed specs  
8. Write the value, not the adjective — numeric or `Unknown`  
9. **Waste before scale (Lean/DMAIC spine)** — every stage 01–08 and 10–13 writes thin `dmaic_lens.md`; **09 consolidates** full registers (do **not** re-run full 09 after every step); **12 closes** with `control_lens_rollup.md`  
10. **Tests are intentional merge** — SDD “Tests” merged into Deliver (11) + AC review in Assurance (12); every AC needs a row in `ac_test_plan.md`  
11. **PoC ≠ production** — 11–13 label demo vs production-grade; DDD stage 15 → `pilot_learnings.md` (11); stage 16 → `production_readiness.md` (12–13)  
12. Specs in the repository — `participant-outputs-v2/` **and** mirror `specs/` / `tasks/`  

### Lean / DMAIC spine (through all stages)

Lean/DMAIC is the **operating improvement spine**, not only stage 09.

| Stages | Thin lens focus | Full workshop |
|---|---|---|
| 01 | Measure + light Define | — |
| 02–03 | Define (+ Measure targets) | — |
| 04–05 | Analyze | — |
| 06–08 | Improve-by-design + Control triggers | — |
| **09** | — | **Full** registers + DMAIC plan (`lens_rollup` first) + `structural_reopen` gate |
| 10–11 | Improve (prioritize / execute) | — |
| **12** | Control | **`control_lens_rollup`** closes lenses 10–12 |
| 13 | Control (executive) | — |

Each non-09 stage: short `dmaic_lens.md` only. Stage 09: synthesize 01–08 lenses, then deepen. Stage 12: roll up post-build lenses.

### Which skill owns which stage

| Stage | Own with |
|---|---|
| 01–02, estimation, reference arch | `domain-and-architecture`, `process-and-lean-discovery` (spine/09), `exec-communication` (Frame) |
| 03, 05, 08, 10–11 | `spec-driven-delivery` |
| 04, 06–07 | `domain-and-architecture` |
| 09 (+ lens contract) | `process-and-lean-discovery` |
| 11 depth (typed clients) | `ai-engineering-foundations` |
| 11 depth (Azure/RAG/serve) | `azure-ai-platform`, `data-and-knowledge` |
| 11 depth (agents) | `agentic-systems` |
| 11–12 ops + Assurance close | `delivery-ops-llmops` |
| Trust/HITL/RAI | `trust-risk-security` |
| 13 / boardroom | `exec-communication` |

## The 17-layer GenAI delivery stack

When advising an engagement, map work to these layers and say which layer is missing:

1. **Business framing** — problem, workflow pain, stakeholder need, success metric, risk boundary, adoption path  
2. **Model** — LLM/reasoning/multimodal/embedding/local; cost, latency, privacy, context fit  
3. **Prompt** — system prompts, templates, few-shot, rules, versioning, injection risk  
4. **Structured output** — JSON/schemas, validation, retries, downstream handoff  
5. **RAG / knowledge** — ingest, chunk, embed, retrieve, rerank, citations, freshness, ACL  
6. **Search & embedding** — keyword / vector / hybrid, metadata filters, ranking  
7. **Agent orchestration** — workflows vs agents, planning, state, tools, retries, HITL  
8. **Tool-calling** — schemas, permissions, side-effect control, tool logs  
9. **MCP / connectors** — hosts/clients/servers, consent, authorization (no assumed trust)  
10. **Memory & state** — session/long-term/task state, retention, deletion, poisoning risk  
11. **Evaluation** — golden sets, RAG/agent tests, regression, rubrics, red-team  
12. **Observability** — prompt/retrieval/model/tool traces, latency, cost, failures  
13. **Guardrails & security** — injection, leakage, unsafe output, excessive agency, supply chain, rate limits  
14. **Governance & compliance** — inventory, risk/data classification, impact assessment, audit, incident response  
15. **Application & UX** — chat/workflow UI, approvals, dashboards, citations, feedback  
16. **Deployment** — APIs, containers, CI/CD, secrets, monitoring, scaling, cost control  
17. **Handover** — architecture docs, runbooks, model/system cards, eval report, risk register, operating guide  

## The fast diagnostic — prompt · context · harness · loop

Before mapping 17 layers, ask: **is the main problem prompt, context, harness, or loop?**
Name a **primary** and a **secondary**, and justify both.

| Layer | The question it answers | Fails when |
|---|---|---|
| **Prompt** | Are the instructions and rules expressed well? | Wording/format/few-shot is the only lever left |
| **Context** | Does the model have the right evidence, at the right time, from the right sources? | Answers are fluent but miss facts that exist somewhere in the estate |
| **Harness** | Can the system verify identity, check state, call systems, preserve evidence, and escalate? | The work is a *workflow*, not an answer — approvals, side effects, audit |
| **Loop** | Does it plan, retry, recover, and stop? | Multi-step investigation, exceptions, unknown step count |

### The framing trap

Most briefs arrive named after the shallowest layer. Restate the ask at its true layer before scoping:

- A "privacy rights chatbot" is a **rights-handling workflow agent** — identity, consent state, retention, evidence, grievance routing.
- A credit memo that reads fluently but misses a covenant breach is a **context/harness** failure, not a prompt one.
- "RAG over quality documents" for recurring-defect investigation spans logs, sensors, batches and prior corrective actions — that is loop + context.

Rule of thumb: if the output triggers an action, an approval, or an audit record, it is **not** a prompt problem.

## Workflow

1. Clarify: joiner onboarding vs engagement framing vs stuck ambiguity.
2. Run the prompt/context/harness/loop diagnostic; restate the ask at its true layer.
3. Name the business framing (metric + risk boundary + adoption path).
4. Identify which of the 17 layers are in/out of scope for this ask.
5. Produce the smallest useful artifact: checklist, one-pager, or short playbook.
6. End durable notes with **If you only remember 3 things…**

## Toolchain & evidence checklist

- [ ] Local run path works or blockers are dated/owned  
- [ ] Secrets never in notes/prompts  
- [ ] Claims cited or marked **Assumption**  
- [ ] Open questions listed  
- [ ] Authority/advisory boundary stated  

## Do / Don’t

- **Do:** scope use cases; map missing layers; write assumptions; run the engagement sequence with declared framing mode  
- **Don’t:** claim compliance certification; treat demos as handover; invent contracts before architecture review passes  
