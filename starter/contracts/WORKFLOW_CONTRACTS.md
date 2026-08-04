# Minimum Workflow Contracts

The executable minimum contracts are in `evaluation/contracts/`. Participants may extend them only through a versioned design with compatibility tests and preserved fail-closed boundaries.

## Batch evidence

Input: batch identifier, purpose, as-of time and current authorized user context. Output: cited evidence, applicable documents, contradictions, gaps, abstentions and review readiness. No disposition or execution property is permitted.

## PV intake

Input: source package, receipt events, product context, purpose, as-of time and current authorized user context. Output: preserved source facts, uncertainty, duplicate candidates, clock evidence, terminology and listedness provenance, and required human reviews. Final safety conclusions are not permitted.

## Supply planning

Input: shortage/cold-chain event, inventory snapshot, quality status, demand, constraints, purpose, as-of time and current authorization. Output: ranked draft options, violated constraints, approvals and impacts. `no_side_effects` must be true; reservation, allocation, shipment, quality-status change and recall properties are not permitted.

Run `python tools/test_contracts.py` to prove positive examples pass and prohibited examples fail.
