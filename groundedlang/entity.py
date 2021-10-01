import random
from typing import Optional
import queue

from groundedlang.drives import Hunger
from groundedlang.location import Location


class Entity:
    def __init__(self,
                 name: str,
                 category: str,
                 ):
        self.name = name
        self.category = category
        self.definite = False  # todo how does an entity become definite?

        self.location: Optional[Location] = None  # assigned upon initialization of World

        self.locations_visited = queue.LifoQueue()  # todo use

    def __str__(self):
        res = ''
        res += f'Entity with name "{self.name}":\n'
        res += f'location={self.location}'
        return res

    @property
    def adjacent_location(self):
        return Location(x=self.location.x + random.choice([0, 1]),
                        y=self.location.y + random.choice([0, 1]))

    @classmethod
    def from_name(cls, name: str):

        return cls(name=name, category='test')  # todo look up entity info like category in some database


class InAnimate(Entity):
    pass


class Animate(Entity):
    def __init__(self,
                 name: str,
                 category: str,
                 ):
        super().__init__(name, category)

        self.hunger = Hunger()
        self.eat_location = None

    def decide_event_type(self):

        # todo

        return self.hunger.event_type
