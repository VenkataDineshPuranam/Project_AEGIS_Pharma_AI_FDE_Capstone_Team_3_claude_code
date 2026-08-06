---
name: delivery-ops-llmops
description: >-
  Applies LLMOps and Assurance: consolidation buffer, eval harness, brownfield
  eval framework, telemetry, FinOps, CI eval gates, rollback, plus artifact/AC
  fidelity review with inconclusive-data-scarcity ratings and
  go/conditional-go/no-go. Use when the user asks about LLMOps, evals,
  assurance, graders, telemetry, cost, CI gates, rollback, or production
  readiness.
---

# Delivery Ops / LLMOps

Portable skill for any repo. Merges LLMOps teaching depth with engagement Assurance (stage 12).

## Thesis

Valid output ≠ trustworthy output. Operating discipline ties **build + eval + telemetry + cost + rollback** into one system.  
**Assurance** (artifact/AC fidelity) and **LLMOps harness** are complementary — the harness does not replace auditing against SCQA/PRD/DDD/C4/ADR/contracts/ACs.

## Consolidation & buffer

- Cold starts on launch: new nodes take minutes; **pause/overprovision pods** hold warm capacity.  
- Checklist: bin-pack workloads, right-size buffer, pre-pull images, stabilize before go-live.

## Eval harness

- Golden sets · regression tests · **LLM-as-judge** · multi-evaluator agreement  
- **Cohen's Kappa** (and fit-for-purpose metrics) · drift detection — kappa doubles as a drift alarm  
- The harness answers: can you trust the pipeline’s judgment?

## Telemetry

- Application Insights (or equivalent): custom events, **token counts**, latency **p99**, full prompt/retrieval/tool traces where allowed.  
- LLM telemetry is not ordinary APM — the failure modes are semantic, not just latency and error rate.

## Cost discipline

- Caching · **model tiering / routing** · batching · **PTU vs PAYG** decision with evidence.  
- Batch API pricing earns a discount only on work that tolerates delay — compute the **break-even** before promising it.

## Model routing — a quality *and* margin lever

Route by **task, risk, latency, cost, and sensitivity** — not one model for everything.

- Maintain a **model–task map**: which model serves support, research, coding, ops, docs; reserve frontier reasoning for
  genuine judgment and send repetitive operations to smaller models.
- The router's decision is part of the audit trail — log which model answered and why.
- Routing is a first-class architectural component, not a config toggle; decide it in an ADR with a fallback path.

## Platform choice

- **Container Apps** for serverless containers, scale-to-zero, fast ship; **AKS** when you need full K8s API/CNI/DaemonSets/sustained util.  
- Today’s default for agents: Container Apps; AKS is graduation, not habit.

## Package & scale

- Slim multi-stage images, non-root, pin deps, bind `0.0.0.0:$PORT`, one process, stateless app (state in a document store).  
- Container registry + KEDA scale rules.

## CI/CD

- GitHub Actions (or equivalent) with **blue/green revisions** + **eval gate that blocks bad deploys**.

## LLMOps ops

- Prompt versioning · model-card automation · one-command rollback.  
- Rehearse the **02:00 rollback runbook** before SEV-1 (bad prompt in prod).

## Integrated operating picture

User → agent on Container Apps → search/retrieval → model endpoint → grounded answer  
Cross-cutting: managed identity · durable checkpoints · blue/green · OpenTelemetry/`gen_ai.*` spans · eval gate on golden set · 30-min load test.

## Designing evals for an existing system

Seven components, offline-first, built *around* a brownfield repo rather than inside it:

| Component | Role |
|---|---|
| **System under test** | The existing app/workflows — unmodified while you baseline |
| **Datasets** | The questions and the difficult situations |
| **Adapter** | The connector to the system; captures input, output, evidence, tools called, retries, errors, approvals, side effects, latency |
| **Runner** | Orchestrates execution — the examiner |
| **Graders** | The answer-checking mechanism — the judges |
| **Policies** | Automatic failure rules and release gates |
| **Reports** | `summary.json`, `detailed_results.jsonl`, `scorecard.csv`, `failed_cases.json`, `final_evaluation_report.md` |

### Design the eval set across case types

Normal · **edge** · **adversarial** · **metamorphic** · **outage** — plus required facts, required behaviours,
**prohibited behaviours**, human escalation, and hard-gate status.

### Grade more than text quality

Schema · required facts · evidence · **prohibited actions** · **authority** · security · **temporal and unit correctness** ·
**trajectory** · latency. Write **positive and negative unit tests for every grader** — an unvalidated judge is not evidence.

### Sequence

Understand the repo (workflows, inputs, data sources, tools/APIs, rules, existing tests, failure handling, human approval
points) → design coverage → scaffold `datasets/ adapters/ graders/ policies/ reports/ runner.py` → build the adapter →
implement deterministic graders → **run the full suite on the unmodified app to establish a baseline before any changes.**

## Agentic-coding FinOps

Token spend is only half the picture; track engineering efficiency too:

| Signal | Reveals |
|---|---|
| Chat sessions used | Fragmented or repeated work |
| Files attached | Context scope |
| Agent iterations | Rework |
| Terminal commands | Exploration overhead |
| Files modified | Over-broad changes |
| Failed attempts | Wasted effort |
| Full-suite runs | Unnecessary validation cost |
| Task outcome | Connects usage to value |

Usage metrics + efficiency signals + outcome tracking = defensible FinOps decisions. Report **cost per successful outcome**,
never cost per token alone.

## Minimum controls checklist

- [ ] Golden-set eval in CI (fail closed)  
- [ ] Baseline captured on the unmodified system before changes  
- [ ] Graders unit-tested (positive and negative cases)  
- [ ] Policies encode hard gates, not advisory warnings  
- [ ] Token + p99 (+ cost) telemetry  
- [ ] Model–task routing map recorded, with fallback  
- [ ] Blue/green + rehearsed rollback  
- [ ] Prompt/model versions recorded  
- [ ] Budget vs actual reviewed; PTU/PAYG justified  
- [ ] Load test cleared before claiming ready  

## Assurance & Control (stage 12)

Audit the built system against SCQA/PRD outcomes, feature ACs/BRs, technical contracts, DDD boundaries, C4, ADRs, and Lean Control.

### Assess

Design fidelity · Data & authority · AI/decision quality (incl. FP/FN examples, HITL exercised) · Operability (degraded mode, NFRs) · Control & residual risk  

### Ratings

`pass` | `fail` | `partial` | **`inconclusive (data scarcity)`**

Use `inconclusive (data scarcity)` when verification was impossible due to missing evidence/baselines/environments — **not** when a test failed. Never treat inconclusive as pass.

**Recommendation triad** (required in the evaluation report): **go** / **conditional-go** / **no-go**, stated separately for **demo** vs **production** path.

**Production go is disallowed** while material areas remain inconclusive unless sponsors explicitly accept that residual risk.

### Produce

`participant-outputs-v2/12-evaluation/`:

- `evaluation_report.md` — ratings per area / material AC; sampling notes; **go / conditional-go / no-go** for demo vs production  
- **`control_lens_rollup.md`** — table of `dmaic_lens.md` from Prompts **10, 11, 12** (+ link to Prompt 09 Control); Measure met/missed/inconclusive; wastes still open; next Discover/Frame loop; Control owners for handover  
- **`production_readiness.md`** (DDD stage 16) — production-ready vs PoC; domain/ops/support owners; open ADRs/ambiguities/risks; handover checklist  
- `dmaic_lens.md` (Control focus)  
- Optional: `control_plan.md`, `fp_fn_examples.md`, `ac_results.md`  

### Exit to Proposal

- Claims classified; PoC vs production evidence-based  
- Go / conditional-go / no-go stated for demo vs production  
- Residual risks and sponsor decisions explicit  
- `control_lens_rollup.md` consolidates lenses 10–12  
- `production_readiness.md` covers DDD stage 16 handover  

## Do / Don’t

- **Do:** gate deploys on eval; baseline before changing; test the graders; rehearse rollback; measure p99/tokens/cost; run Assurance against prior artifacts; close Lean spine with `control_lens_rollup`  
- **Don’t:** warn-only forever; trust an unvalidated judge; treat inconclusive scarcity as pass; skip production readiness handover; one model for every task; ship without warm capacity plan; treat AKS as default without a constraint  
