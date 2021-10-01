from typing import Union, Type
import logging

from groundedlang.workspace import WorkSpace as Ws
from groundedlang.location import Location
from groundedlang.entity import Entity, Animate, InAnimate


log_primitives = logging.getLogger('primitives')


class Primitive:
    pass


class Move(Primitive):
    def __init__(self,
                 entity_: Type[Primitive],
                 location_: Type[Primitive],
                 ):
        self.location_ = location_
        self.entity_ = entity_

    def __call__(self, *args, **kwargs) -> Location:
        target_location = self.location_.__call__()
        self.entity_.__call__().location = target_location
        return target_location


class InspectLocation(Primitive):
    def __init__(self,
                 location_: Type[Primitive],
                 entity_: Type[Primitive],
                 ):
        self.location_ = location_
        self.entity_ = entity_

    def __call__(self) -> bool:
        return self.entity_.__call__() in self.location_.__call__().entities


class GetX(Primitive):
    def __init__(self):
        log_primitives.debug('Initialized GetX')

    def __call__(self) -> Animate:
        return Ws.x

    def __getattr__(self, item):
        """we need to return a function that returns the attribute, instead of getting the attribute right away"""

        def callback():
            return getattr(Ws.x, item)

        return callback


class GetY(Primitive):
    def __call__(self) -> Union[Entity, Location]:
        return Ws.y


class GetZ(Primitive):
    def __call__(self) -> InAnimate:
        return Ws.z
