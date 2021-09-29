"""
Event sequences are an ordered list of actions that end with an eating action.
There may be multiple sequences that are legal for a given entity.
Sequences are differentiated by who is eating: This can be a category of entities, or specific members.


Arguments to verbs are X, Y, Z, always in this order.
What types these variables refer to must be documented in lexicon.py

"""

from groundedlang.event import Event
from groundedlang.entity import Animate, InAnimate

from semantics.verbs import verb2action


entity2eat_sequences = {

    'Mary': (
        Event(
            ys=[Animate.from_name('squirrel'),
                Animate.from_name('fox')],
            likelihood=1,
            actions=[
                verb2action['look_for'],
                # verb2action['chase'],
                # verb2action['stab'],
                # verb2action['transport'],
                # verb2action['butcher'],
                # verb2action['cook'],
                # verb2action['eat'],
            ],
        ),
        Event(
            ys=[Animate.from_name('squirrel'),
                Animate.from_name('fox')],
            likelihood=1,
            actions=[
                verb2action['look_for'],
                # verb2action['chase'],
                # verb2action['stab'],
                # verb2action['eat'],
            ],
        ),
    ),




}
