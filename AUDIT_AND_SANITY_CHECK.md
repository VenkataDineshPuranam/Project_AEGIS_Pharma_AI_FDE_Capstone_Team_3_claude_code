# Audit and Sanity-Check Record

## Scope

The original ZIP was reviewed as a standalone pharmaceutical AI FDE capstone across packaging, case coherence, evidence, data integrity, knowledge authority, brownfield code, public evaluation, safety/GxP boundaries, security, privacy, reliability, economics, templates, runbooks, submission controls and offline execution.

## Material findings in the original package

| Severity | Finding | Impact | Closure in v2 |
|---|---|---|---|
| Critical | `check_submission_structure.py` passed the untouched placeholder scaffold | False completion signal | Added scaffold and strict-final modes with substantive artefact and machine-readable evidence gates |
| High | Package verifier counted files but did not validate content, mappings, relationships, hashes, fixtures or contracts | Broken or inconsistent packages could pass | Replaced with deep fail-fast validator and validation report |
| High | Public scenarios contained prompts only | Not independently executable or reproducible | Added 15 local evidence bundles with hashes and authorization context |
| High | Workflow contracts were prose only | Prohibited fields and side effects could not be machine blocked | Added fail-closed JSON schemas and positive/negative contract tests |
| High | Knowledge catalog covered only 2 of 32 documents | Retrieval authority and completeness were not governable | Catalogued every document with status, authority, date and hash; expanded policy extracts |
| High | All 30 templates were minimal shells | Inconsistent workshop evidence and weak assessment | Replaced with structured evidence, analysis, risk, traceability and review sections |
| High | The stated 180-point scoring table actually totalled 194 | Scores and pass decisions would be inconsistent | Rebalanced the same 17 areas to an exact 180 points and added machine validation |
| High | Offline explorer used `innerHTML` on challenge content | Injection/XSS risk contradicted the security learning objective | Rebuilt using safe text nodes and accessible controls |
| Medium | Manifest file count was stale and hash scope was not participant-safe | Ambiguous integrity boundary | Regenerated manifest and immutable hashes excluding `submission/` and generated reports |
| Medium | No dataset profile, data dictionary or relationship model | Structural defects and referential gaps were difficult to detect | Added exact profiles, field metadata and enforced relationships |
| Medium | Some approved/referenced source documents had no local extract | Reduced offline self-sufficiency | Added local synthetic extracts while preserving one intentionally missing eCTD record |
| Medium | PowerShell was the only launcher | Platform dependency | Added Python and POSIX shell launchers |
| Medium | External regulatory links were the only detailed anchor | Offline delivery depended on internet access | Added a local training guide; links remain optional |
| Medium | No explicit duration, checkpoints or clean-room handover standard | Deployment variability | Added 40-hour plan, Definition of Done and clean-room workflow |

## Data treatment

The audit did not “repair” intentional case contradictions, such as conflicting identities, units, protocol applicability, awareness dates, quality states, listedness sources, authorization caches, untrusted documents or outage states. These remain participant problems. Structural integrity and declared cross-file relationships are now machine checked.

## Validation performed after enhancement

- ZIP/source archive safety and extraction review.
- UTF-8, NUL-byte, JSON and CSV structural checks.
- Exact profile and hash checks for original datasets.
- Sequential and one-to-one validation of all 84 injects and evidence mappings.
- Cross-file relationship checks for clinical, manufacturing, PV, supply, model and evidence entities.
- Full catalog and hash validation for 32 knowledge documents.
- One-to-one validation of all 15 public fixtures and their evidence hashes.
- Positive and negative execution of all workflow contracts.
- Deterministic explorer rebuild and unsafe-HTML check.
- Python and JavaScript syntax checks.
- Immutable-file hash verification.
- Empty submission rejection and clean-room repeatability.

## Residual boundary

This is a complex training simulation, not a validated pharmaceutical system. Participant solutions still require qualitative assessment, technical defence and contextual regulatory review; a passing structural validator does not certify GxP fitness or real-world safety.
