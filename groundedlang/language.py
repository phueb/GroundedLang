import logging

from groundedlang.entity import Entity

log_language = logging.getLogger('language')


def to_noun_phrase(entity: Entity,
                   ):

    res = ''

    if entity.category == 'LOCATION':
        res += 'to '

    if entity.definite:
        res += 'the '
    else:
        res += 'a '

    res += entity.name

    return res


class Corpus:

    def __init__(self):
        self.sentences = []
