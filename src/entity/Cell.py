from src.component import Position
from src.component import Velocity
from src.component import Visible
from src.component import Physic


class Cell:

    def __init__(self, cell_id, position, size, vector):
        self.id = cell_id
        vector = vector
        self.component = {
            "position": Position.Position(position),
            "velocity": Velocity.Velocity(vector=vector),
            "visible": Visible.Visible("cell"),
            "physic": Physic.Physic(size)
        }
