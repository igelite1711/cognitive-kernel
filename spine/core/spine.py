
from spine.core.state import SpineState
from spine.core.planner import planner
from spine.core.executor import executor
from spine.core.verifier import verifier
from spine.tools.registry import TOOLS

def run_spine(user_input, attempt=1):
    state = SpineState(input=user_input)
    state = planner(state)
    state = executor(state, TOOLS)
    state = verifier(state)
    if state.status == "RETRY" and attempt < 2:
        return run_spine(f"Solve step-by-step: {user_input}", attempt=attempt+1)
    return state
