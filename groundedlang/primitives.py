from typing import Union, Type
import logging

from groundedlang.workspace import WorkSpace as Ws
from groundedlang.location import Location
from groundedlang.entity import Entity, Animate, InAnimate


log_primitives = logging.getLogger('primitives')


class Primitive:
    def __call__(self):
        raise NotImplementedError


class Move(Primitive):
    def __init__(self,
                 entity_: Primitive,
                 location_: Primitive,
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

        log_primitives.debug(f'Calling __gettattr__ with "{item}"')

        class Attr(Primitive):
            log_primitives.debug('Initialized Attr')

            def __call__(self):
                log_primitives.debug('Calling Attr')
                return getattr(Ws.x, item)

        return Attr()


class GetY(Primitive):
    def __call__(self) -> Union[Entity, Location]:
        return Ws.y


class GetZ(Primitive):
    def __call__(self) -> InAnimate:
        return Ws.z
