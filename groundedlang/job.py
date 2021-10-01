from typing import Dict, Any
import logging

from groundedlang.language import Corpus, make_sentence
from groundedlang.world import World
from groundedlang.params import Params


def main(param2val: Dict[str, Any],
         ):

    logging.basicConfig(level='INFO')
    log_main = logging.getLogger('main')

    # params
    params = Params.from_param2val(param2val)
    log_main.info(params)

    # ------------ Ludwig-specific

    # project_path = Path(param2val['project_path'])
    # save_path = Path(param2val['save_path'])

    # in case job is run locally, we must create save_path
    # if not save_path.exists():
    #     save_path.mkdir(parents=True)

    # ------------ Ludwig-specific

    corpus = Corpus()

    world = World(max_x=params.max_x,
                  max_y=params.max_y,
                  )

    for turn in range(params.num_turns):

        log_main.info('-' * 60)
        log_main.info(f'turn={turn}')

        # 1 turn iterates over all animates, and gives each a chance to complete 1 event
        for action in world.turn():

            sentence = make_sentence(action)

            corpus.sentences.append(sentence)
            corpus.log.info(sentence)


