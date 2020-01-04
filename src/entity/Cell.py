import pygame
import random
import math

from src import component
from src import module_fct


class Cell(pygame.sprite.Sprite):

    def __init__(self, cell_id, position, size, vector, life, regen, ageing_factor, ageing_start, energy_max):
        super().__init__()
        self.id = cell_id
        self.position = component.Position(position)
        self.physic = component.Physic(size)
        self.health = component.Health(life, regen, ageing_factor, ageing_start)
        self.energy = component.Energy(energy_max)
        self.image, self.rect = module_fct.create_cell_image((255, 255, 255), (255, 0, 0), size, 0)
        self.rect.center = position
        self.velocity = component.Vector(vector=vector)
        self.acceleration = component.Propulsion(vector=(0, 0), cell=self)

    def __str__(self):
        return f'Cell {self.id}: life : [{self.energy.level} | {self.health.life}] ' \
               f'; position: [{self.rect.topleft}, {self.rect.bottomright}]'

    def update(self, *args):
        self.rect.center = self.position.get_position()

    def change_image(self, image):
        self.image = image
