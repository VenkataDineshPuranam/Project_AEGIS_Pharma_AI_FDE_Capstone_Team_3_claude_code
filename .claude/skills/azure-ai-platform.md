---
name: azure-ai-platform
description: >-
  Applies Azure enterprise AI platform guidance: Microsoft Foundry, Azure OpenAI
  (PTU vs PAYG), landing zones, managed identity/RBAC, Azure AI Search hybrid RAG,
  chunking/embeddings, semantic ranking, the baseline layered AI architecture,
  Well-Architected for AI, and LLM serving-runtime internals (prefill/decode, KV
  cache, batching). Use when the user asks about Foundry, Azure OpenAI, AI Search,
  RAG, hybrid retrieval, landing zones, IAM, AI gateway, or serving performance.
---

# Azure AI Platform

Portable skill for any repo. Platform depth from theme skills; use with `fde-operating-model` engagement sequence and lock retrieval/serving choices via `domain-and-architecture` ADRs.

## Decision lens — ask every time

**What · Why · How · When (and when NOT).**  
Thread through all choices: **identity-bound everything** (managed identity; keyless AOAI; landing zone IAM).

## Must-not-miss — platform

1. **Three layers** — Platform (Foundry), Models (AOAI + catalogue), Supporting (Search, Content Safety, Doc Intelligence, Speech, Vision).
2. **Foundry** — projects, model catalogue, prompt flow, evaluation, agents, governance (naming evolved Studio → Foundry).
3. **AOAI economics** — PAYG vs **PTU**; SLA is availability not latency/quality; latency SLA mainly on provisioned; claim credits with your telemetry.
4. **Deployment scope vs residency** — Global (capacity) → Data Zone → Regional (strict residency); same token price, different control.
5. **Landing zones** — identity-bound design, network egress, data residency.
6. **Managed identity & RBAC** — prefer never using API keys as the perimeter.
7. **Azure OpenAI vs direct OpenAI** — decide on compliance, residency, cost, latency — not fashion.

## Must-not-miss — RAG

1. **Retrieval quality is RAG quality** — generation can only use what retrieval surfaces (`recall@k`).
2. **Index shape** — key + searchable content + vector + filterable metadata (ACL, date, dept).
3. **Hybrid retrieval** — BM25 + dense fused by **RRF**; then **semantic ranker** (L2) over top candidates; captions/citations.
4. **Metadata filters** — security trimming, freshness, domain routing before ranking.
5. **Embedding choice locks you in** — re-embed entire corpus on model change; eval on *your* data first.
6. **Chunking is the highest-impact knob** — too big drowns signal; too small loses context.
7. **Vector compression** — scalar/binary quantization + oversampling/rescoring tradeoffs.
8. **Pattern ladder** — naive → hybrid → rerank → query rewrite → HyDE; know when RAG fails (relationships/history → semantic layer/KG).
9. **Evaluate retrieval** — recall@k, MRR, nDCG, golden sets — before blaming the LLM.

## Baseline layered architecture — the picture you will be asked to draw

| Layer | Responsibility |
|---|---|
| **Client** | UI or calling process — keep it thin, delegate downward |
| **Intelligence** | Routing, orchestration, agents, conversation management, decisions |
| **Inferencing** | Running the model to produce generations |
| **Knowledge** | Grounding data — indexed, permissioned, kept fresh by a data pipeline |

Enterprise baselines add private networking/private endpoints (no public model endpoint), zone redundancy, firewall egress
control, the landing-zone variant inside pre-governed networking/identity/policy, and an **AI gateway** when you use multiple
providers (one API surface, failover, per-team chargeback). Add the training/fine-tuning workload **only** if you customise models.

The baseline is a starting point, not a destination. **Every deliberate departure becomes an ADR.**

## Well-Architected for AI — use it as a question bank, not a slide

AI workloads swap deterministic behaviour for non-deterministic behaviour. Ask the five pillars' questions *with* the client:

| Pillar | Ask |
|---|---|
| **Reliability** | "What happens when the model is wrong — not if?" (model decay, inference fallback, versioning/retraining) |
| **Security** | "What data reaches the model, and who may see the output?" (prompts/training sets, access control, content safety) |
| **Cost Optimisation** | "What is the cost per successful outcome — not per token?" (build-vs-buy, licensing, model choice) |
| **Operational Excellence** | "Who notices when quality drops, and how fast?" (CI/CD for models, drift detection, feedback loops) |
| **Performance Efficiency** | "What is the quality bar, in a number, agreed by whom?" |

Five questions, five silences, five constraints you did not have an hour ago. Do not present the framework — ask its questions.

## LLM serving runtime — what "make it faster/cheaper" actually means

A request is **prefill** (process the prompt) then **decode** (emit tokens). They have different cost and latency profiles —
**track them separately**, and treat **KV cache as a first-class capacity constraint**, not a detail.

| Optimization | Where it applies |
|---|---|
| KV cache / **paged** KV cache | Decode runtime; GPU memory manager (reduces fragmentation) |
| **Prefix caching** | Prompt-prefix reuse — needs tenant-safe keys |
| **Continuous batching** | Serving scheduler on shared GPUs |
| **Chunked prefill** | Long-context prompts |
| **Speculative decoding** | Predictable long responses |
| **Quantized variants** | Cost-sensitive workloads |
| **Adapters (LoRA)** | Repeated domain behaviour without a full fine-tune |
| Optimized attention kernels | Long-context and throughput |

Also design the **cache tiers** deliberately — prefix, retrieval, semantic, response, and tool-result caches — each with
freshness and entitlement constraints, or you will serve one tenant's answer to another.

**Note:** serving-side quantization (above) is a different decision from **vector** quantization in the index.

## Locking the retrieval decision

- Run **evidence / data discovery first** (what sources exist, trust, entitlements). Then lock **retrieval architecture** (hybrid + ranking + grounding path) in an ADR **before implementing** index/chunk/retrieve pipelines — not before discovery.
- Integration picture: User → agent (Container Apps) → Azure AI Search → Foundry/AOAI → grounded answer, with CI eval gate + App Insights telemetry + Cosmos state + managed identity.
- Cost review: budget vs actual; revisit PTU vs PAYG.
- Clear load-test + eval gates before handover.

## Workflow

1. Separate foundation (landing/IAM) from app RAG design.
2. Anchor to the baseline layered architecture; note every departure as an ADR.
3. Design index + hybrid + filters + chunking; define retrieval eval.
4. Write/update the retrieval ADR (options, decision, consequences).
5. Run the five Well-Architected questions with the client; capture the silences as constraints.
6. Wire identity, telemetry, serving-runtime metrics, and cost controls into the operating picture.

## Do / Don’t

- **Do:** identity-first; hybrid+semantic; measure recall@k; separate prefill/decode metrics; ADR-lock retrieval and departures  
- **Don’t:** key-in-laptop demos as “enterprise done”; vector-only without eval; shared prefix cache without tenant-safe keys; skip residency questions  
