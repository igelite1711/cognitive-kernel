
def run(user_input: str):
    """
    Phase 3: Domain-aware execution spine
    """
    from spine.router import route
    from spine.executor import execute
    from spine.verifier import verify

    plan = route(user_input)

    if plan.get("status") == "STOPPED":
        return plan

    result = execute(plan, user_input)
    return verify(result)
