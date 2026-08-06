---
name: data-and-knowledge
description: >-
  Applies data/knowledge architecture: discovery (exists/usable/governed/missing),
  schema discovery, data contracts, entity resolution, semantic layers,
  knowledge graphs, GraphRAG and SQL RAG, the question router, provenance vs
  citation, and profiling/expectations gates. Use when the user asks about
  semantic layers, knowledge graphs, GraphRAG, text-to-SQL, data discovery, data
  contracts, Cypher, Great Expectations, or dbt metrics.
---

# Data & Knowledge

Portable skill for any repo. Takes over where `azure-ai-platform` passage-level RAG stops; lock meaning placement with ADRs (`domain-and-architecture`).

## Thesis (must state)

Every client asks for RAG. Many need **metadata, a governed metric layer, a graph, or a hybrid** — defended with discovery evidence, not fashion.

Hybrid retrieval is still passage-level. This skill answers questions whose answers span entities, relationships, history, and governed metrics.

## Discovery — four questions (before any architecture)

| Question | Output | Trap |
|---|---|---|
| What **EXISTS**? | Source register + owner | Demo dataset |
| What is **USABLE**? | Profiling report | “Data is clean” without profile |
| What is **GOVERNED**? | Classification, residency, system-of-record | Ungoverned ≠ unregulated |
| What is **MISSING**? | Gap register (spike or scope cut) | Finding the gap in UAT |

Add to discovery: **schema discovery patterns** (schema-on-write vs schema-on-read — know which one the source actually uses)
and **data contracts** — a source with no versioned contract and no named owner is a risk wearing an integration's label.

## Meaning ladder (decision tree)

```text
Pure RAG → +metadata → +semantic/metrics layer → Knowledge Graph → hybrid
```

Ask: where should meaning live — text, metadata, metrics, or relationships? Climb a rung only when the evidence forces you.

## Three things naive RAG cannot do

1. **Relationships / multi-hop** — questions whose answer is a path, not a passage.  
2. **Entity resolution** — "Meridian Freight Ltd", "MERIDIAN FREIGHT LIMITED", "Meridian Frieght" are one company.
   Embeddings score them *similar*; the business needs them *the same*. Sum an exposure across them and you double-count
   or silently miss a third of it.  
3. **Provenance** — the regulator does not ask where the text came from; they ask **why this answer is the answer**.

**A citation is not provenance.** A citation says "document 47, page 12". Provenance reconstructs a reproducible path —
clause → policy → version in force on the signature date → threshold → rule applied → verdict — identical every time it is
asked. Most vendors sell the first and call it the second. This distinction wins regulated deals.

## Retrieval architecture — route the question, don't pick one pattern

A **question router** classifies the question (text · number · relationship · compliance) and selects the retrieval need.
**Log the routing decision with the answer — the route is itself auditable.**

| Route | Serves |
|---|---|
| **Document RAG** — hybrid retrieval | Passage-level text questions (vector + keyword + RRF, metadata-filtered) |
| **SQL RAG** (text-to-SQL) | Governed natural-language analytics — go *through* the semantic layer, never straight at raw tables |
| **GraphRAG** | Entity-and-relationship questions, impact analysis, questions that cross documents |
| **Tools / rules** | Deterministic answers that must not be generated at all |
| **No retrieval** | Say so — it is a valid route |

Then assemble the answer with a **provenance assembler** that returns the path, not just the sources.

## Semantic layer vs knowledge graph

- **Semantic layer** — governed business metrics/definitions; stops conflicting KPI language and semantic drift
  (two dashboards, one word, two truths). Defined once, in code, served to every BI tool *and* the AI agent.  
  Vocabulary: **semantic models**, **entities / dimensions / metrics**, **MetricFlow**, **time spine**.  
  Three generations: BI-tool layers (UI-bound) → **LookML** (metrics-as-code) → external layers (dbt / Cube / AtScale,
  decoupled from any BI vendor). Direction of travel: versioned metrics-as-code. Watch **Open Semantic Interchange (OSI)**
  as the emerging cross-vendor standard. For a small team the honest answer is often "not yet" — it is a component to run.
- **Knowledge graph** — explicit entities/relationships, temporal validity on edges, entity resolution on the key nodes;
  multi-hop questions; advanced Cypher patterns. Store options include Neo4j-style engines, **Amazon Neptune**,
  **Azure Cosmos DB (Gremlin)**.

## Data quality gates

- **Profiling** (e.g. ydata-profiling) on the *real* extract day one — evidence for discovery conversations.  
- **Great Expectations** — turn findings into CI-enforced expectations before loads. You already unit-test your code;
  unit-test the data. Vocabulary: **Expectation Suites**, **Checkpoints**, **Validation Results**, **Data Docs**.  
- Six checkable quality properties: **validity · completeness · accuracy · consistency · uniqueness · timeliness**.  
- The **1–10–100 rule**: $1 to prevent an error at entry, $10 to fix it in the pipeline, $100 once a bad decision is made.  
- Findings → expectations is the discovery→gate handoff.

## ADR defence

When choosing KG / semantic / hybrid, write an ADR with options, evidence from discovery, consequences, and what remains out of scope.

## Workflow

1. Run the four discovery questions; refuse architecture without the registers.  
2. Place the workload on the meaning ladder with evidence.  
3. If metrics conflict → semantic layer; if relationships missing → KG/hybrid; if the question is a number → SQL RAG
   through the semantic layer.  
4. Design the question router and the provenance path before the index.  
5. Define CI expectations for data quality.  
6. Lock the decision in an ADR.

## Do / Don’t

- **Do:** profile real data; resolve entities before aggregating; log the routing decision; gap-register missing relationships/history; defend with evidence  
- **Don’t:** default to RAG for every brief; text-to-SQL straight onto raw tables; discover gaps in UAT; confuse citations with provenance  
