from typing import Dict, Any
from pathlib import Path

from groundedlang.corpus import Corpus, to_noun_phrase
from groundedlang.world import World
from groundedlang.params import Params
from groundedlang.workspace import WorkSpace as Ws


def main(param2val: Dict[str, Any],
         ):

    # params
    params = Params.from_param2val(param2val)
    print(params)

    # project_path = Path(param2val['project_path'])
    # save_path = Path(param2val['save_path'])

    # in case job is run locally, we must create save_path
    # if not save_path.exists():
    #     save_path.mkdir(parents=True)

    corpus = Corpus()

    world = World(max_x=params.max_x,
                  max_y=params.max_y,
                  )

    for turn in range(params.num_turns):

        print('-' * 60)
        print(f'turn={turn}')

        # 1 turn iterates over all animates, and gives each a chance to complete 1 event
        for action in world.turn():

            # transitive
            if action.requires_x and action.requires_y and not action.requires_z:
                sentence = f'{Ws.x} {action.name} {to_noun_phrase(Ws.y)}'
            # ditransitive
            elif action.requires_x and action.requires_y and action.requires_z:
                sentence = f'{Ws.x} {action.name} {to_noun_phrase(Ws.y)} {to_noun_phrase(Ws.z)}'
            else:
                raise RuntimeError

            print(sentence)
            corpus.sentences.append(sentence)
