# Definition of Done

The capstone is complete only when another team can extract the submission on a clean machine, run it using documented commands, reproduce its tests and evaluation, inspect its evidence, and understand its limitations without undocumented assistance.

## 1. Problem and value

- The measurable problem, baseline, affected decisions, users, constraints and no-AI alternative are evidenced.
- Benefits include cycle time, quality, safety, review burden and full operating cost; assumptions and stop/pivot thresholds are explicit.
- The chosen intervention is narrower than the business problem and does not automate prohibited accountability.

## 2. Three working workflows

Each mandatory workflow has versioned input/output contracts, deterministic test data, safe failure behaviour, provenance, authority, as-of time, uncertainty, abstention, human-review state and audit evidence.

- Batch workflow identifies evidence completeness, conflicts and gaps but cannot release, reject, reprocess, relabel or recall.
- PV workflow supports intake and analysis but cannot make final seriousness, causality, expectedness, reportability or signal decisions.
- Supply workflow produces non-executing options but cannot reserve, allocate, change quality status, ship or initiate recall.

## 3. Engineering and architecture

- Reproducible setup, run, test, evaluate, reset and evidence-export commands exist.
- Dependencies are locked or the deterministic standard-library mode needs no installation.
- Requirements trace to architecture, ADRs, code, tests, controls, evidence and residual risks.
- Brownfield coexistence, migration, rollback, decommissioning and data reconciliation are addressed.

## 4. GxP, safety, security and privacy

- Intended use, GxP boundary, records/signatures boundary, validation/assurance approach and quality-risk controls are documented.
- Prompt injection, poisoning, tool abuse, stale authorization, replay, exfiltration, excessive agency, supply-chain compromise and denial-of-wallet are tested.
- Purpose limitation, minimisation, retention, consent/withdrawal, pseudonymisation, re-identification and cross-border constraints are evidenced.
- Prohibited actions fail closed. Current authorization and signed/approved tools are checked at execution time.

## 5. Evaluation and operations

- Golden, edge, adversarial, subgroup, failure, outage, recovery and regression suites exist.
- Release thresholds are measurable; failed gates block release.
- SLI/SLO, capacity, observability, incident response, backup/restore, AI-disabled continuity and retirement are demonstrated.
- Token/context budgets, avoided inference, human-review cost and cost per successful task are measured.

## 6. Submission evidence

- All 30 required artefacts are completed or mapped to equivalent evidence.
- Machine-readable test and evaluation results are included.
- A submission manifest lists every deliverable, owner, version, status and hash.
- No secret, personal data, live credential, proprietary source record or undeclared external dependency is included.
- `python tools/check_submission_structure.py --final` passes.

## 7. Defence

The team demonstrates happy, edge, attack, outage, recovery and manual paths; proves prohibited actions cannot execute; answers an inspection-style evidence request; and gives a clear go, conditional-go, pivot, pause or stop recommendation.
