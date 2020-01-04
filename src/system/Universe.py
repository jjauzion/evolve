import pygame
import math
import random

from src import entity as ent
from src.constant import *


class Universe:

    def __init__(self, size):
        self.size = size
        self.last_id = 0
        self.all_sprite = pygame.sprite.RenderPlain()
        self.living_entity = pygame.sprite.Group()

    def __str__(self):
        string = "{} entities alive in universe\n".format(len(self.all_sprite))
        for entity in self.all_sprite:
            print("------->", entity)
            string += "\tCell {}: age:{} ; life:{} ; position:{}\n"\
                .format(entity.id, entity.health.age, entity.health.life, str(entity.position))
        return string

    def get_new_id(self):
        self.last_id += 1
        if self.last_id > MAX_ENTITY:
            raise RuntimeError(f'Max entity id number reached. No id recycling implemented yet...')
        return self.last_id

    def create_new_entity(self, position, size, speed_vect=(0, 0), life=CELL_INIT_LIFE,
                          regen=0, ageing_factor=CELL_AGEING_FACTOR, ageing_start=CELL_AGEING_START,
                          energy_max=100):
        if not speed_vect:
            heading = random.random() * 2 * math.pi
            x = math.cos(heading)
            y = math.sin(heading)
            speed_vect = (x, y)
        new = ent.Cell(cell_id=self.get_new_id(), position=position, size=size, vector=speed_vect, life=life,
                       regen=regen, ageing_factor=ageing_factor, ageing_start=ageing_start, energy_max=energy_max)
        print(f'new cell polar vect = {new.velocity.polar_vector}')
        self.all_sprite.add(new)
        self.living_entity.add(new)

    def add_entity(self, entity):
        if not isinstance(entity, ent.Cell):
            raise TypeError("{} is not an instance of Cell".format(entity))
        self.all_sprite.add(entity)
