import pygame
from pygame.locals import *


def load_image(pic_path, size=None, colorkey=None):
    try:
        image = pygame.image.load(pic_path)
    except pygame.error:
        raise SystemError("Cannot load image {}".format(pic_path))
    if size:
        image = pygame.transform.scale(image, size)
    image = image.convert_alpha()
    if colorkey:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

