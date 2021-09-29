"""
This is where all the important parameters are specified that control how the simulation behaves.
"""
from dataclasses import dataclass
from typing import Tuple, Union, Dict, Any

# specify params to submit here
param2requests = {



}

param2debug = {

}

# default params
param2default = {
    'num_turns': 2,
    'max_x': 10,
    'max_y': 10,

}


@dataclass
class Params:
    """
    this object is loaded at the start of job.main() by calling Params.from_param2val(),
    and is populated by Ludwig with hyper-parameters corresponding to a single job.
    """
    num_turns: int
    max_x: int
    max_y: int

    @classmethod
    def from_param2val(cls, param2val):
        """
        instantiate class.
        exclude keys from param2val which are added by Ludwig.
        they are relevant to job submission only.
        """
        kwargs = {k: v for k, v in param2val.items()
                  if k not in ['job_name', 'param_name', 'save_path', 'project_path']}
        return cls(**kwargs)
