"""
An unordered collection of event sequences that end with an eating activity.
There may be multiple sequences that are legal for a given entity.
Sequences are differentiated by what is eaten: This can be a category of entities, or specific members.


Arguments to verbs are X, Y, Z, always in this order.
What types these variables refer to must be documented in lexicon.py

"""


sequences = {

    # a possible event sequence for any entity that is an herbivore
    'HERBIVORE': [
        'look_for(X)',
        'chase(X)',
        'stab(X)',
        'lift(X)',
        'transport(X,Y)',
        'heat(X)',
        'cook(X)',
        'eat(X)',
    ],

    # a possible event sequence for the food entity
    'FOOD': [
        'go_to(X)',
        'transport(X,Y)',
        'heat(X)',
        'cook(X)',
        'eat(X)',
    ]



}
