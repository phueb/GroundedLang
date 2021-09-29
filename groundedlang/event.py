from dataclasses import dataclass
from typing import List, Optional, Callable, Any, Tuple, Union, Type

from groundedlang.entity import Entity, Animate
from groundedlang.location import Location
from groundedlang.primitives import Primitive
from groundedlang.success import Success


@dataclass
class Action:
    name: str
    primitives: List[
        Tuple[Type[Primitive],
              List[Union[Entity, Location]]
        ]
    ]
    success: Tuple[Success.is_equal,
                   List[Union[Entity, Location]]
    ]
    num_attempts: int
    requires_x: bool = False
    requires_y: bool = False
    requires_z: bool = False


@dataclass
class EventSequence:
    legal_y_names: List[str]
    actions: List[Action]
    likelihood: int  # between 1 and 10




