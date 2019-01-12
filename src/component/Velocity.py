class Velocity:

    def __init__(self, vector=(1, 0), speed=0):
        self.vector = vector
        self.value = speed

    def get_xspeed(self):
        return self.vector[0] * self.value

    def get_yspeed(self):
        return self.vector[1] * self.value
