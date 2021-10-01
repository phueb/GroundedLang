import logging

from groundedlang.entity import Entity
from groundedlang.workspace import WorkSpace as Ws


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

        self.log = logging.getLogger('corpus')


def make_sentence(action):
    # transitive
    if action.requires_x and action.requires_y and not action.requires_z:
        sentence = f'{Ws.x.name} {action.name} {to_noun_phrase(Ws.y)}'
    # ditransitive
    elif action.requires_x and action.requires_y and action.requires_z:
        sentence = f'{Ws.x.name} {action.name} {to_noun_phrase(Ws.y)} {to_noun_phrase(Ws.z)}'
    else:
        raise RuntimeError

    return sentence
