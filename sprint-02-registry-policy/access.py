import json
from pathlib import Path

folder = Path(__file__).resolve().parent
registry = json.loads((folder / "registry.json").read_text())
policy = json.loads((folder / "policy.json").read_text())

agent = registry["report-agent"]
request = {"resource": "sample-reports", "action": "read"}

if agent["status"] != "active":
    print("DENY: agent is inactive")
elif request not in policy.get(agent["role"], []):
    print("DENY: role does not permit this request")
elif request not in agent["grants"]:
    print("DENY: agent has no matching grant")
else:
    print("ALLOW: role and grant both match")