

from groundedlang.success import Success
from groundedlang.workspace import WorkSpace
from groundedlang.primitives import Move
from groundedlang.primitives import InspectLocation

from groundedlang.location import Location
from groundedlang.verb import Verb

lexicon = {
    Verb(
        name='look_for(X)',
        primitives=[
            (Move, [Location]),
            (InspectLocation, [WorkSpace.results, WorkSpace.X]),  # inspect location moved to, and check for X
        ],
        success=Success.is_equal(WorkSpace.results, WorkSpace.X),
        num_attempts=10,
    ),

}
