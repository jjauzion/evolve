import pygame
from pygame.locals import *
import math


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


def rotate_image(image, angle):
    """rotate an image while keeping its center and size. Only works for square images."""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def create_cell_image(color_circle, color_line, size, heading):
    """
    create a surface with a circle drawn and a line showing the heading
    :param color_circle:        [tuple (int, int, int)] color of the circle (R, G, B)
    :param color_line:          [tuple (int, int, int)] color of the line (R, G, B)
    :param size:                [int]                   diameter of the circle
    :param heading:             [float]                 heading, in rad, to show direction
    :return:                    [pygame.Surface, rect]  image as surface, rectangle of the surface
    """
    image = pygame.Surface((size, size), SRCALPHA, 32).convert_alpha()
    center_x = size // 2
    center_y = size // 2
    pygame.draw.circle(image, color_circle, (center_x, center_y), size // 2)
    y = round(center_x + size * math.sin(heading))
    x = round(center_y + size * math.cos(heading))
    pygame.draw.line(image, color_line, (center_x, center_y), (x, y), 3)
    return image, image.get_rect()


def create_food_image(color, width, height):
    """
    create a surface with a circle drawn and a line showing the heading
    :param color: color of the entity
    :param width: width of the rectangle
    :param height: length of the rectangle
    :return: image as surface, rectangle of the surface
    """
    image = pygame.Surface((width, height), SRCALPHA, 32).convert_alpha()
    pygame.draw.rect(image, color, image.get_rect())
    return image, image.get_rect()


def coord_in_rect(coord, rect):
    """
    check if a point of coordinate 'coord' is within the rectangle 'rect'
    :param coord:       [tuple of int]  (x, y): coordinate of the point
    :param rect:        [obj]           Position of the rectangle defined by its top left and bottom right corner.
                                        rect object shall have the following attributes:
                                        rect.topleft  = (x, y)
                                        rect.bottomright  = (x, y)
    :return:            [bool]          True if 'coord' is in 'rect' ; else return False
    """
    if rect.bottomright[0] > coord[0] > rect.topleft[0]:
        if rect.bottomright[1] > coord[1] > rect.topleft[1]:
            return True
    return False

