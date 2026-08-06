---
name: agentic-systems
description: >-
  Applies agentic design: workflow patterns before agents (chaining, routing,
  parallelization, orchestrator-workers, evaluator-optimizer); agent =
  deterministic edges + probabilistic core + audited tools; multi-agent
  topologies; framework choice; queue-based scale-out; verifier agents;
  confidence gating; chaos drills. Use when the user asks about workflows vs
  agents, LangGraph, multi-agent orchestration, tool/ACI design, chaos drills, or
  agent memory/checkpointing.
---

# Agentic Systems

Portable skill for any repo. Align agent boundaries with DDD Gen AI boundaries and C4/ADRs (`domain-and-architecture`); implement under Spec-Driven tasks (`spec-driven-delivery`); share HITL/containment with `trust-risk-security`.

## Start here: do you need an agent at all?

**Workflows** orchestrate LLMs and tools through predefined code paths. **Agents** direct their own process and tool use.
Start with the simplest thing that works and *add complexity only when it demonstrably improves outcomes*.

### Building block — the augmented LLM

An LLM with retrieval, tools, and memory attached. Every pattern below composes this block.

### Workflow patterns, in ascending complexity

| Pattern | Use when |
|---|---|
| **Prompt chaining** | The task decomposes into fixed sequential steps; add programmatic gate checks between them |
| **Routing** | Inputs fall into distinct categories better handled separately (a classifier can do the routing) |
| **Parallelization** | *Sectioning* — independent subtasks run concurrently; *voting* — same task run several times for confidence |
| **Orchestrator–workers** | Subtasks cannot be predicted in advance; a central LLM decomposes and delegates |
| **Evaluator–optimizer** | Clear evaluation criteria exist and iterative refinement measurably helps |

### Then agents

Agents suit open-ended problems where the number of steps cannot be predicted or hardcoded, and you can tolerate their
autonomy. They cost more and compound errors — so require **ground truth from the environment at each step**, checkpoints for
human feedback, **explicit stopping conditions (e.g. max iterations)**, and extensive sandboxed testing before production.

### Three principles

1. **Simplicity** — keep the agent's design simple.  
2. **Transparency** — show the planning steps explicitly.  
3. **ACI** — invest in the **agent–computer interface** as much as you would in HCI.

### Tool design (ACI) is prompt engineering

Tool definitions deserve the same attention as the system prompt. Give the model room to "think" before it commits; keep
formats close to what appears naturally in text (a diff needs a line count *before* the code; JSON needs escaping); include
example usage, edge cases, input formats, and clear boundaries from sibling tools. Write the description like a docstring for
a junior engineer, test it against many inputs, and **poka-yoke** the arguments so mistakes get harder (e.g. require absolute
paths rather than relative ones). On real builds, tool optimization can consume more time than prompt optimization.

## Architecture lens — never omit

```text
agent = deterministic edges + probabilistic core + audited tools
```

- Maximize the deterministic shell; minimize/contain the probabilistic core.  
- Trust = inspectable behaviour over time, not one clever completion.  
- Enterprises care about: auditability, HITL control, recoverability (checkpoints), containment (typed tools).

## Graph primitives

| Primitive | Role |
|---|---|
| **State** | Shared typed dict; update via reducers, never blind overwrite |
| **Nodes** | Functions that work (LLM/tool/decide) and return state updates |
| **Edges** | Deterministic or conditional routing you can test/audit |
| **Checkpointer** | Turn/session resume (e.g. a document store for durable persistence) |

Also cover: planner–executor + re-planning; function calling with validation/retries/timeouts/parallelism; guardrails at edges/tools not “inside the model”; turn vs session vs long-term memory; framework choice with justification.

### Confidence, containment, recovery

- **Carry a confidence signal** through state and **gate actions on it** — low confidence routes to HITL, not to a side effect.
- **Circuit-breakers** around flaky tools/providers; fail fast rather than retry a dead dependency into a cost incident.
- **Checkpoints let a long job resume instead of restarting** — persist at node boundaries.
- Accountability precedent: **Air Canada's chatbot** — the operator was held to what its assistant told a customer. An
  ungrounded, unaudited answer is an enterprise liability, not a UX defect.

### Framework choice

Justify against abstraction, control, state, tools, multi-agent support, LLM support, and best fit:

| Framework | Position |
|---|---|
| **Microsoft Agent Framework** | GA; successor to AutoGen / Semantic Kernel — the default ask on a regulated Microsoft stack |
| **LangGraph** | Explicit graphs; complex, audited pipelines; production-proven |
| **Claude Agent SDK / OpenAI Agents SDK** | Lean, model-native agent loops |
| **CrewAI** | Role/crew abstractions (AutoGen's Swarm is retired — do not cite it as current) |

## Multi-agent patterns

1. **Orchestrator / sub-agent** — thin supervisor plans, routes, reconciles  
2. **Parallel agents** — independent specialists + aggregator/consensus  
3. **Handoffs** — transfer conversation to a better specialist  

Real systems often combine all three. Add a **verifier agent** before side effects.

### Handoff & state-sharing

Choose deliberately between **direct shared state** (one store all agents read/write — simple, but coupling and race risk)
and **handoff messages** (explicit payload transferred with the conversation — auditable, but you must design what travels).
Whichever you pick, the transfer itself must be logged.

### Failure modes to design for

Cascades · **agent drift** · **groupthink / loops** · duplicate work · poison messages · runaway cost  

### Scale-out cues

Message queues/topics/sessions · competing consumers · dead-letter queues  

### Chaos drill

Inject agent failures on purpose; prove graceful degradation, not silent corruption.
Keep a **fault catalogue** — for each injected fault, state the safe behaviour you are verifying.

## Workflow

1. Ask whether a workflow pattern suffices before proposing an agent; justify any step up in complexity.  
2. Decide single-agent graph vs multi-agent topology (ADR if material).  
3. Draw deterministic edges + tool allowlist + HITL nodes; write the tool schemas as carefully as the prompts.  
4. Define state, checkpointing, confidence gating, verifier, stopping conditions, and failure/DLQ behaviour.  
5. Specify chaos drill scenarios and success criteria.  
6. If executive-facing, hand off to `exec-communication` for the workflow-redesign framing.

## Do / Don’t

- **Do:** simplest pattern that works; keep orchestrator thin; verify before acting; chaos-test; persist checkpoints  
- **Don’t:** one mega-prompt agent; untyped tools; agent where a chain would do; unbounded loops; skip HITL on high-impact nodes  
