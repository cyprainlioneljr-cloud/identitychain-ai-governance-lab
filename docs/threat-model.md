# Threat model

Status: proposed controls. Verification is pending implementation.

## Assets and boundaries

Protect agent ownership records, policies, grants, session material, and the audit trail. Review the boundaries from GitHub to local policy loading, requester to lifecycle controller, agent to resource gateway, and runtime to audit storage. Assume synthetic identities and local resources.

| Threat | Planned control | Evidence to collect | Sprint |
| --- | --- | --- | --- |
| Unapproved or excessive grants | Require reviewer approval and explicit resource/action scope. Default to deny. | Missing approval rejected and out-of-scope request denied | 3 |
| Stale permissions after a role change | Remove obsolete grants before activating replacements. | Old permission denied after move | 4 |
| Session reuse after offboarding | Check agent status and authorization version on every request. | Previously accepted session denied after leaver event | 5 |
| Duplicate or out-of-order events | Deduplicate event IDs and reject invalid state transitions. | Duplicate and stale events leave grants unchanged | 4 |
| Unreviewed policy loaded locally | Pin a reviewed policy revision and record it in decisions. | Decision references expected revision | 6 |
| Missing or altered audit records | Correlate lifecycle and decision records, restrict writes, and reconcile missing events. | Reviewer detects missing correlated evidence | 6 |
| Secrets or personal data in GitHub | Use synthetic fixtures and sanitize evidence before committing. | Review of tracked files and evidence | 7 |

A compromised local host or maintainer account can undermine these controls. Production isolation and an independently protected audit store are outside the lab scope.
