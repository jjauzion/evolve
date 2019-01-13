import pygame
from pygame import locals as const

from src.system import Universe
from src.system import Draw


class Game:
    def __init__(self, screen=pygame.Surface):
        self.screen = screen
        self.loop = True
        self.universe = Universe.Universe()
        self.draw = Draw.Draw()

    def prepare(self):
        pygame.key.set_repeat(200, 50)
        self.loop = True

    def update_screen(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0) + self.screen.get_size())
        self.draw.draw(self.universe.entity_list, self.screen)

    def process_event(self, event=pygame.event):
        if event.type == const.QUIT or (event.type == const.KEYUP and event.key == const.K_ESCAPE):
            self.loop = False
        elif event.type == const.MOUSEBUTTONUP and event.button == 1:
            self.universe.create_new_entity(event.pos, 20)
            self.update_screen()

    def start(self):
        self.prepare()
        while self.loop:
            for event in pygame.event.get():
                self.process_event(event)
            pygame.display.flip()
