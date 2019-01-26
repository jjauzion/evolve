import pygame
import math

from src.entity import Cell
from src.constant import *


class Universe:

    def __init__(self):
        self.theta = 0
        self.last_id = 0
        self.all_sprite = pygame.sprite.RenderPlain()

    def __str__(self):
        string = "{} entities alive in universe\n".format(len(self.all_sprite))
        for entity in self.all_sprite:
            print("------->", entity)
            string += "\tCell {}: age:{} ; life:{} ; position:{}\n"\
                .format(entity.id, entity.health.age, entity.health.life, str(entity.position))
        return string

    def _get_new_id(self):
        self.last_id += 1
        return self.last_id

    def create_new_entity(self, position, size, speed_vect=(0, 0), life=100,
                          regen=0, ageing_factor=CELL_AGEING_FACTOR, ageing_start=CELL_AGEING_START):
        if not speed_vect:
            x = math.cos(self.theta)
            y = math.sin(self.theta)
            speed_vect = (x, y)
        new = Cell.Cell(cell_id=self._get_new_id(), position=position, size=size, vector=speed_vect, life=life,
                        regen=regen, ageing_factor=ageing_factor, ageing_start=ageing_start)
        self.all_sprite.add(new)
        self.theta += 0.1 if self.theta <= 2 * math.pi else -self.theta

    def add_entity(self, entity):
        if not isinstance(entity, Cell.Cell):
            raise TypeError("{} is not an instance of Cell".format(entity))
        self.all_sprite.add(entity)
