# Project AEGIS-PHARMA — Integrated Challenge Case

## 1. Organisation

**NovaCura Therapeutics Group (NTG)** is a fictional global pharmaceutical company operating discovery laboratories, clinical-development programmes, pharmacovigilance hubs, manufacturing plants, quality laboratories and distribution networks across India, Germany, Ireland, the United States, the UAE and Singapore.

Its portfolio includes:

- NCX-101, an oral small-molecule oncology product approaching patent expiry.
- NCB-204, a monoclonal-antibody biologic in pivotal trials and commercial scale-up.
- NCS-310, a sterile injectable supplied through hospital and compassionate-use channels.
- NCR-415, a rare-disease gene-therapy research programme acquired with a biotech subsidiary.

## 2. Situation

NTG has announced **Project AEGIS-PHARMA**, intended to reduce evidence-reconciliation time across development, quality, safety and supply operations. During the capstone window, a pivotal-trial amendment, a disputed biologics batch, emerging safety reports, a sterile-area excursion, a cold-chain failure, an excipient shortage, a ransomware event and a multi-agency inspection request converge.

The enterprise is fragmented across LIMS, MES, electronic batch records, QMS, RIM, EDC, eConsent, IRT, CTMS, safety databases, serialization platforms, data lakes, spreadsheets, vendor portals and research environments. Identifiers, timestamps, terminology, access controls and authority hierarchies are inconsistent.

## 3. Participant mandate

Design and demonstrate a defensible AI Forward Deployed Engineering intervention that can operate within this brownfield estate without taking over regulated human accountability. Participants may conclude that a workflow, knowledge graph or AI component is unjustified, but must prove the decision.

## 4. Mandatory workflows

### Workflow A — GxP evidence reconciliation for batch-review readiness

Reconcile batch genealogy, laboratory results, environmental monitoring, deviations, CAPA, change control, validation state, supplier evidence and release-packet completeness. The workflow may identify gaps, contradictions and evidence lineage. It must never release, reject, reprocess, re-label or recall a batch.

### Workflow B — Pharmacovigilance case-intake and signal-support workflow

Support intake, duplicate detection, terminology normalization, source authority, reporting-clock reconstruction, listedness evidence, product-quality linkage and multilingual review. It must never make final seriousness, causality, expectedness, reportability or signal-confirmation decisions.

### Workflow C — Bounded supply-shortage and cold-chain recovery planner

Generate traceable options using inventory, quality status, market authorization, trial demand, compassionate-use constraints, cold-chain evidence, CMO capacity, transport and allocation policy. It must never change inventory status, reserve capacity, allocate stock, release product or initiate a recall without explicit authorized human approval.

## 5. Required operating properties

Every workflow must demonstrate purpose limitation, least privilege, current authorization, evidence authority, temporal applicability, provenance, structured outputs, abstention, human review, idempotency, bounded steps, cost and token budgets, checkpointing, rollback, kill switch, degraded mode, auditability and AI-disabled continuity.

## 6. Embedded inject rule

All challenge conditions are disclosed below. There are no later instructor injects. Participants are expected to discover connections, contradictions and failure chains from the supplied evidence rather than receive staged surprises.

## 7. Inject catalogue

### D01 — Portfolio, strategy and product value
**INJ-001 — Board compression target.** The board requires a 14% reduction in end-to-end release lead time without changing registered specifications or weakening independent Quality authority. Evidence is distributed across `board_requests.csv; portfolio_products.csv`.
**INJ-002 — Conflicting success metrics.** Manufacturing rewards throughput, Quality rewards deviation containment, Supply rewards service level, and Clinical rewards database lock speed. Evidence is distributed across `kpi_conflicts.csv; stakeholders.csv`.
**INJ-003 — No-AI challenge.** A process-excellence team claims workflow redesign and master-data repair could deliver most value without generative AI. Evidence is distributed across `no_ai_baselines.csv`.
**INJ-004 — Patent-cliff urgency.** A major product loses exclusivity in 19 months, creating pressure to accelerate a new indication and reduce cost of goods. Evidence is distributed across `portfolio_products.csv; commercial_forecast.csv`.
**INJ-005 — Acquisition integration.** A recently acquired biotech uses incompatible identifiers, cloud tenancy and quality procedures. Evidence is distributed across `organisations.csv; system_inventory.csv`.
**INJ-006 — Prohibited optimization.** Executives prohibit any AI from autonomously changing formulation, specification, clinical eligibility, safety case disposition, batch release or recall decisions. Evidence is distributed across `ai_use_boundaries.csv`.
### D02 — Discovery, translational science and model risk
**INJ-007 — Assay drift.** A potency assay changed reagent lot and instrument firmware; historical comparability is disputed. Evidence is distributed across `assay_results.csv; instruments.csv; reagent_lots.csv`.
**INJ-008 — Compound genealogy collision.** Two acquired compounds share a local code but have different structures and salt forms. Evidence is distributed across `compounds.csv; substance_master.csv`.
**INJ-009 — Omics cohort bias.** A translational model was trained mainly on one ancestry group and underperforms on another. Evidence is distributed across `omics_cohorts.csv; model_performance.csv`.
**INJ-010 — Preclinical image manipulation concern.** Image metadata suggests duplicated microscopy panels in a CRO report. Evidence is distributed across `preclinical_studies.csv; image_forensics.csv`.
**INJ-011 — Unqualified research model.** A discovery model promoted into portfolio decisions has no approved intended-use statement or locked training set. Evidence is distributed across `model_registry.csv`.
**INJ-012 — Target-evidence conflict.** Internal experiments and an external licensed dataset disagree on target validation. Evidence is distributed across `target_evidence.csv; data_licenses.csv`.
### D03 — Clinical development and trial integrity
**INJ-013 — Protocol-version divergence.** Sites are executing three protocol versions; one country has not approved the latest amendment. Evidence is distributed across `clinical_trials.csv; protocol_versions.csv; site_approvals.csv`.
**INJ-014 — Eligibility ambiguity.** A participant meets central-lab criteria but not the local-lab range encoded by the EDC rule. Evidence is distributed across `subjects.csv; eligibility_evidence.csv`.
**INJ-015 — Randomization service outage.** The IRT service was unavailable and emergency kits were assigned using a manual log. Evidence is distributed across `randomization_events.csv; downtime_events.csv`.
**INJ-016 — Potential unblinding.** A support ticket exposes treatment-arm hints to site personnel. Evidence is distributed across `support_tickets.csv; access_logs.csv`.
**INJ-017 — eConsent withdrawal mismatch.** Consent was withdrawn in the eConsent platform but downstream biomarker processing continued. Evidence is distributed across `consents.csv; specimens.csv; processing_events.csv`.
**INJ-018 — Decentralized-device clock skew.** Wearable devices report timestamps in mixed local time and UTC with daylight-saving errors. Evidence is distributed across `wearable_readings.csv; timezone_rules.csv`.
**INJ-019 — Endpoint adjudication backlog.** Imaging endpoint packets contain missing source documents and conflicting reviewer conclusions. Evidence is distributed across `endpoint_packets.csv; imaging_reviews.csv`.
**INJ-020 — Site inspection risk.** A high-enrolling site has unusual data regularity, late source uploads and repeated credential sharing. Evidence is distributed across `site_metrics.csv; access_logs.csv`.
### D04 — GMP manufacturing, laboratories and batch release
**INJ-021 — Biologics batch genealogy break.** A single-use assembly lot is missing from one MES genealogy branch but appears in warehouse consumption. Evidence is distributed across `batches.csv; material_genealogy.csv; warehouse_movements.csv`.
**INJ-022 — Sterility excursion.** Environmental monitoring shows an excursion near fill-finish; organism identification was corrected after initial review. Evidence is distributed across `environmental_monitoring.csv; microbiology_results.csv`.
**INJ-023 — OOS/OOT disagreement.** LIMS marks an assay OOS, the statistical tool marks it OOT, and the laboratory notebook labels it invalid. Evidence is distributed across `lab_results.csv; oos_investigations.csv`.
**INJ-024 — Unit conversion defect.** A contract laboratory transmitted concentration in mg/L while the receiving interface assumed µg/mL. Evidence is distributed across `lab_results.csv; interface_mappings.csv`.
**INJ-025 — Electronic batch record exception.** A required step was completed during network degradation and back-entered after the operation. Evidence is distributed across `ebr_steps.csv; downtime_events.csv`.
**INJ-026 — Cleaning validation boundary.** Campaign sequencing changed after a new high-potency product was introduced. Evidence is distributed across `cleaning_validation.csv; production_schedule.csv`.
**INJ-027 — Process analytical technology drift.** A PAT model version changed without synchronized update to the batch record recipe. Evidence is distributed across `pat_models.csv; recipes.csv`.
**INJ-028 — Qualified Person evidence gap.** The EU release packet lacks confirmation of one contract-site audit commitment. Evidence is distributed across `release_packets.csv; supplier_audits.csv`.
### D05 — Quality systems, validation and data integrity
**INJ-029 — Audit-trail disabled.** A privileged account disabled audit capture for 47 minutes during master-data repair. Evidence is distributed across `audit_trails.csv; privileged_sessions.csv`.
**INJ-030 — Shared laboratory account.** Three analysts used a shared instrument account during night shift. Evidence is distributed across `access_logs.csv; staff_rosters.csv`.
**INJ-031 — Validation-state ambiguity.** The same application is labelled validated, conditionally released and research-only in three inventories. Evidence is distributed across `system_inventory.csv; validation_inventory.csv`.
**INJ-032 — Unapproved spreadsheet.** A macro-enabled spreadsheet calculates dissolution acceptance and has no verified version history. Evidence is distributed across `spreadsheet_inventory.csv`.
**INJ-033 — CAPA effectiveness failure.** A recurring deviation reappears after CAPA closure with a different taxonomy code. Evidence is distributed across `deviations.csv; capa_records.csv`.
**INJ-034 — Change-control bypass.** A vendor hotfix was installed under emergency change but never retrospectively approved. Evidence is distributed across `change_controls.csv; vendor_releases.csv`.
**INJ-035 — Record-retention conflict.** Legal hold, GxP retention and privacy deletion obligations point to different actions for the same records. Evidence is distributed across `retention_rules.csv; legal_holds.csv; deletion_requests.csv`.
**INJ-036 — ALCOA+ provenance break.** A PDF certificate was manually transcribed; the original signed source cannot be located. Evidence is distributed across `certificates_analysis.csv; document_lineage.csv`.
### D06 — Pharmacovigilance and benefit-risk
**INJ-037 — ICSR duplicate cluster.** Cases from a patient programme, literature vendor and call centre likely describe the same event under different product names. Evidence is distributed across `icsr_cases.csv; duplicate_candidates.csv`.
**INJ-038 — Reporting-clock conflict.** Awareness date differs across vendor receipt, affiliate inbox and global safety database. Evidence is distributed across `icsr_cases.csv; safety_receipts.csv`.
**INJ-039 — MedDRA version mismatch.** Coding was performed with two MedDRA versions, changing the preferred term and signal grouping. Evidence is distributed across `adverse_events.csv; terminology_versions.csv`.
**INJ-040 — Expectedness source conflict.** The investigator brochure, core data sheet and local label are not aligned. Evidence is distributed across `listedness_sources.csv; product_labels.csv`.
**INJ-041 — Pregnancy and paediatric sensitivity.** A narrative includes pregnancy exposure and a minor’s data within a general case queue. Evidence is distributed across `icsr_cases.csv; sensitive_segments.csv`.
**INJ-042 — Social-media authenticity.** A high-severity post cannot be linked to an identifiable reporter or patient. Evidence is distributed across `social_listening.csv`.
**INJ-043 — Product-quality and safety link.** A complaint about particles may relate to adverse events and a specific packaging lot. Evidence is distributed across `product_complaints.csv; icsr_cases.csv`.
**INJ-044 — Signal disproportionality instability.** A signal changes materially when duplicate suppression and exposure estimates are varied. Evidence is distributed across `signal_metrics.csv; exposure_estimates.csv`.
### D07 — Regulatory information and submissions
**INJ-045 — IDMP identity conflict.** Substance, strength and pharmaceutical-form codes differ across RIM, ERP and regional registrations. Evidence is distributed across `medicinal_products.csv; idmp_mappings.csv`.
**INJ-046 — Labeling divergence.** A risk statement is approved in the EU but pending in the US and absent in two distributor leaflets. Evidence is distributed across `product_labels.csv; market_authorisations.csv`.
**INJ-047 — Commitment deadline ambiguity.** A post-authorisation commitment has conflicting due dates in authority correspondence and the tracking system. Evidence is distributed across `regulatory_commitments.csv; authority_correspondence.csv`.
**INJ-048 — eCTD sequence gap.** A submission index references a document not present in the archived sequence. Evidence is distributed across `ectd_sequences.csv; document_catalog.csv`.
**INJ-049 — Variation classification dispute.** Regulatory teams disagree whether a manufacturing change is reportable before implementation. Evidence is distributed across `regulatory_changes.csv`.
**INJ-050 — Inspection request surge.** Regulators request traceable evidence spanning trial data, batch history, safety cases and AI-system controls within 72 hours. Evidence is distributed across `inspection_requests.csv`.
### D08 — Supply chain, serialization and anti-counterfeit
**INJ-051 — Cold-chain lane excursion.** A biologic shipment exceeds range; logger clocks and pallet association are disputed. Evidence is distributed across `shipments.csv; temperature_loggers.csv`.
**INJ-052 — Serialization aggregation break.** Case-to-pallet aggregation is missing after a line restart. Evidence is distributed across `serialisation_events.csv; packaging_events.csv`.
**INJ-053 — Counterfeit suspicion.** Two returned packs have valid-looking serials but inconsistent print and distribution history. Evidence is distributed across `returns.csv; serialisation_events.csv`.
**INJ-054 — Critical excipient shortage.** A sole-source excipient supplier reports contamination and an eight-week recovery estimate. Evidence is distributed across `supplier_risks.csv; inventory.csv`.
**INJ-055 — CMO capacity conflict.** The CMO promises capacity to two sponsors during the same campaign window. Evidence is distributed across `cmo_capacity.csv; vendor_contracts.csv`.
**INJ-056 — Allocation ethics.** Demand exceeds available stock across markets, trials and compassionate-use programmes. Evidence is distributed across `demand_forecast.csv; inventory.csv; allocation_constraints.csv`.
**INJ-057 — Customs documentation mismatch.** Shipment product description differs from the import licence and invoice. Evidence is distributed across `shipments.csv; trade_documents.csv`.
**INJ-058 — Recall-scope uncertainty.** Potentially affected lots share components, equipment and distribution routes but not all genealogy links are complete. Evidence is distributed across `recall_candidates.csv; material_genealogy.csv`.
### D09 — Privacy, ethics and cross-border data
**INJ-059 — Genomic re-identification risk.** A rare-disease dataset is nominally pseudonymised but contains highly identifying combinations. Evidence is distributed across `genomic_data.csv; privacy_risk.csv`.
**INJ-060 — Cross-border secondary use.** EU trial data is proposed for global model training under a purpose not explicit in the original consent. Evidence is distributed across `consents.csv; data_exports.csv`.
**INJ-061 — Data-subject request versus GxP record.** A participant requests deletion of data that may need preservation for trial integrity and legal obligations. Evidence is distributed across `deletion_requests.csv; retention_rules.csv`.
**INJ-062 — Patient-support programme leakage.** Free text contains diagnoses, financial hardship and family details beyond the stated purpose. Evidence is distributed across `patient_support_cases.csv`.
**INJ-063 — Research-commercial boundary.** Biomarker data licensed for research is being considered for commercial targeting. Evidence is distributed across `data_licenses.csv; commercial_use_requests.csv`.
**INJ-064 — Regional residency failure.** A backup replica places regulated personal data in an unapproved region. Evidence is distributed across `data_residency.csv; backup_inventory.csv`.
### D10 — Cybersecurity, agentic security and Zero Trust
**INJ-065 — Prompt injection in SOP.** A supplier deviation PDF includes hidden instructions asking the AI to ignore quality holds. Evidence is distributed across `knowledge_catalog.csv; MALICIOUS_SUPPLIER_DEVIATION.md`.
**INJ-066 — Tool-manifest poisoning.** A newly registered batch-status tool requests write access and silently changes a disposition field. Evidence is distributed across `tool_catalog.csv; tool_manifest_poisoned.json`.
**INJ-067 — Entitlement revocation lag.** A contractor’s access was revoked in IAM but remains cached in the AI gateway. Evidence is distributed across `users_entitlements.csv; access_cache.csv`.
**INJ-068 — Safety-data exfiltration.** A crafted query attempts to retrieve identifiable narratives across affiliates. Evidence is distributed across `security_events.csv`.
**INJ-069 — Ransomware and OT segmentation.** Manufacturing historians are isolated while MES and QMS operate in degraded mode. Evidence is distributed across `downtime_events.csv; network_zones.csv`.
**INJ-070 — Model supply-chain compromise.** A model package hash differs from the approved registry entry. Evidence is distributed across `model_registry.csv; model_artifacts.csv`.
### D11 — Human factors, responsible AI and adoption
**INJ-071 — Automation bias in batch review.** Reviewers accept an AI summary despite an omitted critical deviation. Evidence is distributed across `candidate_outputs.csv; reviewer_feedback.csv`.
**INJ-072 — Language inequity.** Safety narratives in Arabic and Hindi have lower extraction quality than English and German. Evidence is distributed across `model_performance.csv; icsr_cases.csv`.
**INJ-073 — Accessibility failure.** The proposed interface cannot be operated fully by keyboard and uses colour-only warnings. Evidence is distributed across `usability_findings.csv`.
**INJ-074 — Role conflict.** A global process owner wants uniform automation while local Qualified Persons and safety officers retain legal accountability. Evidence is distributed across `stakeholders.csv; decision_rights.csv`.
### D12 — Economics, token efficiency and vendor concentration
**INJ-075 — Model price shock.** The preferred model vendor increases input-token price by 70% and reduces batch discounts. Evidence is distributed across `model_costs.csv; vendor_contracts.csv`.
**INJ-076 — Denial-of-wallet pattern.** Repeated oversized document submissions create abnormal inference and embedding spend. Evidence is distributed across `model_usage.csv; security_events.csv`.
**INJ-077 — Hidden human-review cost.** The business case excludes medical, Quality and regulatory review time. Evidence is distributed across `cost_model.csv; staff_rates.csv`.
**INJ-078 — Vendor concentration.** The same provider hosts the model, vector store, evaluation service and observability pipeline. Evidence is distributed across `vendor_dependencies.csv`.
### D13 — Reliability, business continuity and retirement
**INJ-079 — Regional platform outage.** The primary AI region fails during batch review and expedited safety reporting. Evidence is distributed across `downtime_events.csv; model_endpoints.csv`.
**INJ-080 — Checkpoint corruption.** An agent resumes a supply-recovery plan from stale state and duplicates draft reservations. Evidence is distributed across `agent_runs.csv`.
**INJ-081 — Model substitution regression.** A smaller fallback model preserves schema compliance but loses evidence fidelity in non-English cases. Evidence is distributed across `model_performance.csv; model_endpoints.csv`.
**INJ-082 — AI-disabled continuity.** The organisation must operate safely for 14 days without any model inference. Evidence is distributed across `continuity_requirements.csv`.
**INJ-083 — Vendor exit deadline.** A strategic vendor will terminate service in 120 days and export formats are incomplete. Evidence is distributed across `vendor_contracts.csv; vendor_exit_assets.csv`.
**INJ-084 — Retirement and evidence preservation.** The AI service may be retired, but prompts, model versions, decisions and validation evidence must remain inspectable. Evidence is distributed across `retention_rules.csv; retirement_assets.csv`.

## 8. Required strategic decisions

Participants must explicitly decide and defend:

- Whether AI is justified against process redesign, rules, analytics and master-data remediation.
- Which records and systems are authoritative for each decision context and effective date.
- Whether a knowledge graph is necessary and which relations require graph reasoning.
- Which components are GxP-relevant, safety-relevant, regulated, validated or merely advisory.
- How electronic records, signatures, audit trails and generated evidence remain trustworthy.
- How local legal accountability is preserved across Quality, Safety, Clinical and Regulatory roles.
- How model, prompt, retrieval, tool and configuration changes are controlled and evaluated.
- How the system operates during model unavailability, vendor exit and ultimate retirement.

## 9. Definition of done

The capstone is complete only when another qualified team can reproduce the environment, execute the public tests, inspect the evidence, understand residual risks, operate the manual fallback and defend a go, conditional-go, pivot, pause or stop recommendation without oral knowledge from the builders.
