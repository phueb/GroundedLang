import queue
from typing import Union

from groundedlang.entity import Entity, Agent, Instrument
from groundedlang.location import Location


class WorkSpace:

    results = queue.LifoQueue()

    # theta-grid with thematic roles
    # note: X, Y, Y always occur in this order in a sentence
    X: Agent
    Y: Union[Entity, Location]
    Z: Instrument
