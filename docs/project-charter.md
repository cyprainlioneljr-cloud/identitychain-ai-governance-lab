# Project charter

## Purpose

Show how an organization can grant, change, and revoke an AI agent's access as its owner, role, or operating status changes. Use GitHub to review policies and track evidence, and run the lab locally with synthetic identities and resources.

## Scope and success criteria

| Lifecycle event | Expected outcome | Acceptance evidence |
| --- | --- | --- |
| Joiner | A named owner and reviewer approve a scoped, expiring grant. | Approved request, allowed in-scope decision, denied out-of-scope decision |
| Mover | Superseded grants are revoked before new grants take effect. | Before-and-after grant records and denial under the old role |
| Leaver | The agent is disabled, grants are revoked, and prior sessions are rejected. | Revocation event and denied request with a previously valid session |
| Audit | A reviewer can trace a lifecycle request through approval, enforcement, and outcome. | Correlated records with policy revision and event IDs |

In scope: an agent registry, policy decisions, lifecycle workflows, local enforcement, and audit evidence. Out of scope: production accounts, live credentials, production connectors, and cloud infrastructure.

## Ownership and cost

The maintainer approves scope and spending. A reviewer checks policy changes and evidence. Agent owners request changes and attest to access needs. These are lab roles and can be simulated with separate identities.

Target spend is $0/month. The ceiling is $25/month. Before any billable deployment, verify current pricing and free-tier limits, record a monthly estimate including usage and storage, and obtain explicit approval. Keep the lab local until those conditions are met.
