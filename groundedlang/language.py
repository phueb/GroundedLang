import logging
import random

from groundedlang.entity import Entity
from groundedlang.event import Action
from groundedlang.workspace import WorkSpace as Ws
from groundedlang import configs

log_language = logging.getLogger('language')

WHITE_SPACE = ' '


def to_phrase(entity: Entity,
              ):

    res = ''

    if entity.category == 'LOCATION':
        res += 'to' + WHITE_SPACE

    if entity.category == 'INSTRUMENT':
        res += 'with' + WHITE_SPACE

    if entity.definite:
        res += 'the' + WHITE_SPACE
    else:
        res += 'a' + WHITE_SPACE

    res += entity.name

    return res


class Corpus:

    def __init__(self):
        self.sentences = []

    def add_sentence_from_action(self,
                                 action: Action,
                                 add_period: bool,
                                 ):
        """
        convert action to sentence and add to corpus.

        Notes:
            A sentence has the structure X VERB Y I L .
            Y, I, and L are optional.
        """

        sentence = ''
        sentence += Ws.x.name + WHITE_SPACE

        if Ws.y:
            sentence += to_phrase(Ws.y) + WHITE_SPACE

        if action.requires_i:
            if random.random() < configs.Language.instrument_probability:
                sentence += Ws.i.name + WHITE_SPACE

        if action.requires_l:
            if random.random() < configs.Language.location_probability:
                sentence += Ws.l.name + WHITE_SPACE

        if add_period:
            sentence += '.'

        self.sentences.append(sentence)
