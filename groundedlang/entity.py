import random
from typing import Optional, Type, Dict
import queue
from dataclasses import dataclass

from groundedlang.drives import Hunger
from groundedlang.location import Location


class Entity:
    def __init__(self,
                 name: str,
                 category: str,
                 **kwargs
                 ):
        self.name = name
        self.category = category
        self.definite = False  # todo how does an entity become definite?

        # location info
        self.max_x: Optional[int] = kwargs.get('max_x', None)
        self.max_y: Optional[int] = kwargs.get('max_y', None)
        self.location: Optional[Location] = None  # assigned upon initialization of World
        self.locations_visited = queue.LifoQueue()  # todo use

    def __str__(self):
        res = ''
        res += f'Entity\n'
        res += f'   name "{self.name}"\n'
        res += f'   location={self.location}\n'
        return res

    def __repr__(self):
        """this string will show when entity is printed as part of a collection (e.g. inside a list)"""
        return self.name

    @property
    def adjacent_location(self):
        """find adjacent location tha tis not outside bounds of the world"""

        from groundedlang.workspace import WorkSpace as Ws

        while True:
            x = self.location.x + random.choice([-1, 0, 1])
            y = self.location.y + random.choice([-1, 0, 1])
            for location in Ws.locations:
                if location.x == x and location.y == y:
                    return location

    @classmethod
    def from_def(cls,
                 d,  # of type EntityDef
                 entity_kwargs: Optional[Dict] = None,
                 ):
        if entity_kwargs:
            return d.cls(**d.__dict__, **entity_kwargs)
        else:
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
        super().__init__(name, category, **kwargs)

        kwargs.pop('cls')


class Animate(Entity):
    def __init__(self,
                 name: str,
                 category: str,
                 **kwargs,
                 ):
        super().__init__(name, category, **kwargs)

        kwargs.pop('cls')

        self.hunger = Hunger()
        self.eat_location = None

    def decide_event_type(self):

        # todo

        return self.hunger.event_type
