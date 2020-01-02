import pygame
import random

from src.component import Position
from src.component import Velocity
from src.component import Physic
from src.component import Health
from src import module_fct


class Cell(pygame.sprite.Sprite):

    def __init__(self, cell_id, position, size, vector, life, regen, ageing_factor, ageing_start):
        pygame.sprite.Sprite.__init__(self)
        self.id = cell_id
        self.position = Position.Position(position)
        self.physic = Physic.Physic(size)
        self.health = Health.Health(life, regen, ageing_factor, ageing_start)
        self.velocity = Velocity.Velocity(vector=vector)
        heading = self.velocity.get_heading_rad()
        self.image, self.rect = module_fct.create_cell_image((255, 255, 255), (255, 0, 0), size, heading)
        self.rect.center = position

    def __str__(self):
        return "Cell {}: life : [{}]".format(self.id, self.health.life)

    def update(self, *args):
        self.rect.center = self.position.get_position()

    def play(self):
