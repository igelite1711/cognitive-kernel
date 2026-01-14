
"""
Phase 3 — Woodworking Domain Executor

This module provides safe, domain-grounded execution
for woodworking-related planning tasks.
"""

from typing import List, Dict


WOODWORKING_KEYWORDS = {
    "chair",
    "table",
    "wood",
    "wooden",
    "furniture",
    "saw",
    "cut",
    "assemble",
    "sand",
    "finish",
    "measure",
    "nail",
    "screw",
}


def is_woodworking_task(text: str) -> bool:
    """
    Detect whether the input belongs to the woodworking domain.
    """
    text = text.lower()
    return any(word in text for word in WOODWORKING_KEYWORDS)


def generate_plan(task: str) -> Dict:
    """
    Generate a deterministic, safe woodworking plan.
    """
    task_lower = task.lower()

    if "chair" in task_lower:
        steps = [
            "Measure and cut wooden parts according to chair dimensions",
            "Assemble the chair frame securely using screws or joints",
            "Sand the surfaces, apply finish, and test stability",
        ]

    elif "table" in task_lower:
        steps = [
            "Measure and cut tabletop and leg components",
            "Assemble the table frame and attach legs evenly",
            "Sand, finish, and ensure the table is level",
        ]

    else:
        steps = [
            "Measure and prepare wooden components",
            "Assemble parts carefully using appropriate tools",
            "Sand, finish, and inspect the final product",
        ]

    return {
        "status": "SUCCESS",
        "domain": "woodworking",
        "steps": steps,
    }


def execute(task: str) -> Dict:
    """
    Entry point for woodworking execution.
    """
    if not is_woodworking_task(task):
        return {
            "status": "FAILED",
            "reason": "Not a woodworking task",
        }

    return generate_plan(task)
