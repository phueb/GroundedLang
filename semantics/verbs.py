"""
This file defines what primitives are triggered by each verb.
"""

from groundedlang.workspace import WorkSpace as Ws
from groundedlang.success import Success
from groundedlang.primitives import GetX, GetY, GetZ
from groundedlang.primitives import Move
from groundedlang.primitives import InspectLocation
from groundedlang.event import Action

verb2action = {
    'look_for': Action(
        name='look_for',
        primitives=InspectLocation(Move(GetX(), GetX().adjacent_location), GetY()),
        success=(Success.is_equal, [Ws.last_result, GetY]),
        num_attempts=10,
        requires_x=True,
        requires_y=True,
        requires_z=False,
    ),

    'transport': Action(
        name='transport',
        primitives=Move(GetX(), GetX().eat_location),
        success=(Success.is_equal, [Ws.last_result, GetY]),
        num_attempts=10,
        requires_x=True,
        requires_y=True,
        requires_z=True,
    )

}