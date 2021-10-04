from itertools import product
import random
from typing import Generator
import colorlog

from groundedlang.entity import InAnimate, Animate
from groundedlang.event import Action
from groundedlang.location import Location
from groundedlang.workspace import WorkSpace as Ws

from semantics.entities import animates, inanimates

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    fmt='%(log_color)s%(levelname)s:%(name)s:%(message)s',
    log_colors={
        'DEBUG': 'green',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
))

log_world = colorlog.getLogger('world')
log_world.addHandler(handler)
log_world.setLevel('DEBUG')


class World:
    def __init__(self,
                 max_x: int,
                 max_y: int,
                 num_animates: int,  # num instances not types
                 num_inanimates: int,  # num instances not types
                 ):

        self.locations = [Location(x=x, y=y)
                          for x, y in product(range(max_x), range(max_y))]

        self.animates = []
        self.inanimates = []

        entity_kwargs = {'max_x': max_x, 'max_y': max_y}

        # animates
        for ae_def in random.choices(animates.definitions, k=num_animates):
            ae = Animate.from_def(ae_def, entity_kwargs)
            location = random.choice(self.locations)
            location.entities.append(ae)
            ae.location = location
            ae.eat_location = ae.location  # todo but only humans have a non-changing eating location
            self.animates.append(ae)

        # inanimates
        for ie_def in random.choices(inanimates.definitions, k=num_inanimates):
            ie = InAnimate.from_def(ie_def, entity_kwargs)
            location = random.choice(self.locations)
            location.entities.append(ie)
            ie.location = location
            self.inanimates.append(ie)
            log_world.debug(f'{ie}')

        log_world.debug(f'Initialized world with {len(self.locations)} locations')

        Ws.locations = self.locations  # locations must be globally available and never re-initialized

    def turn(self) -> Generator[Action, None, None]:
        """
        Yield 1 set of actions performed by each animate entity.

        We do not create sentences here to clearly separate the world from the corpus.
        """

        for animate_i in self.animates:

            # clear workspace
            Ws.reset()

            # add entity to workspace
            Ws.x = animate_i

            # get event_type to increase drive with highest level (e.g. "eat")
            event_type = animate_i.decide_event_type()
            log_world.debug(f'{animate_i} begins event of type {event_type}.')

            # get event
            if event_type == 'eat':
                # import eat events only once workspace has been updated
                from semantics.events import eat
                # get one eating sequence
                try:
                    events = eat.entity2eat_events[animate_i.name]
                except KeyError:
                    raise KeyError(f'{animate_i} does not have any "eat" event.')
                else:
                    event = random.choices(events, weights=[s.likelihood for s in events])[0]

            else:
                raise NotImplementedError

            # entity performs as many actions as it can in event
            for action in event.actions:

                # check y requirement
                if action.requires_y and Ws.y is None:
                    try:
                        entity_loaders = event.requirements_y[action.name]
                        entity_loader = random.choice(entity_loaders)
                        Ws.y = entity_loader()
                        log_world.debug(f'Loaded {Ws.y}')
                    except KeyError:
                        raise KeyError(f'Action {action} requires Y but none found.')

                # check z requirement
                if action.requires_z and Ws.z is None:
                    try:
                        entity_loaders = event.requirements_z[action.name]
                        entity_loader = random.choice(entity_loaders)
                        Ws.z = entity_loader()
                    except KeyError:
                        raise KeyError(f'Action {action} requires Z but none found.')

                # did action fail due to chance?
                if random.random() > action.failure_probability:
                    log_world.debug(f'{action} failed')
                    continue

                # try to perform primitives
                num_attempts = 0
                while num_attempts < action.num_attempts:

                    # modify world using primitives of the action
                    success = False
                    for primitive in action.primitives:
                        log_world.debug(f'Calling primitives of {action}')
                        success = primitive()
                        log_world.debug('After primitive call:')
                        log_world.debug(Ws.summarize())

                    if success:
                        log_world.debug('Success.')
                        break

                    num_attempts += 1

                else:
                    log_world.warning(f'{event} failed.')
                    break

                yield action
