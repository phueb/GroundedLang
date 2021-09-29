from itertools import product
import random
from typing import List

from groundedlang.entity import Animate, InAnimate, Entity
from groundedlang.location import Location
from groundedlang.workspace import WorkSpace as Ws

from semantics import animates


class World:
    def __init__(self,
                 max_x: int,
                 max_y: int,
                 num_animates: int = 1
                 ):

        self.locations = [Location(x=x, y=y)
                          for x, y in product(range(max_x), range(max_y))]

        # todo animate instances should be created in semantics.animates, and a subsample should be collected here
        self.animates = random.choices(animates.population, k=num_animates)

        # assign locations
        for animate_i in self.animates:
            animate_i.location = random.choice(self.locations)
            animate_i.eat_location = animate_i.location

    def turn(self) -> List[str]:

        sentences = []

        for animate_i in self.animates:

            # add entity to workspace
            Ws.x = animate_i
            # get event_type to increase drive with highest level (e.g. "eat")
            event_type = animate_i.decide_event_type()

            if event_type == 'eat':
                # import eat sequences only once workspace has been updated
                from semantics import eat
                # get one eating sequence
                sequences = eat.entity2eat_sequences[animate_i.name]
                sequence = random.choices(sequences, weights=[s.likelihood for s in sequences])[0]
                # save y to workspace
                Ws.y = random.choice(sequence.ys)

            else:
                raise NotImplementedError

            # entity performs as many actions as it can in event sequence
            for action in sequence.actions:
                # transitive
                if action.requires_x and action.requires_y and not action.requires_z:
                    sentence = f'{Ws.x.name} {action.name} {Ws.y.name}'
                # ditransitive
                elif action.requires_x and action.requires_y and action.requires_z:
                    sentence = f'{Ws.x.name} {action.name} {Ws.y.name} {Ws.z.name}'
                else:
                    raise RuntimeError

                print(sentence)
                sentences.append(sentence)

            return sentences
