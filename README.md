# GroundedLang

A Python-based tool for customizing and generating samples of artificial language with semantic structure that is grounded in a simulated hunter-gatherer world.  



## Design Considerations

- complete independence of the world event semantics in `semantics`, the linguistic descriptions, and the code in `groundedlang`.
- extreme generalizability, with as little as possible hard-coded, and as much as possible procedurally generated from config files.
- customizable config files are human readable and editable in an intuitive way.

- The names of Python objects should not refer to customizable entity names like `human` or `squirrel`. 
     
     
## The World

### Events

Events are sequences of actions that result in the reduction of one drive-level (e.g. an eating event reduces hunger). 
Events are defined using `.py` files in `semantics`.
All actions in the event sequence are obligatory.
All actions correspond to verbs that will be used to generate the linguistic corpus.
All actions are defined in terms of a set of primitives and their arguments.

### Primitives

Primitives are the only hard-coded functions that are allowed to operate on the world.
Primitives are functions that manipulate the spatial location of entities in the world (and possibly parts of entities, e.g. hand, foot).



## Linguistic Descriptions

### Grammatical Structure

#### Theta Roles

The only grammatical rule has to do with ordering of verb arguments. 
There is only one correct ordering.

Each action is uniquely associated with a single verb, which has 1, 2, or 3 required arguments.
The set of required arguments is called the theta-grid.
The 1st argument, called `X`, is always 1st in the linear ordering of words in a sentence.
The 2nd argument, called `Y`, is always 2nd in the linear ordering of words in a sentence.
The 3rd argument, called `Z`, is always 3rd in the linear ordering of words in a sentence.
If a verb requires a `Z`, then it must also require a `Y` and `X`.
If a verb requires a `Y`, then it must also require an `X`.

### Semantic Structure

### Definiteness

### S-Selection

Selectional preferences (ie., c-selection) is defined in `semantics/verbs.py`.

### Semantic Roles

Semantic roles are not explicitly defined, but are implicit in the definitions of verbs and their possible arguments.
