
def route(user_input: str) -> dict:
    text = user_input.lower()

    if "hack" in text or "exploit" in text:
        return {"status": "STOPPED", "reason": "Unsafe intent"}

    if "chair" in text or "wood" in text:
        return {"domain": "woodworking"}

    return {"domain": "general"}
