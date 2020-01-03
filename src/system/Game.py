import pygame
from pygame import locals as const
import time
import random
import math

from src.system import Universe
from src.system import Move
from src.system import Health_system
from src.system import Death
from src.system import Collision
from src import module_fct


def timer(funct):
    def timed_func(*args):
        before = time.time()
        return_val = funct(*args)
        after = time.time()
        print("{} sec spent in function {}".format(after - before, function))
        return return_val
    return timed_func()


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.cycle = 0
        self.universe = Universe.Universe()
        self.move = Move.Move(screen_size=(640, 480))
        self.death = Death.Death()
        self.health_system = Health_system.Health_system()
        self.collision = Collision.Collision()
        self.background = pygame.Surface(screen.get_size()).convert()
        self.background.fill((0, 191, 255))

    def __str__(self):
        string = "Cycle {}:\n".format(self.cycle)
        string += str(self.universe)
        return string

    def prepare(self):
        self.screen.blit(self.background, (0, 0))
        pygame.key.set_repeat(200, 50)
        self.cycle = 0
        self.universe.create_new_entity((320, 300), 20, (0, 0), 100, 0)

    def update_screen(self):
        self.universe.all_sprite.update()
        self.screen.blit(self.background, (0, 0))
        self.universe.all_sprite.draw(self.screen)
        pygame.display.flip()

    def process_event(self, event=pygame.event):
        if event.type == const.QUIT or (event.type == const.KEYUP and event.key == const.K_ESCAPE):
            self.cycle = -1
        elif event.type == const.MOUSEBUTTONUP and event.button == 3:
            self.universe.create_new_entity(event.pos, 20, None, 100, 0)
        elif event.type == const.MOUSEBUTTONDOWN and event.button == 1:
            print(f'event pos: {event.pos}')
            for cell in self.universe.all_sprite:
                print(f'{cell}')
                if module_fct.coord_in_rect(event.pos, cell.rect):
                    print(f'Old heading = {cell.velocity.get_heading_deg()}')
                    cell.change_heading(random.random() * 2 * math.pi)
                    print(f'New heading = {cell.velocity.get_heading_deg()}')

    def exe_cycle(self):
        before = time.time()
        #print(self.__str__())
        self.move.move_entity(self.universe.all_sprite)
        self.health_system.update_health(entity_list=self.universe.all_sprite)
        self.health_system.ageing(entity_list=self.universe.all_sprite, cycle=self.cycle)
        self.death.death(self.universe.all_sprite)
        for cell in self.universe.all_sprite:
            self.collision.collision_with_list(cell, self.universe.all_sprite)
        self.move.move_entity(self.universe.all_sprite)
        self.update_screen()
        self.cycle += 1
        for event in pygame.event.get():
            self.process_event(event)
        #print("cycle {} took {}s to run".format(self.cycle, time.time() - before))

    def start(self):
        self.prepare()
        while self.cycle >= 0:
            self.exe_cycle()
