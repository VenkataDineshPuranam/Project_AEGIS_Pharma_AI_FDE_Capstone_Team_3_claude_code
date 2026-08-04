# Evaluation Plan Requirements

No expected answers are supplied. Participants must construct and justify evaluation assets. The 15 public fixtures are reproducible input bundles, not answer keys.

## Required suites

1. Business outcome and process-baseline evaluation.
2. Evidence fidelity, provenance, temporal applicability and citation correctness.
3. GxP and safety-boundary tests, including prohibited autonomous decisions.
4. Data-integrity, audit-trail and electronic-record trustworthiness tests.
5. Retrieval authority, supersession, poisoning and prompt-injection tests.
6. Structured-output, abstention, uncertainty and human-review tests.
7. Pharmacovigilance duplicate, clock, terminology, listedness and multilingual tests.
8. Agent path, tool authorization, idempotency, replay and partial-failure tests.
9. Privacy leakage, cross-border and purpose-limitation tests.
10. Subgroup, language, usability and accessibility tests.
11. Latency, capacity, token use, cost per successful task and denial-of-wallet tests.
12. Model substitution, regression, outage, rollback, manual mode and retirement tests.

## Public fixtures

Use `PUBLIC_FIXTURE_INDEX.csv` and `public_fixtures/`. A test runner must record scenario ID, input hash, implementation version, contract version, result, evidence path, reviewer role and gate outcome. Participants must add their own edge, adversarial and failure fixtures.

## Release gates

At minimum, release must be blocked by: schema failure; fabricated or uncited material fact; unresolved identity/unit/time/authority conflict presented as resolved; stale authorization; untrusted instructions; prohibited regulated conclusion or side effect; missing manual mode; failed critical security test; missing subgroup evidence; or unreproducible build/evaluation.

## Evaluation deliverables

Provide a golden set, edge-case set, adversarial set, failure-recovery set, deterministic graders where possible, calibrated human rubric, judge controls if an LLM judge is used, release thresholds, regression history and evidence that failed gates block release. Numeric thresholds must be justified by workflow risk and baseline—not selected after seeing results.
