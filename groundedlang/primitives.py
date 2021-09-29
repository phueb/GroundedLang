

class Primitive:
    pass


class PrimitiveArg:
    pass


class Move(Primitive):
    pass


class InspectLocation(Primitive):
    pass


class Variables:
    X = None  # todo
    PreviousOutput = None


class Success:

    @classmethod
    def is_equal(cls, *args):
        raise NotImplementedError