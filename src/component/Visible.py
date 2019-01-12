import pygame


class Visible:

    def __init__(self, shape, size):
        self.shape = shape
        self.size = size

    def draw(self, screen, color, position, radius, width):
        if self.shape == "circle":
            pygame.draw.circle(screen, color, position, radius, width)
