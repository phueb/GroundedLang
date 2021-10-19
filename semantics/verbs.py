"""
This file defines what primitives are triggered by each verb.
"""

from groundedlang.workspace import WorkSpace as Ws
from groundedlang.primitives import GetX, GetY, GetZ
from groundedlang.primitives import Move
from groundedlang.primitives import Empty
from groundedlang.primitives import InspectLocation
from groundedlang.event import Action

verb2action = {
    'look_for': Action(
        name='look_for',
        primitives=[
            InspectLocation(Move(GetX(), GetX().adjacent_coordinate), GetY()),
        ],
        failure_probability=0.9,
        num_attempts=10,
        requires_x=True,
        requires_y=True,
        requires_z=False,
    ),

    'chase': Action(
        name='chase',
        primitives=[
            Empty(),
        ],
        failure_probability=0.9,
        num_attempts=10,
        requires_x=True,
        requires_y=True,
        requires_z=False,
    ),

    'stab': Action(
        name='stab',
        primitives=[
            Empty(),
        ],
        failure_probability=0.9,
        num_attempts=10,
        requires_x=True,
        requires_y=True,
        requires_z=False,
    ),

    'butcher': Action(
        name='butcher',
        primitives=[
            Empty(),
        ],
        failure_probability=0.9,
        num_attempts=10,
        requires_x=True,
        requires_y=True,
        requires_z=False,
    ),

    'cook': Action(
        name='cook',
        primitives=[
            Empty(),
        ],
        failure_probability=0.9,
        num_attempts=10,
        requires_x=True,
        requires_y=True,
        requires_z=False,
    ),

    'transport': Action(
        name='transport',
        primitives=[
            Move(GetX(), GetX().eat_coordinate),
            Move(GetY(), GetX().eat_coordinate),
        ],
        failure_probability=0.9,
        num_attempts=10,
        requires_x=True,
        requires_y=True,
        requires_z=True,
    )

}
