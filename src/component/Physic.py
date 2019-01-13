import math

from src.constant import *


class Physic:

    def __init__(self, size):
        self.size = size
        self.mass = math.pi * size * size * DENSITY
