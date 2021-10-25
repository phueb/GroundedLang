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

### Semantic Structure

### Definiteness

We distinguish between *a squirrel* and *the squirrel*. 
For instance, when a human is looking for a squirrel, it is not any particular squirrel.
Once the human has found a particular squirrel, it is referred to as *the squirrel*.

### S-Selection

Selectional preferences (ie., s-selection) are defined in `semantics/verbs.py`.
S-selection is entirely lexical; that is, each verb selects lexical items - as opposed to categories - as arguments.

### Semantic Roles

There are four semantic roles:
- X
- Y
- I(nstrument)
- L(ocation)

X and Y can be considered Agent and Patient/Theme.


### Additional Constraints

- Non humans stay in set locations, but humans can move anywhere

### Grammatical Structure

#### Syntax

The syntactic structure has to do with ordering of verb arguments. 

Each action is uniquely associated with a single verb, which can have up to 4 required arguments:
- X
- Y 
- I(nstrument)
- L(ocation)

Word order must respect the order X, Y, I, L. 
Required arguments may be dropped by the language system.
In those case, the argument in the next (right) position, simply moves to the previous (left) position.

All possible sentence structures are shown below.

__For all agents:__

X Verb 

X Verb Y

where Y is never a location, or instrument.

__For a HUMAN agent:__

X Verb Y I

X Verb Y I L

X Verb I

X Verb I L

X Verb L

In short, X and Y are always realized to the left, and to to the right of the verb, respectively.
Arguments corresponding to either I or L are optionally realized, and I must precede L.
If Y is absent, but I (or L) is present, then I (or L) follow the verb.
If I is present, I must always precede L.


#### Morphology 

No morphological rules as of yet.

## Compatibility

Developed on Ubuntu 18.04 and Python 3.7