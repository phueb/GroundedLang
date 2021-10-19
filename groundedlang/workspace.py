import queue
from typing import Optional, List

from groundedlang.entity import Entity, Animate, InAnimate
from groundedlang.coordinate import Location


class WorkSpace:

    # store results of primitives
    results = queue.LifoQueue()

    # theta-grid.
    # x is always first in sentence, y is always second, and z is always third.
    x: Optional[Animate] = None
    y: Optional[Entity] = None
    z: Optional[InAnimate] = None

    coordinates: List[Location]

    @property
    def last_result(self):
        return self.results.get()

    @classmethod
    def summarize(cls):
        res = 'Workspace:\n'
        res += f'   x={cls.x}\n'
        res += f'   y={cls.y}\n'
        res += f'   z={cls.z}'
        return res

    @classmethod
    def reset(cls):
        cls.x = None
        cls.y = None
        cls.z = None

