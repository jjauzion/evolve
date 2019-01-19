import pygame
from pygame.locals import *


def load_image(pic_path, size=None, colorkey=None, heading=None):
    try:
        image = pygame.image.load(pic_path)
    except pygame.error:
        raise SystemError("Cannot load image {}".format(pic_path))
    image = image.convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    if heading:
        image = pygame.transform.rotate(image, heading)
    if colorkey:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def rotation_image(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect

