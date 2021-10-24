from groundedlang.entity import EntityDefinition, Animate

definitions = [

    # HUMAN

    EntityDefinition(
        name='Mary',
        categories=['HUMAN'],
        cls=Animate,
    ),

    EntityDefinition(
        name='Jon',
        categories=['HUMAN'],
        cls=Animate,
    ),

    EntityDefinition(
        name='Bill',
        categories=['HUMAN'],
        cls=Animate,
    ),


    # CARNIVORE

    EntityDefinition(
        name='fox',
        categories=['CARNIVORE'],
        cls=Animate,
    ),

    # HERBIVORE

    EntityDefinition(
        name='squirrel',
        categories=['HERBIVORE'],
        cls=Animate,
    ),
]
