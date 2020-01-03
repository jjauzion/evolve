import pygame

from src.system import Game
from src import constant as C

pygame.init()
screen = pygame.display.set_mode(C.SCREEN_SIZE)
pygame.display.set_caption("Evolve")
game = Game.Game(screen)
game.start()
pygame.quit()
