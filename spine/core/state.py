from dataclasses import dataclass, field
from typing import Any, Dict, List

@dataclass
class SpineState:
    input: str
    plan: Dict[str, Any] = field(default_factory=dict)
    step_results: List[Any] = field(default_factory=list)
    output: Any = None
    status: str = 'INIT'
    errors: List[str] = field(default_factory=list)
