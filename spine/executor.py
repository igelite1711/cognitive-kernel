
def execute(plan: dict, user_input: str):
    domain = plan.get("domain")

    if domain == "woodworking":
        return [
            "Measure and cut wooden parts",
            "Assemble the chair frame securely",
            "Sand, finish, and test stability"
        ]

    return "I can respond, but no executor exists for this domain yet."
