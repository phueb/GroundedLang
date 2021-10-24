import queue
from typing import Optional, List

from groundedlang.entity import Entity, Animate, InAnimate
from groundedlang.coordinate import Coordinate


class WorkSpace:
    """
    makes available variables globally (to all parts of the program)
    """

    # store results of primitives
    results = queue.LifoQueue()

    # store verb arguments
    x: Optional[Animate] = None
    y: Optional[Entity] = None
    i: Optional[InAnimate] = None
    l: Optional[InAnimate] = None

    coordinates: List[Coordinate]

    @property
    def last_result(self):
        return self.results.get()

    @classmethod
    def summarize(cls):
        res = 'Workspace:\n'
        res += f'   x={cls.x}\n'
        res += f'   y={cls.y}\n'
        res += f'   i={cls.i}\n'
        res += f'   l={cls.l}'
        return res

    @classmethod
    def reset(cls):
        cls.x = None
        cls.y = None
        cls.i = None
        cls.l = None
