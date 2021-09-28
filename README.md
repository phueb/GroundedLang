# GroundedLang

A Python-based tool for customizing and generating samples of artificial language with semantic structure that is grounded in a simulated hunter-gatherer world.  



## Design Considerations

- complete independence of the world event semantics (and therefore the event corpus), the linguistic descriptions (and therefore the linguistic corpus), and the code.
- extreme generalizability, with as little as possible hard-coded, and as much as possible procedurally generated from config files.
- customizable config files are human readable and editable in an intuitive way.
     
     
## Documentation

### Events

#### Event Files

Event files are `.csv` files, which contain information about a single event tree. 
Each event tree results in the reduction of a drive-level (e.g. an eating event reduces hunger). 
Each leaf-node in the event tree is obligatory - each leaf-noe is an action that must be performed.
Leaf-nodes are labeled with lower-case verbs, and non-leaf-nodes are labeled with upper-case strings.
Leaf node labels are verbs that may be included in the corpus that describes the goings-on in the simulated world.
Non-leaf node labels are arbitrary strings useful only for the user to conceptually organize event trees, but have no influence on computation.

An example leaf-node label is `transport(x, LOCATION(COOK))`. 
`X` will be substituted with the entity to be transported. The name of this entity is in the file name of the event tree file, (e.g. HERBIVORE).