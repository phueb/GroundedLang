from typing import Union, Type
import colorlog

from groundedlang.workspace import WorkSpace as Ws
from groundedlang.location import Location
from groundedlang.entity import Entity, Animate, InAnimate


handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    fmt='%(log_color)s%(levelname)s:%(name)s:%(message)s',
    log_colors={
        'DEBUG': 'blue',
        'INFO': 'blue',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
))

log_primitives = colorlog.getLogger('primitives')
log_primitives.addHandler(handler)
log_primitives.setLevel('DEBUG')


class Primitive:
    def __call__(self):
        raise NotImplementedError


def resolve(a: Union[Primitive, Entity]):
    if isinstance(a, Primitive):
        return a()
    else:
        return a


class Empty(Primitive):
    def __init__(self):
        pass

    def __call__(self):
        return True


class Move(Primitive):
    def __init__(self,
                 entity_: Primitive,
                 location_: Primitive,
                 ):
        self.location_ = location_
        self.entity_ = entity_

    def __call__(self, *args, **kwargs) -> Location:
        location_target: Location = self.location_()
        entity: Entity = self.entity_()
        log_primitives.debug(f'Moving {entity}\nto {location_target}')
        entity.location = location_target
        return location_target


class InspectLocation(Primitive):
    def __init__(self,
                 location_: Primitive,
                 entity_: Primitive,
                 ):
        self.location_ = location_
        self.entity_ = entity_

    def __call__(self) -> bool:
        entity = self.entity_()
        location = self.location_()
        found = entity in location.entities
        if not found:
            log_primitives.debug(f'Did not find {entity} in {location}'
                                 f'{location.entities}')
        return found


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
    def __call__(self) -> Entity:
        return Ws.y


class GetZ(Primitive):
    def __call__(self) -> InAnimate:
        return Ws.z
