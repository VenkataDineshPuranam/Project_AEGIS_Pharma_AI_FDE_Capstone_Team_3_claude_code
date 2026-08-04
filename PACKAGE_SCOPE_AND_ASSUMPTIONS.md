# Package Scope and Assumptions

## Package mode

- Fully synthetic and offline-capable.
- Challenge-only: no reference solution, answer key, golden architecture, completed POC or finished pitch.
- All 84 injects are disclosed from the start; there are no later instructor-only injects.
- External links are optional research anchors. All evidence required to begin and complete the capstone is included locally.
- Python 3.10+ is the only runtime assumed for supplied checks. The explorer requires only a modern browser.

## Participant freedom

Participants may use any implementation stack, including a deterministic non-LLM design, provided they supply locked dependencies, offline or mocked execution, reset and test commands, evidence export, and a defensible migration path. A knowledge graph, agent, vector database or large language model is not mandatory unless justified by evidence.

## Immutable and writable areas

- Treat `case/`, `data/`, `knowledge/`, `source_documents/`, `evaluation/`, `requirements/`, `starter/` and `templates/` as challenge evidence.
- Place all work under `submission/`.
- `FILE_HASHES.csv` protects immutable challenge content and intentionally excludes `submission/` and generated validation reports.

## Deliberate ambiguity

The case intentionally contains conflicting identifiers, versions, timestamps, authorities, quality states, terminology, access states, and business priorities. Do not “clean” these away without preserving source evidence and recording a governed resolution. Records marked `referenced_missing`, `untrusted`, `draft`, `superseded`, `unknown`, or similar are challenge conditions, not packaging defects.

## Regulatory boundary

The repository supplies scenario-specific internal policy extracts and a compact local reference guide. It does not provide legal advice or assert universal regulatory applicability. Participants must state jurisdiction, intended purpose, accountable role, system boundary, risk classification and assumptions for every regulatory conclusion.

## No hidden services

No cloud key, database, internet connection, proprietary model, external API or instructor service is needed to inspect the evidence, run public fixtures, validate contracts or execute the supplied checks. Participant solutions that add such services must retain an offline deterministic mode.
