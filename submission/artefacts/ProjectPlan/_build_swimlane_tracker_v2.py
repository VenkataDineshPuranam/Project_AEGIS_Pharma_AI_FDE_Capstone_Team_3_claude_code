"""Build AEGIS_PROJECT_SWIMLANE_TRACKER_V2.xlsx from swimlane + plan V2.

Run: python -B submission/artefacts/ProjectPlan/_build_swimlane_tracker_v2.py

Seat labels use FDE1–FDE5 (plan aliases for former P1–P5 people seats).
Phase IDs remain P0–P9.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

OUT = Path(__file__).resolve().parent / "AEGIS_PROJECT_SWIMLANE_TRACKER_V2.xlsx"

# People seats (was P1–P5 in plan). Do not confuse with phase IDs P0–P9.
SEATS = [
    ("FDE1", "Value (V)", "Product / Value Lead"),
    ("FDE2", "Domain (D)", "Domain / Evidence Lead"),
    ("FDE3", "Architecture (A)", "Architecture / Build Lead"),
    ("FDE4", "GxP / Quality (Q)", "GxP / Quality / ISO / Assurance Lead"),
    ("FDE5", "Security / Eval (S)", "Security / Privacy / Eval / Reliability Lead"),
]
SEAT_IDS = [s[0] for s in SEATS]

PHASES = [
    # phase_id, name, start_h, end_h, exit_gate, track, days
    ("P0", "Preflight", 0, 2, "Preflight", "A", ["D1"]),
    ("P1", "Discovery", 2, 7, "G1", "A", ["D1", "D2"]),
    ("P2", "Domain", 7, 12, "G2", "A", ["D3", "D4"]),
    ("P3", "Architecture", 12, 18, "G3", "A", ["D5"]),
    ("P4", "Secure design", 18, 23, "G4", "A", ["D6", "D7"]),
    ("P5", "POC build", 23, 31, "G5", "A", ["D8", "D9"]),
    ("P6", "TEVV", 31, 35, "G6", "A", ["D10"]),
    ("P7", "Ops + clean-room", 35, 38, "G7", "A", ["D10"]),
    ("P8", "Defence", 38, 40, "G8", "A", ["D10"]),
    ("P9", "Production hardening", None, None, "G9", "B", ["D11", "D12", "D13", "D14"]),
]
PHASE_IDS = [p[0] for p in PHASES]

# Seat focus per phase — aligned to Plan V2 §8.2 Gate_RACI (author / must-review).
# Wording rules: only seats listed in Gate_RACI Must Review may say "Must-review G#".
PHASE_LANE = {
    "P0": {
        "FDE1": "Charter / plan ratification",
        "FDE2": "Case + inject skim",
        "FDE3": "Scaffold + Hour-0 archive",
        "FDE4": "Constraints catalogue",
        "FDE5": "Constraints catalogue",
    },
    "P1": {
        "FDE1": "Author G1 — artefacts 01–04 + production NFRs",
        "FDE2": "Inject skim support",
        "FDE3": "Scripts skeleton",
        "FDE4": "Must-review G1 — constraints catalogue",
        "FDE5": "Must-review G1 — NFR / threat notes",
    },
    "P2": {
        "FDE1": "Must-review G2",
        "FDE2": "Author G2 — artefacts 05–08 + 84-inject register",
        "FDE3": "RTM / RELATIONSHIP_MODEL start",
        "FDE4": "Must-review G2 — authority / lineage",
        "FDE5": "Privacy / eval support (not G2 must-review)",
    },
    "P3": {
        "FDE1": "Architecture support (not G3 must-review)",
        "FDE2": "Must-review G3 — RTM 09 + language",
        "FDE3": "Author G3 — artefacts 10–12 + evidence-resolver",
        "FDE4": "Co-author G3 — artefacts 13–15 GxP/CSA/QRM",
        "FDE5": "Must-review G3 — threat skeleton + contract tests",
    },
    "P4": {
        "FDE1": "Must-review G4 — artefact 18 RAI",
        "FDE2": "Domain support (not G4 must-review)",
        "FDE3": "Must-review G4 — Cursor evidence; build prep",
        "FDE4": "Co-author G4 — artefacts 19–21 ISO / EU AI Act",
        "FDE5": "Author G4 — artefacts 16–17 + failing prohibited tests",
    },
    "P5": {
        "FDE1": "Must-review G5 — Workflow C domain + UX",
        "FDE2": "Workflow B domain rules",
        "FDE3": "Author G5 — build A→C→B + app + scripts",
        "FDE4": "Must-review G5 — Workflow A readiness rules",
        "FDE5": "Golden / edge / adversarial tests",
    },
    "P6": {
        "FDE1": "FinOps 23 + delivery FinOps",
        "FDE2": "Must-review G6 — clinical / PV inject suites",
        "FDE3": "Must-review G6 — adapter wire + outage path",
        "FDE4": "Reg-authority suites",
        "FDE5": "Author G6 — runner / graders / policies / reports",
    },
    "P7": {
        "FDE1": "26 TOM + 29 runway (G7 full-team review)",
        "FDE2": "Domain freeze sign (G7 full-team review)",
        "FDE3": "Author G7 — evidence files + clean-room",
        "FDE4": "27/28 draft (G7 full-team review)",
        "FDE5": "Co-author G7 — runbooks + eval evidence",
    },
    "P8": {
        "FDE1": "Author G8 — pitch 30 + ship decision",
        "FDE2": "Defence domain demos (G8 full-team review)",
        "FDE3": "Freeze + hash (G8 full-team review)",
        "FDE4": "GxP defence proof (G8 full-team review)",
        "FDE5": "Red-team / outage demos (G8 full-team review)",
    },
    "P9": {
        "FDE1": "G9 release decision / L1 runbook",
        "FDE2": "RC domain regression",
        "FDE3": "G9 tech — RC packaging / rollback / tag",
        "FDE4": "Author G9 — chair Readiness Board 28",
        "FDE5": "G9 security sign — SLO / sec retest",
    },
}

DAYS = [
    ("D1", "Preflight + SCQA start", "—", "P0/P1", "A"),
    ("D2", "Business case, stakeholders, blueprint, prod NFRs", "G1", "P1", "A"),
    ("D3", "DDD + data gov + brownfield", "—", "P2", "A"),
    ("D4", "Ontology + KG + inject map", "G2", "P2", "A"),
    ("D5", "C4 + ADR + contracts + GxP", "G3", "P3", "A"),
    ("D6", "Threat modelling + privacy + security tests", "—", "P4", "A"),
    ("D7", "ISO 42001 + EU AI Act + assurance + human factors", "G4", "P4", "A"),
    ("D8", "Build WF A (+ resolver) + app shell; start C", "—", "P5", "A"),
    ("D9", "Finish C + B; AI-disabled; MVP demo", "G5", "P5", "A"),
    ("D10", "TEVV / FinOps / clean-room / defence", "G6–G8", "P6/P7/P8", "A"),
    ("D11", "P9: SLO, runbooks, packaging", "—", "P9", "B"),
    ("D12", "P9: security retest, backup/restore, rollback", "—", "P9", "B"),
    ("D13", "Production Readiness Board + RC tag", "G9", "P9", "B"),
    ("D14", "Buffer / defect burn-down (optional)", "—", "P9", "B"),
]
DAY_IDS = [d[0] for d in DAYS]

DAY_LANE = {
    "D1": {
        "FDE1": "SCQA start",
        "FDE2": "Case read",
        "FDE3": "Scaffold + Hour-0 baseline archive",
        "FDE4": "Constraints catalogue start",
        "FDE5": "Constraints / NFR notes start",
    },
    "D2": {
        "FDE1": "Author G1 — business case / NFRs / artefacts 01–04",
        "FDE2": "Inject skim support",
        "FDE3": "Scripts skeleton",
        "FDE4": "Must-review G1 (with FDE5)",
        "FDE5": "Must-review G1 — NFR lock (with FDE4)",
    },
    "D3": {
        "FDE1": "Stakeholder / value support",
        "FDE2": "DDD + data gov (05–06)",
        "FDE3": "Brownfield map / RTM start",
        "FDE4": "Authority notes",
        "FDE5": "Eval dataset design start",
    },
    "D4": {
        "FDE1": "Must-review G2 (with FDE4)",
        "FDE2": "Author G2 — ontology / KG / inject map",
        "FDE3": "RELATIONSHIP_MODEL checker start",
        "FDE4": "Must-review G2 — authority / lineage",
        "FDE5": "Privacy / eval support (not G2 must-review)",
    },
    "D5": {
        "FDE1": "Architecture support (not G3 must-review)",
        "FDE2": "Must-review G3 — RTM 09 + language",
        "FDE3": "Author G3 — C4 / ADR / contracts / resolver",
        "FDE4": "Co-author G3 — GxP artefacts 13–15",
        "FDE5": "Must-review G3 — threat skeleton + contract tests",
    },
    "D6": {
        "FDE1": "RAI 18 draft (prep for G4 must-review)",
        "FDE2": "Domain support for threat model (not G4 must-review)",
        "FDE3": "Build prep / Cursor evidence (prep for G4 must-review)",
        "FDE4": "Privacy / QRM support (prep for G4 co-author)",
        "FDE5": "Threat modelling + privacy + security tests",
    },
    "D7": {
        "FDE1": "Must-review G4 (with FDE3)",
        "FDE2": "Domain support (not G4 must-review)",
        "FDE3": "Must-review G4 (with FDE1)",
        "FDE4": "Co-author G4 — ISO / EU AI Act / assurance",
        "FDE5": "Author G4 — failing prohibited tests",
    },
    "D8": {
        "FDE1": "Supply path start (WF C domain)",
        "FDE2": "WF B domain prep",
        "FDE3": "WF A + evidence-resolver + app shell; start C",
        "FDE4": "WF A readiness rules",
        "FDE5": "Tests for WF A / prohibited paths",
    },
    "D9": {
        "FDE1": "Must-review G5 — WF C + MVP demo",
        "FDE2": "WF B domain rules",
        "FDE3": "Author G5 — finish C + B; AI-disabled scripts",
        "FDE4": "Must-review G5 — WF A rules finalize",
        "FDE5": "AI-disabled tests + MVP test evidence",
    },
    "D10": {
        "FDE1": "Author G8 — FinOps + defence pitch (also G7 full-team)",
        "FDE2": "Must-review G6 — inject suites (clinical/PV); G7/G8 full-team",
        "FDE3": "Must-review G6; Author G7 — clean-room / freeze; G8 full-team",
        "FDE4": "Assurance + GxP defence proof (G7/G8 full-team)",
        "FDE5": "Author G6 — TEVV reports; Co-author G7; G8 full-team",
    },
    "D11": {
        "FDE1": "Support runbooks (L1)",
        "FDE2": "RC domain regression prep",
        "FDE3": "App packaging & config",
        "FDE4": "Accessibility smoke prep",
        "FDE5": "Observability & SLOs",
    },
    "D12": {
        "FDE1": "Release decision draft",
        "FDE2": "Domain regression execute",
        "FDE3": "Backup/restore + rollback evidence",
        "FDE4": "Residual risk draft",
        "FDE5": "Security retest + backup/restore",
    },
    "D13": {
        "FDE1": "G9 release decision sign",
        "FDE2": "Domain sign-off",
        "FDE3": "G9 tech — RC tag + manifest",
        "FDE4": "Author G9 — chair Production Readiness Board",
        "FDE5": "G9 security sign",
    },
    "D14": {
        "FDE1": "Defect burn-down / buffer",
        "FDE2": "Defect burn-down / buffer",
        "FDE3": "Defect burn-down / buffer",
        "FDE4": "Defect burn-down / buffer",
        "FDE5": "Defect burn-down / buffer",
    },
}

GATES = [
    ("Preflight", "Package + charter; Hour-0 baseline", "All", "—", "P0", "D1"),
    ("G1", "Problem measurable; no-AI honest; NFRs locked?", "FDE1", "FDE4 + FDE5", "P1", "D2"),
    ("G2", "Conflicts tracked not silently resolved; inject register real?", "FDE2", "FDE1 + FDE4", "P2", "D4"),
    ("G3", "Prohibited actions outside executable boundary?", "FDE3 + FDE4", "FDE2 + FDE5", "P3", "D5"),
    ("G4", "Threat/privacy/ISO controls + failing prohibited tests? Agents unlock after PASS", "FDE5 + FDE4", "FDE1 + FDE3", "P4", "D7"),
    ("G5", "Three workflows run offline against fixtures?", "FDE3 + domain", "FDE1 + FDE4", "P5", "D9"),
    ("G6", "Red-team / outage / cost gates fail closed?", "FDE5", "FDE2 + FDE3", "P6", "D10"),
    ("G7", "Clean-room + --final + hash --check?", "FDE3 + FDE5", "Full team + outsider", "P7", "D10"),
    ("G8", "13 defence elements rehearsed; recommendation clear?", "FDE1 leads", "Full team", "P8", "D10"),
    ("G9", "Readiness Board; Blockers=0; RC clean-room?", "FDE4 chairs", "FDE3 tech · FDE5 sec · FDE1 release", "P9", "D13"),
]

WORKFLOWS = [
    ("A", "Batch evidence", "FDE4", "FDE3", "FDE5", "FDE4", "batch_response.schema.json"),
    ("B", "PV intake", "FDE2", "FDE3", "FDE5", "FDE2 + FDE4", "pv_response.schema.json"),
    ("C", "Supply options", "FDE1", "FDE3", "FDE5", "FDE1 + FDE4", "supply_response.schema.json"),
    ("Shared", "authZ / contracts / evidence-resolver", "—", "FDE3", "FDE5", "FDE5 + FDE4", "shared modules"),
]

OWES = [
    ("FDE1", "01–04, 26, 29, 30; WF C", "Release decision; L1 runbook; G9 minutes"),
    ("FDE2", "05–08; inject map; WF B", "RC domain regression sign-off"),
    ("FDE3", "09–12; app/src/scripts; clean-room", "RC tag, packaging, rollback, manifest"),
    ("FDE4", "13–15, 19–21; WF A; GxP proof", "Chair 28 board; residual risk sign"),
    ("FDE5", "16–18, 22–25, 27; security tests", "SLO/observability; RC retest; G9 sec sign"),
]

HEADER_FILL = PatternFill("solid", fgColor="1F4E79")
HEADER_FONT = Font(color="FFFFFF", bold=True, size=11)
LANE_FILLS = {
    "FDE1": PatternFill("solid", fgColor="D6EAF8"),
    "FDE2": PatternFill("solid", fgColor="D5F5E3"),
    "FDE3": PatternFill("solid", fgColor="FCF3CF"),
    "FDE4": PatternFill("solid", fgColor="FADBD8"),
    "FDE5": PatternFill("solid", fgColor="E8DAEF"),
}
GATE_FILL = PatternFill("solid", fgColor="F5B041")
TRACK_B_FILL = PatternFill("solid", fgColor="D5D8DC")
META_FILL = PatternFill("solid", fgColor="D6DBDF")
THIN = Border(
    left=Side(style="thin", color="BFBFBF"),
    right=Side(style="thin", color="BFBFBF"),
    top=Side(style="thin", color="BFBFBF"),
    bottom=Side(style="thin", color="BFBFBF"),
)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(wrap_text=True, vertical="center", horizontal="center")

REQUIRED_SHEETS = [
    "Instructions",
    "Phase_Matrix",
    "Day_Matrix",
    "Phase_Tasks",
    "Day_Tasks",
    "Gate_RACI",
    "Workflow_RACI",
    "Owes",
]


def style_header(ws, row: int = 1, cols: int | None = None) -> None:
    cols = cols or ws.max_column
    for col in range(1, cols + 1):
        cell = ws.cell(row, col)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        cell.border = THIN


def autosize(ws, min_w: int = 10, max_w: int = 42) -> None:
    for col in range(1, ws.max_column + 1):
        letter = get_column_letter(col)
        width = min_w
        for row in range(1, min(ws.max_row, 80) + 1):
            val = ws.cell(row, col).value
            if val is None:
                continue
            width = max(width, min(max_w, len(str(val)) + 2))
        ws.column_dimensions[letter].width = width


def apply_grid(ws, start_row: int = 1) -> None:
    for row in ws.iter_rows(min_row=start_row, max_row=ws.max_row, max_col=ws.max_column):
        for cell in row:
            cell.border = THIN
            if cell.alignment.wrap_text is not True:
                cell.alignment = WRAP


def add_status_validation(ws, col_letter: str, start_row: int, end_row: int) -> None:
    dv = DataValidation(
        type="list",
        formula1='"Not Started,In Progress,Blocked,Done,N/A"',
        allow_blank=True,
    )
    dv.error = "Pick a status"
    dv.errorTitle = "Invalid status"
    ws.add_data_validation(dv)
    dv.add(f"{col_letter}{start_row}:{col_letter}{end_row}")


def sheet_instructions(wb: Workbook) -> None:
    ws = wb.active
    ws.title = "Instructions"
    lines = [
        ("AEGIS Project Swimlane Tracker V2", True),
        ("Source: AEGIS_PROJECT_SWIMLANE_V2.md + AEGIS_PROJECT_PLAN_V2.md", False),
        ("Classification: Synthetic training only — not for real GxP / PV / supply / recall decisions.", False),
        ("Seat labels: FDE1–FDE5 (plan people seats; formerly P1–P5). Phase IDs remain P0–P9.", False),
        ("", False),
        ("Sheets", True),
        ("Phase_Matrix — phases as rows; Author/Must-review from Gate_RACI; seats FDE1–FDE5 as columns", False),
        ("Day_Matrix — days as rows; Author/Must-review from Gate_RACI; seats FDE1–FDE5 as columns", False),
        ("RACI SoT: Gate_RACI = Plan V2 §8.2. Phase/Day focus text must not invent different must-reviewers.", False),
        ("Phase_Tasks — flat tracker: one row per seat × phase (50 = 10×5)", False),
        ("Day_Tasks — flat tracker: one row per seat × day (70 = 14×5)", False),
        ("Gate_RACI — gate author / reviewers mapped to phase + day", False),
        ("Workflow_RACI — Workflow A/B/C + shared resolver ownership", False),
        ("Owes — G8 defence owes and G9 extras by seat", False),
        ("", False),
        ("Rules from plan", True),
        ("Agents / model-inference OFF until G4 PASS; deterministic core always on.", False),
        ("POC build order (phase P5): evidence-resolver → Workflow A → C → B.", False),
        ("Track A = D1–D10 / P0–P8 / G1–G8 (40h). Track B = D11–D14 / P9 / G9 (optional).", False),
        ("Never claim production-ready without G9.", False),
        ("Writable boundary: submission/ only. Challenge evidence immutable.", False),
        ("", False),
        ("Regenerate + validate", True),
        ("python -B submission/artefacts/ProjectPlan/_build_swimlane_tracker_v2.py", False),
        ("python -B submission/artefacts/ProjectPlan/_build_swimlane_tracker_v2.py --validate-only", False),
    ]
    for i, (text, bold) in enumerate(lines, 1):
        cell = ws.cell(i, 1, text)
        cell.font = Font(bold=bold, size=14 if i == 1 else 11)
        cell.alignment = WRAP
    ws.column_dimensions["A"].width = 110


def _gate_meta_by_phase() -> dict[str, tuple[str, str]]:
    """phase_id -> (author, must_review) from GATES SoT."""
    return {phase: (author, review) for _g, _q, author, review, phase, _d in GATES}


def _gate_meta_by_day() -> dict[str, tuple[str, str, str]]:
    """day_id -> (gate, author, must_review). Multi-gate days use combined labels."""
    by_day: dict[str, list[tuple[str, str, str]]] = {}
    for gate, _q, author, review, _phase, day in GATES:
        by_day.setdefault(day, []).append((gate, author, review))
    out: dict[str, tuple[str, str, str]] = {}
    for day, items in by_day.items():
        if len(items) == 1:
            g, a, r = items[0]
            out[day] = (g, a, r)
        else:
            out[day] = (
                " / ".join(i[0] for i in items),
                " / ".join(i[1] for i in items),
                " / ".join(i[2] for i in items),
            )
    # D10 carries G6–G8 in calendar even though Gate_RACI lists each separately
    out["D10"] = (
        "G6–G8",
        "G6:FDE5 · G7:FDE3+FDE5 · G8:FDE1",
        "G6:FDE2+FDE3 · G7/G8:Full team",
    )
    return out


def sheet_phase_matrix(wb: Workbook) -> None:
    """Phases as rows, seats as columns (transposed). Author/Must-review from Gate_RACI."""
    ws = wb.create_sheet("Phase_Matrix")
    headers = [
        "Phase",
        "Phase Name",
        "Hours",
        "Exit Gate",
        "Author / Chair",
        "Must Review",
        "Track",
        "Option B+ Days",
    ]
    for seat, stream, role in SEATS:
        headers.append(f"{seat} · {stream}\n{role}")
    ws.append(headers)
    style_header(ws)

    seat_start = 9
    for c, (seat, _stream, _role) in enumerate(SEATS, start=seat_start):
        cell = ws.cell(1, c)
        cell.fill = LANE_FILLS[seat]
        cell.font = Font(bold=True, size=11)
        cell.alignment = CENTER

    gate_by_phase = _gate_meta_by_phase()
    for ph, name, start, end, gate, track, days in PHASES:
        hours = f"{start}–{end}" if start is not None else "+16–24"
        author, review = gate_by_phase.get(ph, ("—", "—"))
        row = [ph, name, hours, gate, author, review, track, ", ".join(days)]
        for seat, _stream, _role in SEATS:
            row.append(PHASE_LANE[ph][seat])
        ws.append(row)
        r = ws.max_row
        is_track_b = track == "B"
        for c in range(1, seat_start):
            cell = ws.cell(r, c)
            cell.fill = TRACK_B_FILL if is_track_b else META_FILL
            cell.font = Font(bold=(c == 1))
            if c in {1, 3, 4, 7}:
                cell.alignment = CENTER
        for c, (seat, _stream, _role) in enumerate(SEATS, start=seat_start):
            cell = ws.cell(r, c)
            cell.fill = TRACK_B_FILL if is_track_b else LANE_FILLS[seat]
        if gate and gate != "—":
            ws.cell(r, 4).fill = GATE_FILL
            ws.cell(r, 4).font = Font(bold=True)
            ws.cell(r, 5).fill = GATE_FILL
            ws.cell(r, 6).fill = GATE_FILL
        ws.row_dimensions[r].height = 48

    apply_grid(ws)
    ws.row_dimensions[1].height = 48
    ws.freeze_panes = "I2"
    autosize(ws, min_w=12, max_w=32)
    ws.column_dimensions["A"].width = 8
    ws.column_dimensions["B"].width = 18
    ws.column_dimensions["C"].width = 10
    ws.column_dimensions["D"].width = 12
    ws.column_dimensions["E"].width = 22
    ws.column_dimensions["F"].width = 28
    ws.column_dimensions["G"].width = 8
    ws.column_dimensions["H"].width = 16
    for c in range(seat_start, seat_start + len(SEATS)):
        ws.column_dimensions[get_column_letter(c)].width = 30


def sheet_day_matrix(wb: Workbook) -> None:
    """Days as rows, seats as columns. Author/Must-review from Gate_RACI."""
    ws = wb.create_sheet("Day_Matrix")
    headers = [
        "Day",
        "Day Focus",
        "Gate",
        "Author / Chair",
        "Must Review",
        "Phase(s)",
        "Track",
    ]
    for seat, stream, role in SEATS:
        headers.append(f"{seat} · {stream}\n{role}")
    ws.append(headers)
    style_header(ws)

    seat_start = 8
    for c, (seat, _stream, _role) in enumerate(SEATS, start=seat_start):
        cell = ws.cell(1, c)
        cell.fill = LANE_FILLS[seat]
        cell.font = Font(bold=True, size=11)
        cell.alignment = CENTER

    gate_by_day = _gate_meta_by_day()
    for day, focus, gate, phase, track in DAYS:
        g_meta = gate_by_day.get(day)
        if g_meta:
            gate_label, author, review = g_meta
        else:
            gate_label, author, review = gate, "—", "—"
        row = [day, focus, gate_label, author, review, phase, track]
        for seat, _stream, _role in SEATS:
            row.append(DAY_LANE[day][seat])
        ws.append(row)
        r = ws.max_row
        is_track_b = track == "B"
        for c in range(1, seat_start):
            cell = ws.cell(r, c)
            cell.fill = TRACK_B_FILL if is_track_b else META_FILL
            cell.font = Font(bold=(c == 1))
            if c in {1, 3, 6, 7}:
                cell.alignment = CENTER
        for c, (seat, _stream, _role) in enumerate(SEATS, start=seat_start):
            cell = ws.cell(r, c)
            cell.fill = TRACK_B_FILL if is_track_b else LANE_FILLS[seat]
        if gate_label and gate_label != "—":
            ws.cell(r, 3).fill = GATE_FILL
            ws.cell(r, 3).font = Font(bold=True)
            ws.cell(r, 4).fill = GATE_FILL
            ws.cell(r, 5).fill = GATE_FILL
        ws.row_dimensions[r].height = 48

    apply_grid(ws)
    ws.row_dimensions[1].height = 48
    ws.freeze_panes = "H2"
    autosize(ws, min_w=12, max_w=32)
    ws.column_dimensions["A"].width = 8
    ws.column_dimensions["B"].width = 40
    ws.column_dimensions["C"].width = 10
    ws.column_dimensions["D"].width = 28
    ws.column_dimensions["E"].width = 28
    ws.column_dimensions["F"].width = 12
    ws.column_dimensions["G"].width = 8
    for c in range(seat_start, seat_start + len(SEATS)):
        ws.column_dimensions[get_column_letter(c)].width = 30


def sheet_phase_tasks(wb: Workbook) -> None:
    ws = wb.create_sheet("Phase_Tasks")
    headers = [
        "Task ID",
        "Phase",
        "Phase Name",
        "Hours",
        "Exit Gate",
        "Track",
        "Option B+ Days",
        "Seat",
        "Stream",
        "Focus / Work Package",
        "Status",
        "% Complete",
        "Owner Name",
        "Reviewer",
        "Blockers / Remarks",
        "Actual Completion",
    ]
    ws.append(headers)
    style_header(ws)

    for ph, name, start, end, gate, track, days in PHASES:
        hours = f"{start}–{end}" if start is not None else "+16–24"
        for seat, stream, _role in SEATS:
            ws.append(
                [
                    f"PH-{ph}-{seat}",
                    ph,
                    name,
                    hours,
                    gate,
                    track,
                    ", ".join(days),
                    seat,
                    stream,
                    PHASE_LANE[ph][seat],
                    "Not Started",
                    0,
                    "",
                    "",
                    "",
                    "",
                ]
            )
            fill = TRACK_B_FILL if track == "B" else LANE_FILLS[seat]
            for c in range(1, len(headers) + 1):
                ws.cell(ws.max_row, c).fill = fill

    apply_grid(ws)
    add_status_validation(ws, "K", 2, ws.max_row)
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{ws.max_row}"
    autosize(ws)


def sheet_day_tasks(wb: Workbook) -> None:
    ws = wb.create_sheet("Day_Tasks")
    headers = [
        "Task ID",
        "Day",
        "Day Focus",
        "Gate",
        "Phase(s)",
        "Track",
        "Seat",
        "Stream",
        "Focus / Work Package",
        "Status",
        "% Complete",
        "Owner Name",
        "Reviewer",
        "Dependencies",
        "Blockers / Remarks",
        "Actual Completion",
    ]
    ws.append(headers)
    style_header(ws)

    for day, focus, gate, phase, track in DAYS:
        for seat, stream, _role in SEATS:
            ws.append(
                [
                    f"DY-{day}-{seat}",
                    day,
                    focus,
                    gate,
                    phase,
                    track,
                    seat,
                    stream,
                    DAY_LANE[day][seat],
                    "Not Started",
                    0,
                    "",
                    "",
                    "",
                    "",
                    "",
                ]
            )
            fill = TRACK_B_FILL if track == "B" else LANE_FILLS[seat]
            for c in range(1, len(headers) + 1):
                ws.cell(ws.max_row, c).fill = fill

    apply_grid(ws)
    add_status_validation(ws, "J", 2, ws.max_row)
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{ws.max_row}"
    autosize(ws)


def sheet_gate_raci(wb: Workbook) -> None:
    ws = wb.create_sheet("Gate_RACI")
    headers = [
        "Gate",
        "Checkpoint Question / Exit",
        "Author / Chair",
        "Must Review",
        "Phase",
        "Day",
        "Status",
        "Decision (PASS/FAIL/CONDITIONAL)",
        "Remediation Notes",
        "Signed By",
        "Date",
    ]
    ws.append(headers)
    style_header(ws)
    for gate, question, author, review, phase, day in GATES:
        ws.append(
            [gate, question, author, review, phase, day, "Not Started", "", "", "", ""]
        )
        for c in range(1, len(headers) + 1):
            if c > 1:
                ws.cell(ws.max_row, c).fill = PatternFill("solid", fgColor="FDEBD0")
    apply_grid(ws)
    add_status_validation(ws, "G", 2, ws.max_row)
    ws.freeze_panes = "A2"
    autosize(ws, max_w=50)


def sheet_workflow_raci(wb: Workbook) -> None:
    ws = wb.create_sheet("Workflow_RACI")
    headers = [
        "Workflow",
        "Name",
        "Domain Owner",
        "Builder",
        "Security",
        "Sign-off",
        "Contract",
        "Build Order",
        "Status",
        "Notes",
    ]
    ws.append(headers)
    style_header(ws)
    order = {"Shared": 0, "A": 1, "C": 2, "B": 3}
    for wf, name, domain, builder, sec, signoff, contract in WORKFLOWS:
        ws.append(
            [
                wf,
                name,
                domain,
                builder,
                sec,
                signoff,
                contract,
                order[wf],
                "Not Started",
                "execution_status must remain not_executed; no prohibited autonomy",
            ]
        )
    apply_grid(ws)
    add_status_validation(ws, "I", 2, ws.max_row)
    note = ws.cell(
        ws.max_row + 2,
        1,
        "Forbidden on all workflows: release/reject/reprocess/relabel/recall; "
        "final PV seriousness/causality/expectedness/reportability/signal confirm; "
        "reserve/allocate/ship/quality-status change. Build order: Shared → A → C → B.",
    )
    note.alignment = WRAP
    ws.merge_cells(start_row=note.row, start_column=1, end_row=note.row, end_column=10)
    autosize(ws)


def sheet_owes(wb: Workbook) -> None:
    ws = wb.create_sheet("Owes")
    headers = [
        "Seat",
        "Stream",
        "By G8 (Defence)",
        "Extra by G9 (Track B)",
        "G8 Status",
        "G9 Status",
        "Owner Name",
        "Notes",
    ]
    ws.append(headers)
    style_header(ws)
    stream_by_seat = {s[0]: s[1] for s in SEATS}
    for seat, by_g8, by_g9 in OWES:
        ws.append(
            [seat, stream_by_seat[seat], by_g8, by_g9, "Not Started", "Not Started", "", ""]
        )
        fill = LANE_FILLS[seat]
        for c in range(1, len(headers) + 1):
            ws.cell(ws.max_row, c).fill = fill
    apply_grid(ws)
    add_status_validation(ws, "E", 2, ws.max_row)
    add_status_validation(ws, "F", 2, ws.max_row)
    autosize(ws, max_w=55)


def build() -> Path:
    wb = Workbook()
    sheet_instructions(wb)
    sheet_phase_matrix(wb)
    sheet_day_matrix(wb)
    sheet_phase_tasks(wb)
    sheet_day_tasks(wb)
    sheet_gate_raci(wb)
    sheet_workflow_raci(wb)
    sheet_owes(wb)
    wb.save(OUT)
    return OUT


def _fde_seats_in(text: str) -> set[str]:
    return set(re.findall(r"FDE[1-5]", text or ""))


def _claimed_must_reviewers(focus_by_seat: dict[str, str], gate: str) -> set[str]:
    """Seats whose focus claims Must-review for this gate (excludes 'not G# must-review')."""
    claimed: set[str] = set()
    # Skip multi-gate calendar labels (e.g. G6–G8); single gates G1–G9 are checked.
    if not gate or gate == "—" or "–" in gate or "-" in gate and gate.count("G") > 1:
        return claimed
    pat = re.compile(rf"Must-review\s+{re.escape(gate)}\b", re.I)
    neg = re.compile(rf"not\s+{re.escape(gate)}\s+must-review", re.I)
    for seat, focus in focus_by_seat.items():
        text = focus or ""
        if neg.search(text):
            continue
        if pat.search(text):
            claimed.add(seat)
    return claimed


def validate(path: Path = OUT) -> list[str]:
    """Return list of validation errors (empty = PASS)."""
    errors: list[str] = []
    if not path.exists():
        return [f"Missing file: {path}"]

    wb = load_workbook(path, data_only=True)
    for name in REQUIRED_SHEETS:
        if name not in wb.sheetnames:
            errors.append(f"Missing sheet: {name}")
    if errors:
        return errors

    pm_seat_start = 9
    dm_seat_start = 8

    # Phase_Matrix: rows = phases, cols = seats
    pm = wb["Phase_Matrix"]
    if pm.cell(1, 1).value != "Phase":
        errors.append("Phase_Matrix: expected header col A = 'Phase' (phases as rows)")
    if pm.cell(1, 5).value != "Author / Chair":
        errors.append("Phase_Matrix: missing Author / Chair column (E)")
    if pm.cell(1, 6).value != "Must Review":
        errors.append("Phase_Matrix: missing Must Review column (F)")
    for i, seat in enumerate(SEAT_IDS):
        header = str(pm.cell(1, pm_seat_start + i).value or "")
        if not header.startswith(seat):
            errors.append(
                f"Phase_Matrix: expected seat column {pm_seat_start+i} to start with {seat}, got {header!r}"
            )
    phase_rows = [pm.cell(r, 1).value for r in range(2, pm.max_row + 1) if pm.cell(r, 1).value]
    if phase_rows != PHASE_IDS:
        errors.append(f"Phase_Matrix phases mismatch: {phase_rows} != {PHASE_IDS}")

    p5_row = PHASE_IDS.index("P5") + 2
    fde3_col = pm_seat_start + SEAT_IDS.index("FDE3")
    got = pm.cell(p5_row, fde3_col).value
    exp = PHASE_LANE["P5"]["FDE3"]
    if got != exp:
        errors.append(f"Phase_Matrix P5/FDE3 expected {exp!r}, got {got!r}")

    # Day_Matrix
    dm = wb["Day_Matrix"]
    if dm.cell(1, 1).value != "Day":
        errors.append("Day_Matrix: expected header col A = 'Day'")
    if dm.cell(1, 4).value != "Author / Chair":
        errors.append("Day_Matrix: missing Author / Chair column (D)")
    if dm.cell(1, 5).value != "Must Review":
        errors.append("Day_Matrix: missing Must Review column (E)")
    day_rows = [dm.cell(r, 1).value for r in range(2, dm.max_row + 1) if dm.cell(r, 1).value]
    if day_rows != DAY_IDS:
        errors.append(f"Day_Matrix days mismatch: {day_rows}")
    for i, seat in enumerate(SEAT_IDS):
        header = str(dm.cell(1, dm_seat_start + i).value or "")
        if not header.startswith(seat):
            errors.append(f"Day_Matrix: expected seat column {dm_seat_start+i} to start with {seat}")

    # Phase_Tasks / Day_Tasks counts + sync with matrices
    pt = wb["Phase_Tasks"]
    dt = wb["Day_Tasks"]
    pt_n = max(0, pt.max_row - 1)
    dt_n = max(0, dt.max_row - 1)
    if pt_n != 50:
        errors.append(f"Phase_Tasks row count {pt_n} != 50")
    if dt_n != 70:
        errors.append(f"Day_Tasks row count {dt_n} != 70")

    seats_pt = {pt.cell(r, 8).value for r in range(2, pt.max_row + 1)}
    seats_dt = {dt.cell(r, 7).value for r in range(2, dt.max_row + 1)}
    if seats_pt != set(SEAT_IDS):
        errors.append(f"Phase_Tasks seats {seats_pt} != {set(SEAT_IDS)}")
    if seats_dt != set(SEAT_IDS):
        errors.append(f"Day_Tasks seats {seats_dt} != {set(SEAT_IDS)}")

    for r in range(2, pt.max_row + 1):
        seat = pt.cell(r, 8).value
        if seat in {"P1", "P2", "P3", "P4", "P5"}:
            errors.append(f"Phase_Tasks still uses legacy seat label {seat}")
        ph = pt.cell(r, 2).value
        focus = pt.cell(r, 10).value
        if ph in PHASE_LANE and seat in PHASE_LANE[ph] and focus != PHASE_LANE[ph][seat]:
            errors.append(f"Phase_Tasks {ph}/{seat} focus out of sync with PHASE_LANE")
    for r in range(2, dt.max_row + 1):
        seat = dt.cell(r, 7).value
        if seat in {"P1", "P2", "P3", "P4", "P5"}:
            errors.append(f"Day_Tasks still uses legacy seat label {seat}")
        day = dt.cell(r, 2).value
        focus = dt.cell(r, 9).value
        if day in DAY_LANE and seat in DAY_LANE[day] and focus != DAY_LANE[day][seat]:
            errors.append(f"Day_Tasks {day}/{seat} focus out of sync with DAY_LANE")

    for r in range(2, min(pt.max_row, 6) + 1):
        tid = str(pt.cell(r, 1).value or "")
        if not re.match(r"^PH-P\d-FDE\d$", tid):
            errors.append(f"Phase_Tasks bad Task ID pattern: {tid}")
    for r in range(2, min(dt.max_row, 6) + 1):
        tid = str(dt.cell(r, 1).value or "")
        if not re.match(r"^DY-D\d+-FDE\d$", tid):
            errors.append(f"Day_Tasks bad Task ID pattern: {tid}")

    # Gate_RACI SoT vs Plan V2 §8.2 expected reviewers
    plan_must_review = {
        "G1": {"FDE4", "FDE5"},
        "G2": {"FDE1", "FDE4"},
        "G3": {"FDE2", "FDE5"},
        "G4": {"FDE1", "FDE3"},
        "G5": {"FDE1", "FDE4"},
        "G6": {"FDE2", "FDE3"},
    }
    gr = wb["Gate_RACI"]
    gates = [gr.cell(r, 1).value for r in range(2, gr.max_row + 1) if gr.cell(r, 1).value]
    expected_gates = [g[0] for g in GATES]
    if gates != expected_gates:
        errors.append(f"Gate_RACI gates mismatch: {gates}")

    gate_sheet: dict[str, tuple[str, str]] = {}
    for r in range(2, gr.max_row + 1):
        gate = gr.cell(r, 1).value
        if not gate:
            continue
        author = str(gr.cell(r, 3).value or "")
        review = str(gr.cell(r, 4).value or "")
        gate_sheet[str(gate)] = (author, review)
        if gate in plan_must_review:
            got_rev = _fde_seats_in(review)
            if got_rev != plan_must_review[gate]:
                errors.append(
                    f"Gate_RACI {gate} must-review {got_rev} != Plan §8.2 {plan_must_review[gate]}"
                )

    # Phase_Matrix Author/Must Review columns must match Gate_RACI
    for r in range(2, pm.max_row + 1):
        ph = pm.cell(r, 1).value
        gate = pm.cell(r, 4).value
        author = str(pm.cell(r, 5).value or "")
        review = str(pm.cell(r, 6).value or "")
        if gate in gate_sheet:
            exp_a, exp_r = gate_sheet[str(gate)]
            if author != exp_a or review != exp_r:
                errors.append(
                    f"Phase_Matrix {ph}/{gate} Author/Must-review ({author!r}/{review!r}) "
                    f"!= Gate_RACI ({exp_a!r}/{exp_r!r})"
                )
        # Focus-text must-review claims must match Gate_RACI
        if gate in plan_must_review:
            focus_by_seat = {
                seat: str(pm.cell(r, pm_seat_start + i).value or "")
                for i, seat in enumerate(SEAT_IDS)
            }
            claimed = _claimed_must_reviewers(focus_by_seat, str(gate))
            expected = plan_must_review[str(gate)]
            if claimed != expected:
                errors.append(
                    f"Phase_Matrix {ph}/{gate} focus Must-review seats {claimed} != {expected}"
                )

    # Day_Matrix single-gate days: Must Review column + focus claims
    day_to_gate = {d: g for g, _q, _a, _r, _p, d in GATES}
    # Prefer primary gate for days that appear once
    for r in range(2, dm.max_row + 1):
        day = dm.cell(r, 1).value
        gate_label = str(dm.cell(r, 3).value or "")
        author = str(dm.cell(r, 4).value or "")
        review = str(dm.cell(r, 5).value or "")
        if day in day_to_gate and gate_label in gate_sheet:
            exp_a, exp_r = gate_sheet[gate_label]
            if author != exp_a or review != exp_r:
                errors.append(
                    f"Day_Matrix {day}/{gate_label} Author/Must-review ({author!r}/{review!r}) "
                    f"!= Gate_RACI ({exp_a!r}/{exp_r!r})"
                )
        if gate_label in plan_must_review:
            focus_by_seat = {
                seat: str(dm.cell(r, dm_seat_start + i).value or "")
                for i, seat in enumerate(SEAT_IDS)
            }
            claimed = _claimed_must_reviewers(focus_by_seat, gate_label)
            expected = plan_must_review[gate_label]
            if claimed != expected:
                errors.append(
                    f"Day_Matrix {day}/{gate_label} focus Must-review seats {claimed} != {expected}"
                )

    # Workflow_RACI vs Plan §6.4
    expected_wf = {w[0]: w[2:6] for w in WORKFLOWS}
    wr = wb["Workflow_RACI"]
    wfs = [
        wr.cell(r, 1).value
        for r in range(2, wr.max_row + 1)
        if wr.cell(r, 1).value in {"A", "B", "C", "Shared"}
    ]
    if set(wfs) != {"A", "B", "C", "Shared"}:
        errors.append(f"Workflow_RACI missing workflows: {wfs}")
    for r in range(2, wr.max_row + 1):
        wf = wr.cell(r, 1).value
        if wf not in expected_wf:
            continue
        got_tuple = tuple(wr.cell(r, c).value for c in range(3, 7))
        if got_tuple != expected_wf[wf]:
            errors.append(f"Workflow_RACI {wf} RACI {got_tuple} != {expected_wf[wf]}")

    # Owes
    ow = wb["Owes"]
    owe_seats = [ow.cell(r, 1).value for r in range(2, ow.max_row + 1) if ow.cell(r, 1).value]
    if owe_seats != SEAT_IDS:
        errors.append(f"Owes seats {owe_seats} != {SEAT_IDS}")
    for r, (seat, by_g8, by_g9) in enumerate(OWES, start=2):
        if ow.cell(r, 1).value != seat:
            errors.append(f"Owes row {r} seat mismatch")
        if ow.cell(r, 3).value != by_g8 or ow.cell(r, 4).value != by_g9:
            errors.append(f"Owes {seat} deliverables out of sync")

    for ph in PHASE_IDS:
        for seat in SEAT_IDS:
            if not PHASE_LANE[ph].get(seat):
                errors.append(f"PHASE_LANE missing {ph}/{seat}")
    for day in DAY_IDS:
        for seat in SEAT_IDS:
            if not DAY_LANE[day].get(seat):
                errors.append(f"DAY_LANE missing {day}/{seat}")

    return errors


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    validate_only = "--validate-only" in argv
    if not validate_only:
        path = build()
        print(f"Wrote {path}")
    else:
        path = OUT
        print(f"Validate-only: {path}")

    errs = validate(path)
    if errs:
        print("VALIDATION FAIL")
        for e in errs:
            print(f"  - {e}")
        return 1
    print("VALIDATION PASS")
    print(f"  sheets={REQUIRED_SHEETS}")
    print(f"  Phase_Matrix: phases-as-rows × seats-as-cols (FDE1–FDE5)")
    print(f"  Day_Matrix: days-as-rows × seats-as-cols (FDE1–FDE5)")
    print("  Phase_Tasks=50 Day_Tasks=70 Gates=10 Workflows=4 Owes=5")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
