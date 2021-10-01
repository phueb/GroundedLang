
from groundedlang.entity import Entity


def to_noun_phrase(entity: Entity,
                   ):

    res = ''

    if entity.definite:
        res += 'the '
    else:
        res += 'a '

    res += entity.name

    return res


class Corpus:

    def __init__(self):
        self.sentences = []


