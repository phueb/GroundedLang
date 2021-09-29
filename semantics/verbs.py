"""
This file defines what primitives are triggered by each verb.
"""

from groundedlang.success import Success
from groundedlang.primitives import Move
from groundedlang.primitives import InspectLocation
from groundedlang.event import Action
from groundedlang.workspace import WorkSpace as Ws

verb2action = {
    'look_for': Action(
        name='look_for',
        primitives=[
            (Move, [Ws.x.adjacent_location]),
            (InspectLocation, [Ws.results, Ws.x]),  # inspect location moved to, and check for X
        ],
        success=(Success.is_equal, [Ws.last_result, Ws.y]),
        num_attempts=10,
        requires_x=True,
        requires_y=True,
        requires_z=False,
    ),

    'transport': Action(
        name='transport',
        primitives=[
            (Move, [Ws.x.eat_location]),
        ],
        success=(Success.is_equal, [Ws.last_result, Ws.y]),
        num_attempts=10,
        requires_x=True,
        requires_y=True,
        requires_z=True,
    )

}
