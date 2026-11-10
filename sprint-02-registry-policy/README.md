# Sprint 02 · Registry and Policy

This local exercise checks whether an active synthetic agent has both a role that permits reading sample reports and a grant for that specific action. It uses Python's standard library and costs $0 to run.

From the repository folder, run `python3 sprint-02-registry-policy/access.py`. The script reads [registry.json](registry.json) and [policy.json](policy.json) from its own folder.

## 01. Deny a request with no grant

![Terminal output showing denial when the agent has no matching grant](screenshots/01-deny-missing-grant.png)

With `"grants": []` in the registry, the active agent's reader role permitted the request, but the agent had no matching grant. The script denied the read.

## 02. Allow the same request after adding a grant

![Terminal output showing allowance when role and grant match](screenshots/02-allow-matching-grant.png)

Adding a grant for `read` on `sample-reports` changed the decision to allow. The role policy and request stayed the same. The saved registry includes this grant. To reproduce the first result, temporarily empty the grants list, run the script, and then restore the grant.

## Screenshot index

| Figure | File | Status |
| --- | --- | --- |
| 01 | [01-deny-missing-grant.png](screenshots/01-deny-missing-grant.png) | Captured locally |
| 02 | [02-allow-matching-grant.png](screenshots/02-allow-matching-grant.png) | Captured locally |

Both screenshots are cropped to the actual result lines to remove personal terminal details.

The two checks above cover the scripted read request. The practice script uses one fixed agent and request. Grant expiry and general request handling remain outside this exercise.
