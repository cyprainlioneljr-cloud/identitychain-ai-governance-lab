# Project Bible

## Working decisions

- Repository name: `identitychain-ai-governance-lab`. Public on GitHub under `cyprainlioneljr-cloud`.
- JML is the primary use case. Use synthetic agent identities and local resources.
- Target $0/month, capped at $25/month. Apply the charter's verification and approval gate before billable deployment.
- Every sprint owns a `screenshots/` folder. In its README, use numbered headings in execution order, embed each visual at full available width, explain what it shows, and include a screenshot index. Distinguish design diagrams from captured evidence. Mark uncaptured evidence as pending.

## Sprint tracker

| Sprint | Scope | Delivery status | Evidence status |
| --- | --- | --- | --- |
| 01 Foundation | Charter, architecture, threat model, repo structure | Complete. Foundation published on GitHub. | Design diagrams and local verification record available. Published branch verified and repository screenshot captured. |
| 02 Registry and policy | Synthetic agent registry, roles, scoped grants, default-deny decisions | Planned | Pending local allow/deny evidence |
| 03 Joiner | Ownership, approval, issuance, and scoped access | Planned | Pending approval and access decisions |
| 04 Mover | Replace access, handle retries and stale events | Planned | Pending old/new access and replay checks |
| 05 Leaver | Disable agents, revoke grants, invalidate prior sessions | Planned | Pending post-revocation denial |
| 06 Audit | Correlated lifecycle and decision records, policy provenance | Planned | Pending audit trace and reconciliation |
| 07 Review and handoff | End-to-end JML run, residual-risk review, reproducibility | Planned | Pending reproducible run and evidence review |

Close a sprint when its acceptance checks have been run, evidence is embedded and indexed, and outstanding items are explicitly recorded.
