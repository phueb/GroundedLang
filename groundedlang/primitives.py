import colorlog

from groundedlang.workspace import WorkSpace as Ws
from groundedlang.coordinate import Coordinate
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


class Empty(Primitive):
    def __init__(self):
        pass

    def __call__(self):
        return True


class Move(Primitive):
    def __init__(self,
                 entity_: Primitive,
                 coordinate_: Primitive,
                 ):
        self.coordinate_ = coordinate_
        self.entity_ = entity_

    def __call__(self, *args, **kwargs) -> Coordinate:
        coordinate_target: Coordinate = self.coordinate_()
        entity: Entity = self.entity_()
        log_primitives.debug(f'Moving {entity} to {coordinate_target}')
        entity.coordinate = coordinate_target
        return coordinate_target


class InspectCoordinate(Primitive):
    def __init__(self,
                 coordinate_: Primitive,
                 entity_: Primitive,
                 ):
        self.coordinate_ = coordinate_
        self.entity_ = entity_

    def __call__(self) -> bool:
        entity = self.entity_()
        coordinate = self.coordinate_()
        found = entity.name in [e.name for e in coordinate.entities]  # match name not object
        if not found:
            log_primitives.debug(f'Did not find {entity} in {coordinate} with entities {coordinate.entities}')
        return found


class GetX(Primitive):
    def __init__(self):
        log_primitives.debug('Initialized GetX')

    def __call__(self) -> Animate:
        return Ws.x

    def __getattr__(self, item):
        """we need to return a function that returns the attribute, instead of getting the attribute right away"""

        log_primitives.debug(f'Initialized __gettattr__ with "{item}"')

        class Attr(Primitive):
            log_primitives.debug('Initialized Attr')

            def __call__(self):
                log_primitives.debug('Calling Attr')
                return getattr(Ws.x, item)

        return Attr()


class GetY(Primitive):
    def __call__(self) -> Entity:
        return Ws.y


class GetI(Primitive):
    def __call__(self) -> InAnimate:
        return Ws.i


class GetL(Primitive):
    def __call__(self) -> InAnimate:
        return Ws.l