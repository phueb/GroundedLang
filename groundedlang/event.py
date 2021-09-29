from dataclasses import dataclass
from typing import List, Optional, Callable, Any

from groundedlang.workspace import WorkSpace


@dataclass
class Action:
    name: str
    arg_x: Optional[WorkSpace.X] = None
    arg_y: Optional[WorkSpace.Y] = None
    arg_z: Optional[WorkSpace.Z] = None


@dataclass
class EventSequence:
    legality_condition: Callable[[Any], bool]
    actions: List[Action]
    likelihood: int  # between 1 and 10




