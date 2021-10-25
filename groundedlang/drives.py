class Drive:
    def __init__(self):
        self.level = 100

    def down(self):
        self.level += 1

    def reset(self):
        self.level = 100


class Hunger(Drive):
    def __init__(self):
        super().__init__()

        self.event_type = 'eat'


class Thirst(Drive):
    def __init__(self):
        super().__init__()

        self.event_type = 'drink'


class Fatigue(Drive):
    def __init__(self):
        super().__init__()

        self.event_type = 'sleep'
