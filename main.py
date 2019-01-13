import pygame

from src.system import Game

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Evolve")
game = Game.Game(screen)
game.start()
pygame.quit()
