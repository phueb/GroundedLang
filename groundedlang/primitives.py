from typing import Union, Type

from groundedlang.workspace import WorkSpace as Ws
from groundedlang.location import Location
from groundedlang.entity import Entity, Animate, InAnimate


class Primitive:
    pass


class Move(Primitive):
    def __init__(self,
                 entity: Primitive,
                 location: Primitive,
                 ):
        self.location = location
        self.entity = entity

    def __call__(self, *args, **kwargs):
        self.entity.location = self.location
        return self.location


class InspectLocation(Primitive):
    def __init__(self,
                 location: Primitive,
                 entity: Primitive,
                 ):
        self.location = location
        self.entity = entity

    def __call__(self, *args, **kwargs) -> bool:
        return self.entity in self.location.entities


class GetX(Primitive):
    def __call__(self) -> Animate:
        return Ws.x

    def __getattr__(self, item):
        return getattr(Ws.x, item)


class GetY(Primitive):
    def __call__(self) -> Union[Entity, Location]:
        return Ws.y


class GetZ(Primitive):
    def __call__(self) -> InAnimate:
        return Ws.z