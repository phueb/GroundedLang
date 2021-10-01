"""
An event consists of a sequence of actions that result in teh reduction of one drive
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple, Union, Type

from groundedlang.load import LoadEntity
from groundedlang.entity import Entity, Animate
from groundedlang.primitives import Primitive


@dataclass
class Action:
    name: str
    primitives: List[Primitive]
    failure_probability: float
    num_attempts: int
    requires_x: bool = False
    requires_y: bool = False
    requires_z: bool = False

    def __str__(self):
        return f'"{self.name}"'


@dataclass
class Event:
    actions: List[Action]
    likelihood: int  # between 1 and 10

    requirements_y: Dict[str, List[LoadEntity]]
    requirements_z: Dict[str, List[LoadEntity]] = field(default_factory=dict)

    def __str__(self):
        return str(self.actions[-1])
