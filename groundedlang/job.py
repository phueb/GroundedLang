from typing import Dict, Any
import colorlog

from groundedlang.language import Corpus, make_sentence
from groundedlang.world import World
from groundedlang.params import Params


handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    fmt='%(log_color)s%(levelname)s:%(name)s:%(message)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'black',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
))

log_main = colorlog.getLogger('main')
log_main.addHandler(handler)
log_main.setLevel('DEBUG')


def main(param2val: Dict[str, Any]):

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

            # convert action into 1 sentence
            sentence = make_sentence(action, params.add_period)

            corpus.sentences.append(sentence)
            log_main.info(sentence)

    return []

