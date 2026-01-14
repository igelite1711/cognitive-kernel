# spine/executor.py

def execute(plan: dict, user_input: str):
    # Execute a plan step based on domain.
    domain = plan.get("domain")

    if domain == "woodworking":
        # Real 3-step woodworking plan
        return [
            "Measure and cut wooden parts",
            "Assemble the chair frame securely",
            "Sand, finish, and test stability"
        ]

    # Default fallback
    return "I can respond, but no executor exists for this domain yet."
