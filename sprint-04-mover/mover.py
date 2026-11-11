import json
from pathlib import Path

folder = Path(__file__).resolve().parent
agent = json.loads((folder / "agent-before.json").read_text())


def check_access(agent, resource, action):
    requested_grant = {"resource": resource, "action": action}
    if agent["status"] == "active" and requested_grant in agent["grants"]:
        return "ALLOW"
    return "DENY"


print("Before move")
print("Read sample-reports:", check_access(agent, "sample-reports", "read"))
print("Read sample-catalog:", check_access(agent, "sample-catalog", "read"))

move = json.loads((folder / "move-request.json").read_text())

processed_events = set()


def apply_move(agent, move):
    event_id = move["event_id"]

    if move["agent_id"] != agent["agent_id"]:
        return "DENY: move targets a different agent"

    if event_id in processed_events:
        return "SKIP: move was already applied"

    if move["expected_authorization_version"] != agent["authorization_version"]:
        return "DENY: move targets an outdated agent version"

    agent["grants"] = []
    print("\nAfter revoking old grants")
    print("Read sample-reports:", check_access(agent, "sample-reports", "read"))

    agent["role"] = move["new_role"]
    agent["grants"] = move["replacement_grants"]
    agent["authorization_version"] += 1
    processed_events.add(event_id)
    return "PASS: move applied"


result = apply_move(agent, move)
print(result)
if result != "PASS: move applied":
    raise SystemExit(1)

print("\nAfter move")
print("Role:", agent["role"])
print("Authorization version:", agent["authorization_version"])
print("Read sample-reports:", check_access(agent, "sample-reports", "read"))
print("Read sample-catalog:", check_access(agent, "sample-catalog", "read"))

print("\nRetry same event")
print(apply_move(agent, move))
print("Authorization version:", agent["authorization_version"])
print("Read sample-reports:", check_access(agent, "sample-reports", "read"))
print("Read sample-catalog:", check_access(agent, "sample-catalog", "read"))
