import pygame
from pygame.locals import *

from source import Cell

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Evovle")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 191, 255))

screen.blit(background, (0, 0))
pygame.display.update()

clock = pygame.time.Clock()

all_sprite = pygame.sprite.RenderPlain()

loop = True
while loop:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            loop = False
        elif event.type == MOUSEBUTTONDOWN:
            cell = Cell.Cell()
            all_sprite.add(cell)
    all_sprite.update()
    screen.blit(background, (0, 0))
    all_sprite.draw(screen)
    pygame.display.update()
pygame.quit()
