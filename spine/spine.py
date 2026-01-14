
"""
Spine — Central Intelligence Loop
Phase 2–4: Planning, Execution, Verification, Memory
"""

from spine.router import route
from spine.planner import plan
from spine.executor import execute
from spine.verifier import verify
from spine.memory import MEMORY


def run(user_input: str):
    """
    Main execution entry point.
    Integrates memory for recall and storage.
    """

    # ---- MEMORY RECALL ----
    recalled = MEMORY.recall(user_input)
    if recalled is not None:
        return {
            "status": "CACHED",
            "output": recalled
        }

    # ---- ROUTING ----
    route_result = route(user_input)
    if route_result["status"] != "OK":
        return route_result

    # ---- PLANNING ----
    plan_obj = plan(user_input)

    # ---- EXECUTION ----
    result = execute(plan_obj)

    # ---- VERIFICATION ----
    verdict = verify(user_input, result)
    if verdict["status"] != "SUCCESS":
        return verdict

    # ---- MEMORY STORE ----
    MEMORY.store(user_input, result)

    return {
        "status": "SUCCESS",
        "output": result
    }
