# GroundedLang

A Python-based tool for customizing and generating samples of artificial language with semantic structure that is grounded in a simulated hunter-gatherer world.  



## Design Considerations

- complete independence of the world event semantics (and therefore the event corpus), the linguistic descriptions (and therefore the linguistic corpus), and the code.
- extreme generalizability, with as little as possible hard-coded, and as much as possible procedurally generated from config files.
- customizable config files are human readable and editable in an intuitive way.
     
     
## Documentation

### Events

#### Event Files

Event files are `.py` files, which contain information about all possible event sequences that result in the reduction of one drive-level (e.g. an eating event reduces hunger). 
All steps in the event sequence are obligatory.
All steps are labeled by verbs that may will be used to generate the linguistic corpus.

An example label of an event step is `transport(x, LOCATION(COOK))`. 
`X` will be substituted with the entity to be transported (e.g. HERBIVORE).