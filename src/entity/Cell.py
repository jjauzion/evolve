from src.component import Position
from src.component import Velocity
from src.component import Visible
from src.component import Physic
from src.component import Health


class Cell:

    def __init__(self, cell_id, position, size, vector, life, regen):
        self.id = cell_id
        vector = vector
        self.component = {
            "position": Position.Position(position),
            "velocity": Velocity.Velocity(vector=vector),
            "visible": Visible.Visible("cell"),
            "physic": Physic.Physic(size),
            "health": Health.Health(life, regen)
        }

    def __str__(self):
        return "Cell {}: component : {{}}".format(self.id, self.component)
