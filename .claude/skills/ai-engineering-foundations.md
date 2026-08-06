---
name: ai-engineering-foundations
description: >-
  Applies Python AI scaffolding: Pydantic v2 typed LLM contracts, resilient async
  clients with retries/backoff, function-calling validation, FastAPI exposure,
  ports-and-adapters provider swap, and contract tests. Use when the user asks
  about typed contracts, LLM SDK scaffolding, provider adapters, function calling,
  or FastAPI AI services.
---

# AI Engineering Foundations

Portable skill for any repo. Primary satellite during Deliver (stage 11) under `spec-driven-delivery` task execution.

## Foundational idea

**Scaffolding** = contracts, validation, error handling, tests, and layering built *before/under* AI features so the system does not collapse when the model/vendor drifts.

Mental model: **the model is a flaky vendor** — type it, validate it, retry it, time it out.

## Must-not-miss points

1. **Contract drift is the production bug** — same meaning, different JSON shape (staging vs prod) crashes clients; normalize at the boundary.
2. **Pydantic v2 is the contract** — `strict=True`; before-validators absorb provider drift into one clean shape (`text`, `model`, `finish_reason`).
3. **Typed client + retries** — validate inside the retry loop; TransientError → backoff (`base * 2^attempt` + jitter in prod); PermanentError → stop.
4. **Timeouts** — never hang the event loop on a model call.
5. **Ports & adapters** — no SDK imports in business logic; procurement *will* change vendors; swap is one adapter line.
6. **Function calling** — `json.loads` then schema-validate; return typed `ok=False` errors, never stack traces to callers.
7. **FastAPI `response_model`** — outbound validation; 422 on bad input is a feature.
8. **Contract tests** — pin the boundary; later domain/integration work trusts these stay green.
9. **Async + packaging** — I/O-bound LLM calls; reproducible env (`uv`/venv).

## Four verbs at every model boundary

| Verb | Meaning |
|---|---|
| Type | Strict schemas at the edge |
| Validate | Reject garbage with field names |
| Retry | Transient 429/5xx with backoff |
| Time out | Bound wait; fail loudly |

## Workflow

1. Identify the LLM/tool boundary in the user’s feature.
2. Define request/response (and tool-arg) schemas.
3. Specify normalize → validate → call → map errors.
4. Require contract tests for provider-shape drift.
5. Keep domain logic out of prompts.

## Do / Don’t

- **Do:** strict contracts; provider-swappable adapters; typed tool errors  
- **Don’t:** notebook-style scripts as production; silent KeyError on shape drift; SDK in domain core  
