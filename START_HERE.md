# Start Here — Project AEGIS-PHARMA

Project AEGIS-PHARMA is a challenge-only, fully synthetic, offline-capable AI Forward Deployed Engineering capstone. It is designed to be executed without an instructor revealing later injects or a reference solution.

## First 20 minutes

1. Extract the ZIP to a writable local folder. Avoid editing inside the ZIP.
2. Run the preflight from the repository root:
   - Windows: `python run_capstone.py --check`
   - PowerShell: `./run_capstone.ps1`
   - macOS/Linux: `./run_capstone.sh`
3. Read `PACKAGE_SCOPE_AND_ASSUMPTIONS.md` and `case/INTEGRATED_CASE.md` completely.
4. Open `app/index.html` for the offline inject and evidence explorer.
5. Run `python starter/baseline_diagnostics.py`; treat its output as a starting clue, not a complete assessment.
6. Put every participant-created or modified artefact under `submission/`. Do not alter challenge evidence.

## Required outcome

Deliver a defensible intervention for all three mandatory workflows:

- GxP batch-review evidence reconciliation without batch disposition.
- Pharmacovigilance intake and signal support without final safety decisions.
- Supply-shortage and cold-chain option planning without inventory, allocation, shipment or recall execution.

The submission must include working deterministic tests, an offline execution mode, evaluation evidence, security and GxP controls, operational runbooks, and a final defence. The full completion standard is in `DEFINITION_OF_DONE.md`.

## Core commands

```text
python tools/verify_package.py
python tools/test_contracts.py
python tools/check_submission_structure.py --scaffold
python tools/check_submission_structure.py --final   # expected to fail until work is complete
python tools/rebuild_explorer_data.py --check
```

## Safety boundary

This repository is fictional training material. It must not be used for real product release, clinical, pharmacovigilance, patient, regulatory, quality, supply or recall decisions.
