"""
An event consists of a sequence of actions that result in teh reduction of one drive
"""

from dataclasses import dataclass
from typing import List, Optional, Dict, Any, Tuple, Union, Type

from groundedlang.entity import Entity, Animate
from groundedlang.location import Location
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

    requirements_y: Dict[Action, List[Union[Location, Entity]]]
    requirements_z: Optional[Dict[Action, List[Union[Location]]]] = None




