import json
from pathlib import Path
from datetime import datetime, timedelta, timezone

folder = Path(__file__).resolve().parent
request = json.loads((folder / "request.json").read_text())

try:
    approval = json.loads((folder / "approval.json").read_text())
except FileNotFoundError:
    raise SystemExit("DENY: approval file is missing")

if approval.get("request_id") != request["request_id"]:
    raise SystemExit("DENY: approval belongs to a different request")

reviewer = approval.get("reviewed_by")
if not reviewer or reviewer == request["requested_by"]:
    raise SystemExit("DENY: a separate reviewer is required")

if approval.get("decision") != "approved":
    raise SystemExit("DENY: request was not approved")
    
request_details = {key: value for key, value in request.items() if key != "request_id"}

if approval.get("approved_details") != request_details:
    raise SystemExit("DENY: request details differ from the approval")

print("PASS: matching approval from a separate reviewer")

policy_path = folder.parent / "sprint-02-registry-policy" / "policy.json"
policy = json.loads(policy_path.read_text())

scope = {"resource": request["resource"], "action": request["action"]}

if scope not in policy.get(request["role"], []):
    raise SystemExit("DENY: role does not permit this resource and action")

print("PASS: requested resource and action are allowed by the role")
duration = request.get("requested_duration_hours")
if type(duration) is not int or not 1 <= duration <= 24:
    raise SystemExit("DENY: grant duration must be a whole number from 1 to 24 hours")

issued_at = datetime.now(timezone.utc).replace(microsecond=0)
expires_at = issued_at + timedelta(hours=duration)

grant = {
    "agent_id": request["agent_id"],
    "resource": request["resource"],
    "action": request["action"],
    "issued_at": issued_at.isoformat(),
    "expires_at": expires_at.isoformat(),
}

print("PASS: scoped grant generated")
print(json.dumps(grant, indent=2))
def check_access(agent_id, resource, action, at_time):
    if (
        agent_id == grant["agent_id"]
        and resource == grant["resource"]
        and action == grant["action"]
        and issued_at <= at_time < expires_at
    ):
        return "ALLOW"
    return "DENY"


print("Read before expiry:", check_access(
    "summary-agent", "sample-reports", "read", issued_at
))
print("Write before expiry:", check_access(
    "summary-agent", "sample-reports", "write", issued_at
))
print("Read at expiry:", check_access(
    "summary-agent", "sample-reports", "read", expires_at
))
