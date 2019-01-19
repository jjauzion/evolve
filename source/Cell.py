import pygame

from source import module_fct


class Cell(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.original, self.rect = module_fct.load_image("resources/cell.png", size=(60, 60))
        self.image = self.original

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos
