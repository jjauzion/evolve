from src.entity import Cell
import math


class Universe:

    def __init__(self):
        self.entity_list = []
        self.theta = 0

    def _get_new_id(self):
        if len(self.entity_list) == 0:
            return 0
        return self.entity_list[-1].id + 1

    def create_new_entity(self, position, size):
        x = size * math.cos(self.theta)
        y = size * math.sin(self.theta)
        new = Cell.Cell(cell_id=self._get_new_id(), position=position, size=size, vector=(x, y))
        self.add_entity(new)
        self.theta += 0.1 if self.theta <= 2 * math.pi else -self.theta

    def add_entity(self, entity):
        if not isinstance(entity, Cell.Cell):
            raise TypeError("{} is not an instance of Cell".format(entity))
        self.entity_list.append(entity)

