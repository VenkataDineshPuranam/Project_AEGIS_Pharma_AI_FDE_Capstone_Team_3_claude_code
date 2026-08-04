# AEGIS Architecture Map

Offline interactive architecture deliverables derived from the challenge package and the planned `submission/` runtime (FINAL project plan).

## Files

| File | Purpose |
|---|---|
| `AEGIS_ARCHITECTURE_MAP.json` | Agent-ready graph: `nodes`, `edges`, `flows[].steps` |
| `AEGIS_ARCHITECTURE_INTERACTIVE.html` | Self-contained interactive diagram + flows panel |
| `export_architecture_html.py` | Regenerates the HTML from the JSON |

## Open the diagram

Open `AEGIS_ARCHITECTURE_INTERACTIVE.html` in a browser (double-click or drag into Chrome/Edge/Firefox). No server required.

## Regenerate HTML after JSON edits

```text
python -B submission/artefacts/Architecture/export_architecture_html.py
```

## Agent usage notes

- Prefer flows when planning multi-step work.
- Respect `meta.writable_boundary` (`submission/`) and `meta.immutable_trees`.
- Never propose prohibited autonomy listed in workflow node tooltips.
