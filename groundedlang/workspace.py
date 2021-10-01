import queue
from typing import Union, Optional

from groundedlang.entity import Entity, Animate, InAnimate
from groundedlang.location import Location


class WorkSpace:

    # store results of primitives
    results = queue.LifoQueue()

    # theta-grid.
    # x is always first in sentence, y is always second, and z is always third.
    x: Optional[Animate] = None
    y: Optional[Union[Entity, Location]] = None
    z: Optional[InAnimate] = None

    @property
    def last_result(self):
        return self.results.get()

    @classmethod
    def summarize(cls):
        res = 'workspace:\n'
        res += f'x={cls.x}\n'
        res += f'y={cls.y}\n'
        res += f'z={cls.z}'
        return res
