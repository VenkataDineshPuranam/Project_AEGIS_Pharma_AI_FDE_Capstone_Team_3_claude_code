# Project AEGIS-PHARMA — Delivery Swimlanes (V2)

> Derived from `AEGIS_PROJECT_PLAN_V2.md` §§5–8, §6.5 parallel streams, Option B+ calendar.  
> **Classification:** Synthetic training only — not for real GxP / clinical / PV / supply / recall decisions.

| Field | Entry |
|---|---|
| Title | Track A / Track B swimlanes by seat (P1–P5) |
| Source of truth | `AEGIS_PROJECT_PLAN_V2.md` |
| Version / date | **V2.0** — 2026-08-05 |
| Status | Companion visual to governing plan |
| Excel tracker | `AEGIS_PROJECT_SWIMLANE_TRACKER_V2.xlsx` — phase/day matrices (phases & days as rows; seats FDE1–FDE5 as columns) + task rows (regenerate/validate via `_build_swimlane_tracker_v2.py`) |

**How to read:** each horizontal lane is a seat/stream. Time runs left → right (phases P0–P9 / gates G1–G9). Boxes are that seat’s parallel focus from the plan; diamonds are shared gates.

---

## 1. Seat lanes × phases (Track A + optional P9)

```mermaid
flowchart LR
  %% Shared gate spine
  subgraph GATES["Shared gates"]
    direction LR
    PF((Preflight)) --> G1((G1)) --> G2((G2)) --> G3((G3)) --> G4((G4)) --> G5((G5)) --> G6((G6)) --> G7((G7)) --> G8((G8)) --> G9((G9))
  end

  subgraph V["P1 · Value stream V"]
    direction LR
    V0["P0: charter / plan ratify"] --> V1["P1: 01–04 + prod NFRs"]
    V1 --> V2["P2: must-review G2 (with FDE4)"]
    V2 --> V3["P3: architecture support (not G3 must-review)"]
    V3 --> V4["P4: must-review G4 — artefact 18 RAI"]
    V4 --> V5["P5: Workflow C domain + UX"]
    V5 --> V6["P6: FinOps 23 + delivery FinOps"]
    V6 --> V7["P7: 26 TOM + 29 runway"]
    V7 --> V8["P8: pitch 30 + ship decision"]
    V8 --> V9["P9: release decision / L1 runbook"]
  end

  subgraph D["P2 · Domain stream D"]
    direction LR
    D0["P0: case + inject skim"] --> D1["P1: inject skim support"]
    D1 --> D2["P2: author G2 — 05–08 + 84-inject register"]
    D2 --> D3["P3: must-review G3 — RTM 09 + language"]
    D3 --> D4["P4: domain support (not G4 must-review)"]
    D4 --> D5["P5: Workflow B domain rules"]
    D5 --> D6["P6: clinical/PV inject suites"]
    D6 --> D7["P7: domain freeze sign"]
    D7 --> D8["P8: defence domain demos"]
    D8 --> D9["P9: RC domain regression"]
  end

  subgraph A["P3 · Architecture / Build stream A"]
    direction LR
    A0["P0: scaffold + Hour-0 archive"] --> A1["P1: scripts skeleton"]
    A1 --> A2["P2: RTM / RELATIONSHIP_MODEL start"]
    A2 --> A3["P3: 10–12 + evidence-resolver"]
    A3 --> A4["P4: Cursor evidence; build prep"]
    A4 --> A5["P5: build A→C→B + app + scripts"]
    A5 --> A6["P6: adapter wire + outage path"]
    A6 --> A7["P7: evidence files + clean-room"]
    A7 --> A8["P8: freeze + hash"]
    A8 --> A9["P9: RC packaging / rollback / tag"]
  end

  subgraph Q["P4 · GxP / Quality stream Q"]
    direction LR
    Q0["P0: constraints catalogue"] --> Q1["P1: constraints + G1 review"]
    Q1 --> Q2["P2: must-review G2 — authority / lineage"]
    Q2 --> Q3["P3: co-author G3 — 13–15 GxP/CSA/QRM"]
    Q3 --> Q4["P4: co-author G4 — 19–21 ISO / EU AI Act"]
    Q4 --> Q5["P5: must-review G5 — Workflow A readiness"]
    Q5 --> Q6["P6: reg-authority suites"]
    Q6 --> Q7["P7: 27/28 draft + G7"]
    Q7 --> Q8["P8: GxP defence proof"]
    Q8 --> Q9["P9: chair Readiness Board 28"]
  end

  subgraph S["P5 · Security / Eval stream S"]
    direction LR
    S0["P0: constraints catalogue"] --> S1["P1: NFR / threat notes"]
    S1 --> S2["P2: privacy/eval support (not G2 must-review)"]
    S2 --> S3["P3: must-review G3 — threat skeleton + contracts"]
    S3 --> S4["P4: author G4 — 16–17 + failing prohibited tests"]
    S4 --> S5["P5: golden/edge/adversarial tests"]
    S5 --> S6["P6: author G6 — runner/graders/policies/reports"]
    S6 --> S7["P7: runbooks + eval evidence"]
    S7 --> S8["P8: red-team / outage demos"]
    S8 --> S9["P9: SLO / sec retest / G9 sign"]
  end

  V1 -.-> G1
  D2 -.-> G2
  A3 -.-> G3
  S4 -.-> G4
  A5 -.-> G5
  S6 -.-> G6
  A7 -.-> G7
  V8 -.-> G8
  Q9 -.-> G9
```

**Agent freeze (plan DECISION):** no agent / model-inference feature coding until **G4 PASS**. Deterministic core always on.

**Build order inside P5 (plan DECISION G-24):** shared evidence-resolver → Workflow **A** → **C** → **B**.

---

## 2. Compact RACI swimlane (who owns what at each gate)

```mermaid
flowchart TB
  subgraph RACI["Gate ownership — primary lane / must-review"]
    direction TB
    subgraph g1["G1 Problem / no-AI / NFRs"]
      direction LR
      g1a["Author: P1"] --> g1b["Review: P4 + P5"]
    end
    subgraph g2["G2 Authority / identity / time / unit"]
      direction LR
      g2a["Author: FDE2"] --> g2b["Must-review: FDE1 + FDE4"]
    end
    subgraph g3["G3 Architecture / contracts / GxP"]
      direction LR
      g3a["Author: P3 + P4"] --> g3b["Review: P2 + P5"]
    end
    subgraph g4["G4 Threat / ISO / privacy — agents unlock after PASS"]
      direction LR
      g4a["Author: P5 + P4"] --> g4b["Review: P1 + P3"]
    end
    subgraph g5["G5 Three-workflow MVP offline"]
      direction LR
      g5a["Author: P3 + domain"] --> g5b["Review: P1 + P4"]
    end
    subgraph g6["G6 TEVV / red-team / cost"]
      direction LR
      g6a["Author: P5"] --> g6b["Review: P2 + P3"]
    end
    subgraph g7["G7 Clean-room + --final"]
      direction LR
      g7a["Author: P3 + P5"] --> g7b["Review: full team + outsider"]
    end
    subgraph g8["G8 Defence"]
      direction LR
      g8a["Author: P1 leads pitch"] --> g8b["Review: full team"]
    end
    subgraph g9["G9 Production Readiness Board Track B"]
      direction LR
      g9a["Chair: P4"] --> g9b["Tech P3 · Sec P5 · Release P1"]
    end
    g1 --> g2 --> g3 --> g4 --> g5 --> g6 --> g7 --> g8 --> g9
  end
```

---

## 3. Workflow RACI swimlane

```mermaid
flowchart LR
  subgraph WA["Workflow A — Batch evidence"]
    direction TB
    WA_D["Domain: P4"] --> WA_B["Builder: P3"] --> WA_S["Security: P5"] --> WA_X["Sign-off: P4"]
  end
  subgraph WB["Workflow B — PV intake"]
    direction TB
    WB_D["Domain: P2"] --> WB_B["Builder: P3"] --> WB_S["Security: P5"] --> WB_X["Sign-off: P2 + P4"]
  end
  subgraph WC["Workflow C — Supply options"]
    direction TB
    WC_D["Domain: P1"] --> WC_B["Builder: P3"] --> WC_S["Security: P5"] --> WC_X["Sign-off: P1 + P4"]
  end
  subgraph SH["Shared authZ / contracts / evidence-resolver"]
    direction TB
    SH_B["Builder: P3"] --> SH_S["Security: P5"] --> SH_X["Sign-off: P5 + P4"]
  end
```

**Forbidden on all lanes:** release/reject/reprocess/relabel/recall · final PV seriousness/causality/expectedness/reportability/signal confirm · reserve/allocate/ship/quality-status change. All responses keep `execution_status: "not_executed"`.

---

## 4. Option B+ day swimlanes (D1–D14)

Recommended ~4h sessions from plan §5.4. Lanes show primary owner; others support.

```mermaid
flowchart LR
  subgraph P1D["P1 Value"]
    direction LR
    P1D1["D1 SCQA"] --> P1D2["D2 business case / NFRs / G1"]
    P1D2 --> P1D8["D8 supply path start"]
    P1D8 --> P1D9["D9 WF C + MVP"]
    P1D9 --> P1D10["D10 FinOps + defence"]
    P1D10 --> P1D11["D11 support runbooks"]
    P1D11 --> P1D13["D13 release decision"]
  end

  subgraph P2D["P2 Domain"]
    direction LR
    P2D1["D1 case read"] --> P2D3["D3 DDD + data gov"]
    P2D3 --> P2D4["D4 ontology / KG / G2"]
    P2D4 --> P2D9["D9 WF B"]
    P2D9 --> P2D10["D10 inject suites"]
    P2D10 --> P2D13["D13 domain sign"]
  end

  subgraph P3D["P3 Build"]
    direction LR
    P3D1["D1 scaffold"] --> P3D5["D5 C4 ADR contracts / G3"]
    P3D5 --> P3D8["D8 WF A + resolver + shell"]
    P3D8 --> P3D9["D9 finish C+B / G5"]
    P3D9 --> P3D10["D10 clean-room / G7"]
    P3D10 --> P3D11["D11 packaging"]
    P3D11 --> P3D12["D12 rollback"]
    P3D12 --> P3D13["D13 RC tag / G9"]
  end

  subgraph P4D["P4 GxP / ISO"]
    direction LR
    P4D2["D2 G1 review"] --> P4D5["D5 GxP artefacts"]
    P4D5 --> P4D7["D7 ISO / EU AI Act / G4"]
    P4D7 --> P4D9["D9 WF A rules"]
    P4D9 --> P4D10["D10 assurance"]
    P4D10 --> P4D13["D13 chair board / G9"]
  end

  subgraph P5D["P5 Sec / Eval"]
    direction LR
    P5D2["D2 NFR lock"] --> P5D6["D6 threat + privacy tests"]
    P5D6 --> P5D7["D7 assurance + G4"]
    P5D7 --> P5D9["D9 AI-disabled tests"]
    P5D9 --> P5D10["D10 TEVV / G6"]
    P5D10 --> P5D11["D11 SLO"]
    P5D11 --> P5D12["D12 sec retest / backup"]
    P5D12 --> P5D13["D13 G9 sec sign"]
  end
```

| Day | Focus | Gate |
|---|---|---|
| D1 | Preflight + SCQA start | — |
| D2 | Business case, stakeholders, blueprint, prod NFRs | G1 |
| D3 | DDD + data gov + brownfield | — |
| D4 | Ontology + KG + inject map | G2 |
| D5 | C4 + ADR + contracts + GxP | G3 |
| D6 | Threat modelling + privacy + security tests | — |
| D7 | ISO 42001 + EU AI Act + assurance + human factors | G4 |
| D8 | Build WF A (+ resolver) + app shell; start C | — |
| D9 | Finish C + B; AI-disabled; MVP demo | G5 |
| D10 | TEVV / FinOps / clean-room / defence | G6–G8 |
| D11 | P9: SLO, runbooks, packaging | — |
| D12 | P9: security retest, backup/restore, rollback | — |
| D13 | Production Readiness Board + RC tag | G9 |
| D14 | Buffer / defect burn-down (optional) | — |

---

## 5. Phase hour map (Track A)

| Phase | Hours | Exit gate | Parallel focus (plan §8) |
|---|---:|---|---|
| P0 Preflight | 0–2 | Preflight | All: baseline PASS; ratify plan |
| P1 Discovery | 2–7 | G1 | P1: 01–04; P2 inject skim; P3 scripts; P4/P5 constraints |
| P2 Domain | 7–12 | G2 | P2: 05–08 + inject register; P3 RTM; P4 authority |
| P3 Architecture | 12–18 | G3 | P3: 10–12 + resolver; P4: 13–15; P5 threat + contracts |
| P4 Secure design | 18–23 | G4 | P5: 16–17 + failing tests; P4: 19–21; P1: 18 |
| P5 POC build | 23–31 | G5 @26 | P3 A→C→B + app; domain rules; P5 tests; AI-disabled |
| P6 TEVV | 31–35 | G6 @34 | P5 eval stack; P1 FinOps; red-team/outage |
| P7 Ops | 35–38 | G7 @38 | Runbooks; evidence; clean-room; 26–29 |
| P8 Defence | 38–40 | G8 | Pitch + 13 defence elements |
| P9 Hardening | +16–24 | G9 | Track B only — production-ready claim |

---

## 6. Owes by lane (defence / RC)

| Seat | By G8 | Extra by G9 |
|---|---|---|
| P1 | 01–04, 26, 29, 30; WF C | Release decision; L1 runbook; G9 minutes |
| P2 | 05–08; inject map; WF B | RC domain regression sign-off |
| P3 | 09–12; app/src/scripts; clean-room | RC tag, packaging, rollback, manifest |
| P4 | 13–15, 19–21; WF A; GxP proof | Chair 28 board; residual risk sign |
| P5 | 16–18, 22–25, 27; security tests | SLO/observability; RC retest; G9 sec sign |

---

## Traceability

| Diagram | Plan anchors |
|---|---|
| §1 phase swimlanes | §§6.1, 6.5, 8 |
| §2 gate RACI | §8.2 checkpoint questions |
| §3 workflow RACI | §6.4 |
| §4 Option B+ days | §5.4 |
| §5 hour map | §5.2, §9 |
| §6 owes | §17 |
