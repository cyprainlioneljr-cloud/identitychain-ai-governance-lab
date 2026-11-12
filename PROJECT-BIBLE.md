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
| [02 Registry and policy](sprint-02-registry-policy/README.md) | Synthetic agent registry, roles, scoped grants, default-deny decisions | Practice checks complete and published on the practice branch.| Missing-grant denial and matching-grant allowance captured. |
| [03 Joiner](sprint-03-joiner/README.md) | Ownership, approval, issuance, and scoped access | Local Joiner exercise verified. | Approval, policy, scoped access, and expiry results captured. |
| [04 Mover](sprint-04-mover/README.md) | Replace access, handle retries and stale events | Mover exercise verified locally and merged into main. | Before and after access, stale denial, and duplicate retry captured. |
| [05 Leaver](sprint-05-leaver/README.md) | Disable agents, revoke grants, invalidate prior sessions | Local Leaver exercise verified. | Baseline access, offboarding denial, and outdated session denial captured. |
| [06 Audit](sprint-06-audit/README.md) | Correlated lifecycle and decision records, policy provenance | Local audit exercise verified. | Linked records and three review conditions captured, plus fingerprint verification. |
| 07 Review and handoff | End-to-end JML run, residual-risk review, reproducibility | Planned | Pending reproducible run and evidence review |

Close a sprint when its acceptance checks have been run, evidence is embedded and indexed, and outstanding items are explicitly recorded.
