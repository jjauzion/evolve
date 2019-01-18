import pygame
from pygame import locals as const
import time

from src.system import Universe
from src.system import Draw
from src.system import Move
from src.system import Ageing
from src.system import Death


def timer(funct):
    def timed_func(*args):
        before = time.time()
        return_val = funct(*args)
        after = time.time()
        print("{} sec spent in function {}".format(after - before, function))
        return return_val
    return timed_func()


class Game:
    def __init__(self, screen=pygame.Surface):
        self.screen = screen
        self.cycle = 0
        self.universe = Universe.Universe()
        self.draw = Draw.Draw()
        self.move = Move.Move()
        self.death = Death.Death()
        self.ageing = Ageing.Ageing()

    def __str__(self):
        string = "Cycle {}:\n".format(self.cycle)
        string += str(self.universe)
        return string

    def prepare(self):
        pygame.key.set_repeat(200, 50)
        self.cycle = 0
        self.universe.create_new_entity((320, 300), 20, (0, 0), 100, 0)

    def update_screen(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0) + self.screen.get_size())
        self.draw.draw(self.universe.entity_list, self.screen)

    def process_event(self, event=pygame.event):
        if event.type == const.QUIT or (event.type == const.KEYUP and event.key == const.K_ESCAPE):
            self.cycle = -1
        elif event.type == const.MOUSEBUTTONUP and event.button == 1:
            self.universe.create_new_entity(event.pos, 20, None, 100, 0)

    def exe_cycle(self):
        before = time.time()
        print(self.__str__())
        self.move.move_entity(self.universe.entity_list)
        self.ageing.ageing(entity_list=self.universe.entity_list, cycle=self.cycle)
        self.death.death(self.universe.entity_list)
        self.update_screen()
        self.cycle += 1
        for event in pygame.event.get():
            self.process_event(event)
        pygame.display.flip()
        print("cycle {} took {}s to run".format(self.cycle, time.time() - before))

    def start(self):
        self.prepare()
        while self.cycle >= 0:
            self.exe_cycle()
