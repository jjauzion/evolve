from src.system import Draw
from src.system import Move
from src.entity import Cell


class Universe:

    def __init__(self):
        self.entity_list = []

    def _get_new_id(self):
        if len(self.entity_list) == 0:
            return 0
        return self.entity_list[-1].id + 1

    def create_new_entity(self, position, size):
        new = Cell.Cell(cell_id=self._get_new_id(), position=position, size=size)
        self.add_entity(new)

    def add_entity(self, entity):
        if not isinstance(entity, Cell.Cell):
            raise TypeError("{} is not an instance of Cell".format(entity))
        self.entity_list.append(entity)

