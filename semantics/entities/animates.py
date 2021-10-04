from groundedlang.entity import EntityDefinition, Animate

definitions = [

    # HUMAN

    EntityDefinition(
        name='Mary',
        category='HUMAN',
        cls=Animate,
    ),

    # CARNIVORE

    EntityDefinition(
        name='fox',
        category='CARNIVORE',
        cls=Animate,
    ),

    # HERBIVORE

    EntityDefinition(
        name='squirrel',
        category='HERBIVORE',
        cls=Animate,
    ),
]
