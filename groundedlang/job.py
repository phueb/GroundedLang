from typing import Dict, Any
from pathlib import Path

from groundedlang.world import World
from groundedlang.params import Params



def main(param2val: Dict[str, Any],
         ):  # todo make ludwig compatible

    # params
    params = Params.from_param2val(param2val)
    print(params)

    project_path = Path(param2val['project_path'])
    save_path = Path(param2val['save_path'])

    # in case job is run locally, we must create save_path
    if not save_path.exists():
        save_path.mkdir(parents=True)

    world = World()

    for turn in range(params.num_turns):
        world.turn()
