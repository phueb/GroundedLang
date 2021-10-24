"""
This file defines what primitives are triggered by each verb.
"""

from groundedlang.primitives import GetX, GetY, GetI, GetL
from groundedlang.primitives import Move
from groundedlang.primitives import Empty
from groundedlang.primitives import InspectCoordinate
from groundedlang.primitives import ReduceDrive
from groundedlang.event import Action
from groundedlang import configs

T = True
F = False

verb2action = {

    'rest': Action(
        name='rest',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=F,
        requires_i=F,
        requires_l=T,
    ),

    'go_to': Action(
        name='go_to',
        primitives=[
            Move(GetX(), GetL()),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=F,
        requires_i=F,
        requires_l=T,
    ),

    'chop': Action(
        name='chop',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=T,
        requires_l=T,
    ),

    'gather': Action(
        name='gather',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=F,
        requires_l=F,
    ),

    'crack': Action(
        name='crack',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=T,
        requires_l=T,
    ),

    'cut': Action(
        name='cut',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=T,
        requires_l=T,
    ),

    'weave': Action(
        name='weave',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=F,
        requires_l=F,
    ),

    'heat': Action(
        name='heat',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=T,
        requires_l=F,
    ),

    'carve': Action(
        name='carve',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=T,
        requires_l=F,
    ),

    'polish': Action(
        name='polish',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=T,
        requires_l=F,
    ),

    'peel': Action(
        name='peel',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=T,
        requires_l=F,
    ),

    'tie': Action(
        name='tie',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=T,
        requires_l=F,
    ),

    'look_for': Action(
        name='look_for',
        primitives=[
            InspectCoordinate(Move(GetX(), GetX().adjacent_coordinate), GetY()),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=False,
        requires_l=False,
    ),

    'chase': Action(
        name='chase',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=F,
        requires_l=F,
    ),

    'throw_at': Action(
        name='throw_at',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=T,
        requires_l=F,
    ),

    'butcher': Action(
        name='butcher',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=T,
        requires_l=F,
    ),

    'transport': Action(
        name='transport',
        primitives=[
            Move(GetX(), GetX().eat_coordinate),
            Move(GetY(), GetX().eat_coordinate),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=F,
        requires_l=T,
    ),

    'eat': Action(
        name='eat',
        primitives=[
            ReduceDrive(configs.Drives.hunger)
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=F,
        requires_l=F,
    ),

    'shoot': Action(
        name='shoot',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=T,
        requires_l=F,
    ),

    'set_trap': Action(
        name='set_trap',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=F,
        requires_i=F,
        requires_l=T,
    ),

    'wait': Action(
        name='wait',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=F,
        requires_i=F,
        requires_l=F,
    ),

    'stab': Action(
        name='stab',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=T,
        requires_l=F,
    ),

    'bite': Action(
        name='bite',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=F,
        requires_l=F,
    ),

    'boil': Action(
        name='boil',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=F,
        requires_l=F,
    ),

    'pour': Action(
        name='pour',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=F,
        requires_l=F,
    ),

    'drink': Action(
        name='boil',
        primitives=[
            ReduceDrive(configs.Drives.hunger),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=T,
        requires_i=F,
        requires_l=F,
    ),

    'lay_down': Action(
        name='lay_down',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=F,
        requires_i=F,
        requires_l=T,
    ),


    'sleep': Action(
        name='sleep',
        primitives=[
            ReduceDrive(configs.Drives.fatigue),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=F,
        requires_i=F,
        requires_l=T,
    ),

    'wake_up': Action(
        name='wake_up',
        primitives=[
            Empty(),
        ],
        failure_probability=configs.Action.failure_probability,
        num_attempts=10,
        requires_x=T,
        requires_y=F,
        requires_i=F,
        requires_l=T,
    ),
}
