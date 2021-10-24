"""
Event sequences are an ordered list of actions that end with an eating action.
There may be multiple sequences that are legal for a given entity.
Sequences are differentiated by who is eating: This can be a category of entities, or specific members.


Arguments to verbs are X, Y, Z, always in this order.
What types these variables refer to must be documented in lexicon.py

"""

from groundedlang.load import LoadEntity
from groundedlang.event import Event
from groundedlang.entity import Animate, InAnimate

from semantics.verbs import verb2action


human_eat_bovine = Event(
    requirements_y={
        'look_for': [
            LoadEntity(cls=Animate, name='fox'),
        ],
    },
    requirements_l={
        'transport': [
            LoadEntity(cls=InAnimate, name='tent'),
        ],
    },
    likelihood=1,
    actions=[
        verb2action['look_for'],
        verb2action['chase'],
        verb2action['throw_at'],
        verb2action['butcher'],
        verb2action['gather'],
        verb2action['transport'],
        verb2action['heat'],
        verb2action['eat'],
    ],
)


entity2eat_events = {

    # HUMANS

    'Mary': (
        human_eat_bovine,
    ),

    # CARNIVORES

    'fox': (
        Event(
            requirements_y={
                'look_for': [
                    LoadEntity(cls=InAnimate, name='strawberry'),
                    LoadEntity(cls=InAnimate, name='acorn'),
                ],
            },
            likelihood=1,
            actions=[
                verb2action['look_for'],
                # verb2action['eat'],
            ],
        ),
    ),

    # HERBIVORES

    'squirrel': (
        Event(
            requirements_y={
                'look_for': [
                    LoadEntity(cls=InAnimate, name='strawberry'),
                    LoadEntity(cls=InAnimate, name='acorn'),
                ],
            },
            likelihood=1,
            actions=[
                verb2action['look_for'],
                # verb2action['eat'],
            ],
        ),
    ),


}
