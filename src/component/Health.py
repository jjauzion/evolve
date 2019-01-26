class Health:

    def __init__(self, life, regen, ageing_factor, ageing_start):
        self.life = life
        self.max_life = life
        self.regen = regen
        self.ageing_factor = ageing_factor
        self.ageing_start = ageing_start
        self.age = 0
