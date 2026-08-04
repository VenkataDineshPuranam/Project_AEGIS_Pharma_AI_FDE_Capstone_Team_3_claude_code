# Submission Evidence Standard

A workshop submission is assessable only when evidence is inspectable without running a private service or relying on oral explanation.

## Mandatory machine-readable files

Under `submission/evidence/` provide:

- `submission_manifest.csv` with columns `path,owner,version,status,sha256`.
- `file_hashes.csv` generated from the final submission state.
- `test_results.json` containing suite, test ID, requirement/control IDs, result, timestamp, runtime mode and evidence path.
- `evaluation_results.json` containing dataset/cohort, grader, threshold, observed result, gate result and evidence path.

## Minimum runbooks

Provide setup, operations, incident response and AI-disabled continuity runbooks. Each command must specify prerequisites, inputs, expected outputs, failure handling and reset/rollback.

## Evidence quality

- Use relative paths and stable IDs.
- Preserve original evidence and record transformations.
- Separate facts, interpretations, assumptions, decisions and residual risk.
- Record software, model, prompt, corpus, schema, tool and evaluator versions.
- Do not include credentials, live personal data, proprietary records or unverifiable screenshots as the sole evidence.

## Completion test

Run `python tools/hash_submission.py`, then `python tools/check_submission_structure.py --final`. Structural success does not replace content scoring or defence.
