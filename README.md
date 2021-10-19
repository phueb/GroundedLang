<div align="center">
 <img src="images/logo.png" width="250"> 
</div>

A Python toolkit for customizing and generating samples of artificial language with semantic structure that is grounded in a simulated world.  

Research-code. Under active development.

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
Primitives are functions that manipulate the spatial coordinate of entities in the world (and possibly parts of entities, e.g. hand, foot).



## Linguistic Descriptions

Currently, the linguistic descriptions of goings-on in the world conform exclusively to argument structure. 
This means that teh sole determinant of the structure of a sentence is argument structure of the verb.

### Grammatical Structure

#### Syntax

The only syntactic rule has to do with ordering of verb arguments. 
There is only one correct ordering.

Each action is uniquely associated with a single verb, which has 1, 2, or 3 required arguments.
The set of required arguments is called the theta-grid.
The 1st argument, called `X`, is always 1st in the linear ordering of words in a sentence.
The 2nd argument, called `Y`, is always 2nd in the linear ordering of words in a sentence.
The 3rd argument, called `Z`, is always 3rd in the linear ordering of words in a sentence.
If a verb requires a `Z`, then it must also require a `Y` and `X`.
If a verb requires a `Y`, then it must also require an `X`.

The sentence structure is as follows. Parentheses enclose optional constituents.

__For all agents:__

X + Verb + (Y)

where Y is never a location, or instrument.

__For a HUMAN agent:__

X + Verb + (Y) + (Z)

X + Verb + (Y) + (Z)

Either Y or Z may refer to a location, or instrument.

Because slots are filled from left to right (e.g. X, Y, Z), and an instrument or location must fill the last slot:
* Z refers to a location or instrument when Y is occupied and does not refer to a location or instrument.
* Y may refer to a location or instrument if Z is not occupied. 


#### Morphology 

No morphological rules as of yet.

### Semantic Structure

### Definiteness

We distinguish between *a squirrel* and *the squirrel*. 
For instance, when a human is looking for a squirrel, it is not any particular squirrel.
Once the human has found a particular squirrel, it is referred to as *the squirrel*.

### S-Selection

Selectional preferences (ie., s-selection) are defined in `semantics/verbs.py`.
S-selection is entirely lexical; that is, each verb selects lexical items - as opposed to categories - as arguments.

### Semantic Roles

Semantic roles are not explicitly defined, but are implicit in the definitions of verbs and their possible arguments.
Semantic roles are not needed because agents always correspond to `X`, and `X` is always in first position in a sentence.
Put differently, there is no need for semantic roles because the position of agents, and patients does not vary. 
If, on the other hand, passive forms of active sentences were included, semantic roles would be useful to distinguish agents from patients.

## Compatibility

Developed on Ubuntu 18.04 and Python 3.7