import random
from typing import Optional

from groundedlang.drives import Hunger
from groundedlang.location import Location


class Entity:
    def __init__(self,
                 name: str,
                 category: str,
                 ):
        self.name = name
        self.category = category

        self.location: Optional[Location] = None  # assigned upon initialization of World

    @property
    def adjacent_location(self):
        return Location(x=self.location.x + random.choice([0, 1]),
                        y=self.location.y + random.choice([0, 1]))


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
