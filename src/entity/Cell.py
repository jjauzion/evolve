from src.component import Position
from src.component import Velocity
from src.component import Visible


class Cell:

    def __init__(self, cell_id, position=(0, 0), size=10):
        self.id = cell_id
        self.component = {
            "position": Position.Position(position),
            "velocity": Velocity.Velocity(),
            "visible": Visible.Visible("circle", size)
        }
