
from spine.core.kernel_connector import get_kernel
def planner(state):
    kernel = get_kernel()
    intent = kernel.call_primitive("intent", state.input).upper()
    if "COMPLEX" in intent:
        raw_steps = kernel.call_primitive("decomposition", state.input)
        steps = [s.strip() for s in raw_steps.split("\n") if len(s.strip()) > 5]
        state.plan = {"goal": state.input, "steps": [{"id": i+1, "action": "respond", "input": s} for i, s in enumerate(steps)]}
    else:
        state.plan = {"goal": state.input, "steps": [{"id": 1, "action": "respond", "input": state.input}]}
    return state
