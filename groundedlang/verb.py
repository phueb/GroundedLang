from dataclasses import dataclass
from typing import List, Tuple, Type

from groundedlang.primitives import Primitive, PrimitiveArg
from groundedlang.success import Success


@dataclass
class Verb:
    name: str
    primitives: List[Tuple[Type[Primitive], List[Type[PrimitiveArg]]]]
    success: Success
