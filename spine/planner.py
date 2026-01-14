
# spine/planner.py
# Minimal planner for Phase 5 — produces step-by-step plan based on domain

def plan(user_input: str, domain: str) -> dict:
    '''
    Generate a plan object for the given user input and domain.
    Returns:
        dict with keys:
            - goal: original input
            - domain: domain type
            - steps: list of steps with id, action, input
    '''
    steps = []

    if domain == "woodworking":
        steps.append({"id": 1, "action": "execute", "input": user_input})
    else:
        steps.append({"id": 1, "action": "execute", "input": user_input})

    return {
        "goal": user_input,
        "domain": domain,
        "steps": steps
    }
