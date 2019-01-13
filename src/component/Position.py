class Position:

    def __init__(self, position=(0, 0)):
        self.x = position[0]
        self.y = position[1]

    def __str__(self):
        return "(x:{} ; y:{})".format(self.x, self.y)

    def get_position(self):
        return self.x, self.y
