import pygame
import random
import math

from src.component import Position
from src.component import Velocity
from src.component import Physic
from src.component import Health
from src import module_fct


class Cell(pygame.sprite.Sprite):

    def __init__(self, cell_id, position, size, vector, life, regen, ageing_factor, ageing_start):
        super().__init__()
        self.id = cell_id
        self.position = Position.Position(position)
        self.physic = Physic.Physic(size)
        self.health = Health.Health(life, regen, ageing_factor, ageing_start)
        self.velocity = Velocity.Velocity(vector=vector)
        heading = self.velocity.get_heading_rad()
        self.image, self.rect = module_fct.create_cell_image((255, 255, 255), (255, 0, 0), size, heading)
        self.rect.center = position

    def __str__(self):
        return f'Cell {self.id}: life : [{self.health.life}] ; position: [{self.rect.topleft}, {self.rect.bottomright}]'

    def update(self, *args):
        self.rect.center = self.position.get_position()

    def change_heading(self, heading):
        """
        Change cell's heading
        :param heading:     [float] heading in rad
        """
        self.velocity.polar_vector = {
            "r": self.velocity.polar_vector["r"],
            "theta": heading
        }
        self.image, _ = module_fct.create_cell_image((255, 255, 255), (255, 0, 0), self.physic.size, heading)

    def play(self):
        self.change_heading(random.random() * 2 * math.pi)
        print(f'Cell {self.id} new velocity : {self.velocity.polar_vector}')
