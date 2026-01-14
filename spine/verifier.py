
def verify(result):
    if isinstance(result, str) and "hack" in result.lower():
        return {"status": "STOPPED", "reason": "Unsafe output"}

    return {"status": "SUCCESS", "output": result}
