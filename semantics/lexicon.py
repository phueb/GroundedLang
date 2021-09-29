

from groundedlang.primitives import Variables, Success
from groundedlang.primitives import Move
from groundedlang.primitives import InspectLocation

from groundedlang.location import Location
from groundedlang.verb import Verb

lexicon = {
    Verb(
        name='look_for(X)',
        primitives=[
            (Move, [Location]),
            (InspectLocation, [Variables.PreviousOutput, Variables.X]),  # inspect location moved to, and check for X
        ],
        success=Success.is_equal(Variables.PreviousOutput, Variables.X),
    ),

}
