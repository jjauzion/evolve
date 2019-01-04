class Entity:

    def __init__(self):
        self.weight_min = 80
        self.energy_storage_capacity = 1000
        self.power_max = 1000

        self.energy = 500
        self.weight = self.weight_min + self.energy
        self.size = self.weight

        self.position = {"x": 0, "y": 0}
        self.velocity = {"x": 0, "y": 0}


    def move(self, power, direction):
        energy_cost, velocity
