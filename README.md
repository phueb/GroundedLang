# GroundedLang

A Python-based tool for customizing and generating samples of artificial language with semantic structure that is grounded in a simulated hunter-gatherer world.  



## Design Considerations

- complete independence of the world event semantics in `semantics`, the linguistic descriptions, and the code in `groundedlang`.
- extreme generalizability, with as little as possible hard-coded, and as much as possible procedurally generated from config files.
- customizable config files are human readable and editable in an intuitive way.

- The names of Python objects should not refer to customizable entity names like `human` or `squirrel`. 
     
     
## Documentation

### Events

#### Event Files

Event files are `.py` files, which contain information about all possible event sequences that result in the reduction of one drive-level (e.g. an eating event reduces hunger). 
All actions in the event sequence are obligatory.
All actions correspond to verbs that will be used to generate the linguistic corpus.
All actions are defined in terms of a set of primitives and their arguments.

### Primitives

Primitives are the only hard-coded functions that are allowed to operate on the world.
 

### Corpus and Grammar

#### Theta-Grid

Each action is uniquely associated with a single verb, which is 1, 2, or 3 required arguments.
The set of required arguments is called the theta-grid.
The first argument, which is also always the first in the linear ordering of words in a sentence, is called `X`.
The second argument, which is also always the second in the linear ordering of words in a sentence, is called `Y`.
The third argument, which is also always the second in the linear ordering of words in a sentence, is called `Z`.

#### Definiteness
