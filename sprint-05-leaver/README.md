# Sprint 05 · Leaver

This local exercise offboards the synthetic catalog reader from Sprint 4 and checks what happens to its existing session.

From the repository folder, run `python3 sprint-05-leaver/leaver.py`.

## 01. Verify access before offboarding

![Version 2 session can read the catalog](screenshots/01-before.png)

The active agent has a catalog read grant and its version 2 session can use it.

## 02. Disable the agent and revoke grants

![Disabled agent has zero grants and the original session is denied](screenshots/02-offboarded.png)

The script disables the agent, clears its grants, and advances its authorization version to 3. The original version 2 session is denied because the agent is disabled.

## 03. Verify session version enforcement

![Active test copy rejects the outdated session](screenshots/03-stale-session.png)

A separate active test copy has a catalog grant at version 3. The original version 2 session is still denied, this time because its version is outdated.

## Screenshot index

| Figure | Evidence |
| --- | --- |
| 01 | [Before offboarding](screenshots/01-before.png) |
| 02 | [Offboarding and denial](screenshots/02-offboarded.png) |
| 03 | [Outdated session denial](screenshots/03-stale-session.png) |

The screenshots are cropped from actual Terminal output to remove personal paths and prompts. Agent state and the simulated session live in memory for one run. The exercise ran locally at $0.
