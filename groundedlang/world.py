from itertools import product
import random
from typing import List, Generator

from groundedlang.event import Action
from groundedlang.location import Location
from groundedlang.workspace import WorkSpace as Ws

from semantics import animates


class World:
    def __init__(self,
                 max_x: int,
                 max_y: int,
                 num_animates: int = 2
                 ):

        self.locations = [Location(x=x, y=y)
                          for x, y in product(range(max_x), range(max_y))]

        # include a sample of entities
        self.animates = random.sample(animates.population, k=num_animates)

        # assign locations
        for animate_i in self.animates:
            animate_i.location = random.choice(self.locations)
            animate_i.eat_location = animate_i.location

    def turn(self) -> Generator[Action, None, None]:
        """
        Yield 1 set of actions performed by each animate entity.

        We do not create sentences here to clearly separate the world from the corpus.
        """

        for animate_i in self.animates:

            # add entity to workspace
            Ws.x = animate_i
            # get event_type to increase drive with highest level (e.g. "eat")
            event_type = animate_i.decide_event_type()

            # get event
            if event_type == 'eat':
                # import eat sequences only once workspace has been updated
                from semantics import eat
                # get one eating sequence
                try:
                    sequences = eat.entity2eat_sequences[animate_i.name]
                except KeyError:
                    raise KeyError(f'{animate_i} does not have any "eat" event.')
                else:
                    sequence = random.choices(sequences, weights=[s.likelihood for s in sequences])[0]
                # save y to workspace
                Ws.y = random.choice(sequence.y_targets)

            else:
                raise NotImplementedError

            # entity performs as many actions as it can in event sequence
            for action in sequence.actions:
                yield action
