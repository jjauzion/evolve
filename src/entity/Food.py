import pygame

from src.component import Position
from src.component import Physic
from src.component import Health
from src import module_fct


class Food(pygame.sprite.Sprite):

    def __init__(self, cell_id, position, size, life, regen, ageing_factor, ageing_start):
        pygame.sprite.Sprite.__init__(self)
        self.id = cell_id
        self.position = Position.Position(position)
        self.physic = Physic.Physic(size)
        self.health = Health.Health(life, regen, ageing_factor, ageing_start)
        self.image, self.rect = module_fct.create_food_image(color=(0, 255, 0), width=5, height=5)
        self.rect.center = position

    def __str__(self):
        return "Cell {}: life : [{}]".format(self.id, self.health.life)

    def update(self, *args):
        self.rect.center = self.position.get_position()
