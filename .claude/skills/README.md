# Portable FDE Skills — Final (consolidated)

Flat Markdown skills (one `.md` file per skill) merging theme teaching depth with Spec-Driven engagement process.

**Synced to current `prompts_v2/`** (Lean/DMAIC thin-lens spine, `structural_reopen` gate, `ac_test_plan`, `control_lens_rollup`, DDD stages 15–16, Tests merged into Deliver).

Each file is self-contained and carries no runtime dependency on `deck/`, `prompts_v2/`, or `fde-skill-pack/`. When produce lists diverge, prefer opening the matching `prompts_v2/` file for the full checklist.

## Layout

```text
skills_final/
  README.md
  fde-operating-model.md
  ai-engineering-foundations.md
  azure-ai-platform.md
  domain-and-architecture.md
  agentic-systems.md
  data-and-knowledge.md
  delivery-ops-llmops.md
  process-and-lean-discovery.md
  trust-risk-security.md
  spec-driven-delivery.md
  exec-communication.md
```

## What each skill covers

| File | Scope |
|---|---|
| `fde-operating-model.md` | FDE role, 17-layer stack, diagnostic, **01→13 sequence**, scarce-data, **Lean spine rules**, skill routing |
| `ai-engineering-foundations.md` | Typed LLM contracts, resilient clients, function-calling, ports & adapters |
| `azure-ai-platform.md` | Foundry/AOAI, landing zones, hybrid RAG, WAF, serving runtime |
| `domain-and-architecture.md` | Discovery→SCQA→DDD→C4→ADR/review (PRD/Features/TD via `spec-driven-delivery`) + **dmaic_lens**, Evidence basis, Gen AI runtime, DDD 15/16 handoffs |
| `agentic-systems.md` | Workflows before agents, ACI, multi-agent, chaos, verifiers |
| `data-and-knowledge.md` | Discovery ladder, semantic layers, KGs, question router, provenance, quality gates |
| `delivery-ops-llmops.md` | Eval/CI/FinOps + Assurance + **`control_lens_rollup`** + **`production_readiness`** |
| `process-and-lean-discovery.md` | Thin-lens contract, **`lens_rollup`**, full DMAIC, **`structural_reopen`**, Measure-first |
| `trust-risk-security.md` | RAI, ISO 42001, EU AI Act, DPDP, guardrails, HITL |
| `spec-driven-delivery.md` | Layers (Arch before TD), mirrors, **`traceability_gap_audit`**, **`ac_test_plan`**, Tests-in-Deliver, **`pilot_learnings`** |
| `exec-communication.md` | Frame (+ handoff pack/lens), pods/lenses/30-60-90, Proposal with Lean spine close |

## Cross-links

- `fde-operating-model` triages stage + which skill applies.
- `domain-and-architecture` owns Discovery→ADR/review; `spec-driven-delivery` owns PRD/features/tech/tasks/deliver.
- `process-and-lean-discovery` owns thin-lens contract + stage 09 consolidation; `delivery-ops-llmops` closes Control at 12.
- `exec-communication` owns Frame (02) and Proposal (13).

## Engagement sequence (quick)

```text
01 Discovery → 02 Frame → 03 PRD → 04 DDD → 05 Features → 06 C4 → 07 ADR+Review
→ 08 Technical Design → 09 Lean (lens_rollup + structural_reopen cleared)
→ 10 Tasks (+ ac_test_plan) → 11 Deliver (Coding+Tests + pilot_learnings)
→ 12 Assurance (control_lens_rollup + production_readiness) → 13 Propose
```

## Install

```powershell
New-Item -ItemType Directory -Force ".\.cursor\skills" | Out-Null
Copy-Item -Path ".\skills_final\*.md" -Destination ".\.cursor\skills\" -Force -Exclude README.md
```

Personal:

```powershell
Copy-Item -Path ".\skills_final\*.md" -Destination "$env:USERPROFILE\.cursor\skills\" -Force -Exclude README.md
```

## Format note

Flat Cursor-style skills (one `.md` per skill, YAML `name` + `description`).

## Rules

- Portable: no dependency on a specific repo, client, or training programme folder  
- Mark gaps as **Assumption**  
- No compliance certification claims  
- Architecture before Technical Design; structural reopen must be `cleared` before tasks  
- Thin `dmaic_lens.md` on non-09 stages; full Lean workshop only at 09  
