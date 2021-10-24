

class Language:
    location_probability: float = 0.5
    instrument_probability: float = 0.5


class Drives:
    fatigue = 'FATIGUE'
    hunger = 'HUNGER'
    thirst = 'THIRST'


class Action:
    failure_probability = 0.0