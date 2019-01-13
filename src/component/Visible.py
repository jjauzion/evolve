import pygame
import math


class Visible:

    def __init__(self, shape):
        self.shape = shape

    def draw(self, screen, color, position, size, width, vector, polar_vector):
        if self.shape == "cell":
            pygame.draw.circle(screen, color, (round(position[0]), round(position[1])), size, width)
            y = position[1] + size * 2 * math.sin(polar_vector["theta"])
            x = position[0] + size * 2 * math.cos(polar_vector["theta"])
            print("position = {} ; vector = {} ; (x, y) = {}".format(position, vector, (x, y)))
            pygame.draw.line(screen, color, position, (x, y), 3)
