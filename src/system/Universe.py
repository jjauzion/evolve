from src.entity import Cell
import math


class Universe:

    def __init__(self):
        self.entity_list = {}
        self.theta = 0
        self.last_id = 0

    def __str__(self):
        string = "{} entities alive in universe\n".format(len(self.entity_list))
        for ent_id, entity in self.entity_list.items():
            print("------->", entity)
            string += "\tCell {}: age:{} ; life:{} ; position:{}\n"\
                .format(entity.id, entity.component["health"].age, entity.component["health"].life, str(entity.component["position"]))
        return string

    def _get_new_id(self):
        self.last_id += 1
        return self.last_id

    def create_new_entity(self, position, size, speed_vect=(0, 0), life=100, regen=0):
        if not speed_vect:
            x = size * math.cos(self.theta)
            y = size * math.sin(self.theta)
            speed_vect = (x, y)
        new = Cell.Cell(cell_id=self._get_new_id(), position=position, size=size, vector=speed_vect, life=life, regen=regen)
        self.add_entity(new)
        self.theta += 0.1 if self.theta <= 2 * math.pi else -self.theta

    def add_entity(self, entity):
        if not isinstance(entity, Cell.Cell):
            raise TypeError("{} is not an instance of Cell".format(entity))
        self.entity_list[entity.id] = entity
