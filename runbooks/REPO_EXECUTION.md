# Repository Execution

## Zero-install challenge checks

From the repository root:

```text
python run_capstone.py --check
```

Equivalent launchers are `run_capstone.ps1` and `run_capstone.sh`. The checks use only the Python standard library. Open `app/index.html` directly or run `python run_capstone.py --serve`.

## Participant implementation contract

Provide documented commands under `submission/scripts/` for setup, run, test, evaluate, reset and evidence export. Commands must work from a clean extraction. Lock every added dependency and provide a deterministic offline or mock mode. No secret or cloud key may be required for assessment.

## Clean-room proof

Before defence, extract the final ZIP to a different directory, run preflight twice, run participant setup/test/evaluation/reset, compare evidence hashes, and document any platform limitation. Runtime caches and generated files must not invalidate immutable challenge evidence.
