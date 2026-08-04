# Source-System Fact Pack

| Domain | Systems | Known condition |
|---|---|---|
| Discovery | ELN, assay platform, image repository, compound registry | Research identifiers collide after acquisition; metadata is incomplete. |
| Clinical | EDC, CTMS, eConsent, IRT, ePRO, wearable hub, imaging core lab | Protocol and consent versions are asynchronous; clocks differ. |
| Manufacturing | ERP, MES, eBR, historian, PAT, warehouse system | Genealogy breaks during downtime and vendor interfaces use different units. |
| Laboratory | LIMS, CDS, instrument PCs, notebooks, spreadsheets | Shared accounts, inconsistent OOS states and undocumented spreadsheets exist. |
| Quality | eQMS, document management, training, supplier quality | Deviation taxonomies and effective documents are inconsistent. |
| Safety | Global safety DB, affiliate inboxes, vendors, literature, call centre | Duplicate cases, versioned terminology and awareness dates conflict. |
| Regulatory | RIM, eCTD archive, labeling, IDMP/SPOR staging | Product identities and commitments are not synchronized. |
| Supply | Serialization, logistics, cold-chain, CMO portals | Aggregation and logger association can be incomplete. |
| AI platform | Gateway, model endpoints, vector store, tools, evaluator | Bundled vendor, stale entitlements, mutable manifests and weak cost controls. |

## Evidence hierarchy is contextual

No system is universally authoritative. Participants must define authority by business object, jurisdiction, effective time, process state and accountable role. A later timestamp is not automatically more authoritative than an approved signed record.
