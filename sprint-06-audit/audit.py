import hashlib
import json
from pathlib import Path

folder = Path(__file__).resolve().parent

events = {}
event_path = folder / "lifecycle-event.json"
if event_path.is_file():
    event = json.loads(event_path.read_text())
    events[event["event_id"]] = event

decision = json.loads((folder / "access-decision.json").read_text())
event_id = decision["related_event_id"]
event = events.get(event_id)

if event is None:
    raise SystemExit(f"REVIEW: lifecycle event {event_id} is missing")

if event["agent_id"] != decision["agent_id"]:
    raise SystemExit("REVIEW: lifecycle event and decision name different agents")
policy_path = folder.parent / "sprint-05-leaver" / "leaver.py"
current_hash = hashlib.sha256(policy_path.read_bytes()).hexdigest()

if decision.get("policy_sha256") != current_hash:
    raise SystemExit("REVIEW: policy fingerprint does not match")

print("VERIFIED: policy fingerprint matches")

print(f"LINKED: {decision['decision_id']} → {event_id}")
print(f"Lifecycle: {event['actor_id']} disabled {event['agent_id']}")
print(f"Access: {decision['decision']} — {decision['reason']}")
