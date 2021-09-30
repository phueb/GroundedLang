
from groundedlang.entity import Entity


class Corpus:

    def __init__(self):
        self.sentences = []

    def to_noun_phrase(self,
                       entity: Entity,
                       ):

        res = ''

        if entity.definite:
            res += 'the '
        else:
            res += 'a '

        res += entity.name

        return res


