



## Design Consideration

- complete independence of the world event semantics (and therefore the event corpus), the linguistic descriptions (and therefore the linguistic corpus), and the modeling code.
- extreme generalizability, with as little as possible hard-coded, and as much as possible procedurally generated from config files.
- making config files human readable and editable in an intuitive way will be key and something we should talk about. i can think of three kinds of things we want to script:
     - fixed properties of entities
     - evolvable properties of entities
     - event structures/sequences and arguments/adjuncts