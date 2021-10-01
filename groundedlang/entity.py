import random
from typing import Optional, Type
import queue
from dataclasses import dataclass

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
        res += f'Entity\n'
        res += f'   name "{self.name}"\n'
        res += f'   location={self.location}'
        return res

    @property
    def adjacent_location(self):
        raise NotImplementedError
        return Location(x=self.location.x + random.choice([-1, 0, 1]),  # todo must not be larger than max x and max y
                        y=self.location.y + random.choice([-1, 0, 1]))

    @property
    def next_location(self):  # todo
        return Location

    @classmethod
    def from_def(cls, d):
        return d.cls(**d.__dict__)


@dataclass
class EntityDefinition:
    name: str
    category: str
    cls: Type[Entity]

    # todo what about custom attributes?


class InAnimate(Entity):
    def __init__(self,
                 name: str,
                 category: str,
                 **kwargs
                 ):
        super().__init__(name, category)

        kwargs.pop('cls')


class Animate(Entity):
    def __init__(self,
                 name: str,
                 category: str,
                 **kwargs,
                 ):
        super().__init__(name, category)

        kwargs.pop('cls')

        self.hunger = Hunger()
        self.eat_location = None

    def decide_event_type(self):

        # todo

        return self.hunger.event_type
