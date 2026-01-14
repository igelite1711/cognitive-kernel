# spine/spine.py - Main run function

from spine.executor import execute
from memory.vector import MEMORY

# Mock functions for now
def route(user_input: str):
    if "wooden chair" in user_input.lower() or "woodworking" in user_input.lower():
        return "woodworking"
    return "general"

def plan(user_input: str, domain: str):
    if domain == "woodworking":
        return {"domain": "woodworking", "steps": [{"action": "execute", "input": user_input}]}
    return {"domain": "general", "steps": [{"action": "execute", "input": user_input}]}

def verify(output):
    if output == "I can respond, but no executor exists for this domain yet.":
        return {"status": "FAILED", "reason": "No executor for this domain"}
    return {"status": "SUCCESS"}

def run(user_input: str):
    domain = route(user_input)
    plan_obj = plan(user_input, domain)
    final_output = None

    for step in plan_obj.get("steps", []):
        if step["action"] == "execute":
            final_output = execute(plan_obj, step["input"])

    verdict = verify(final_output)
    if verdict.get("status") != "SUCCESS":
        return final_output # Return the output even if verification failed

    MEMORY.store(user_input, final_output)
    return final_output
