"""
An unordered collection of event sequences that end with an eating activity.
There may be multiple sequences that are legal for a given entity.
Sequences are differentiated by who is eating: This can be a category of entities, or specific members.


Arguments to verbs are X, Y, Z, always in this order.
What types these variables refer to must be documented in lexicon.py

"""

from groundedlang.legality import match_arg_y_name, match_arg_y_category
from groundedlang.event import EventSequence, Action
from groundedlang.workspace import WorkSpace as Ws


entity2eat_sequences = {

    'Mary': (
        EventSequence(
            legality_condition=match_arg_y_category('HERBIVORE'),
            likelihood=1,
            actions=[
                Action('look_for', Ws.X, Ws.Y),
                Action('chase', Ws.X, Ws.Y),
                Action('stab', Ws.X, Ws.Y),
                Action('transport', Ws.X, Ws.Y, Ws.X.eat_location),
                Action('butcher', Ws.X, Ws.Y),
                Action('cook', Ws.X, Ws.Y),
                Action('eat', Ws.X, Ws.Y),
            ],
        ),
        EventSequence(
            legality_condition=match_arg_y_name('squirrel'),
            likelihood=1,
            actions=[
                Action('look_for', Ws.X, Ws.Y),
                Action('chase', Ws.X, Ws.Y),
                Action('stab', Ws.X, Ws.Y),
                Action('eat', Ws.X, Ws.Y),
            ],
        ),
    ),




}
