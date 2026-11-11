import json
from pathlib import Path

folder = Path(__file__).resolve().parent
agent = json.loads((folder / "agent-before.json").read_text())

session = {
    "agent_id": agent["agent_id"],
    "authorization_version": agent["authorization_version"],
}


def check_access(agent, session, resource, action):
    if session["agent_id"] != agent["agent_id"]:
        return "DENY: session belongs to a different agent"

    if agent["status"] != "active":
        return "DENY: agent is disabled"

    if session["authorization_version"] != agent["authorization_version"]:
        return "DENY: session version is outdated"

    if {"resource": resource, "action": action} not in agent["grants"]:
        return "DENY: agent has no matching grant"

    return "ALLOW"


print("Before offboarding")
print("Session version:", session["authorization_version"])
print("Read sample-catalog:", check_access(agent, session, "sample-catalog", "read"))
agent["status"] = "disabled"
agent["grants"] = []
agent["authorization_version"] += 1

print("\nAfter offboarding")
print("Agent status:", agent["status"])
print("Remaining grants:", len(agent["grants"]))
print("Agent version:", agent["authorization_version"])
print("Original session version:", session["authorization_version"])
print("Read sample-catalog:", check_access(agent, session, "sample-catalog", "read"))
test_agent = {
    **agent,
    "status": "active",
    "grants": [{"resource": "sample-catalog", "action": "read"}],
}

print("\nOld session against an active test copy")
print("Agent version:", test_agent["authorization_version"])
print("Session version:", session["authorization_version"])
print("Read sample-catalog:", check_access(test_agent, session, "sample-catalog", "read"))
