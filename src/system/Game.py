import pygame
from pygame import locals as const
import time
import random
import math

from src.system import Universe
from src.system import Move
from src.system import HealthSystem
from src.system import EnergySystem
from src.system import Death
from src.system import Collision
from src.system import FoodGenerator
from src import module_fct
from src.constant import *


def timer(funct):
    def timed_func(*args):
        before = time.time()
        return_val = funct(*args)
        after = time.time()
        print("{} sec spent in function {}".format(after - before, funct))
        return return_val
    return timed_func()


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.cycle = 0
        self.universe = Universe.Universe(size=SCREEN_SIZE)
        self.move = Move.Move(screen_size=SCREEN_SIZE)
        self.death = Death.Death()
        self.health_system = HealthSystem.HealthSystem()
        self.energy_system = EnergySystem.EnergySystem()
        self.collision = Collision.Collision()
        self.food_generator = FoodGenerator.FoodGenerator(proba=0.01)
        self.background = pygame.Surface(screen.get_size()).convert()
        self.background.fill((0, 191, 255))
        self.selected_cell = None

    def __str__(self):
        string = "Cycle {}:\n".format(self.cycle)
        string += str(self.universe)
        return string

    def prepare(self):
        self.screen.blit(self.background, (0, 0))
        pygame.key.set_repeat(200, 50)
        self.cycle = 0
        self.universe.create_new_entity((320, 300), 20, (0, 0), CELL_INIT_LIFE, 0)

    def update_screen(self):
        self.universe.all_sprite.update()
        self.screen.blit(self.background, (0, 0))
        self.universe.all_sprite.draw(self.screen)
        pygame.display.flip()

    def process_event(self, event=pygame.event):
        direction_key = [const.K_UP, const.K_DOWN, const.K_LEFT, const.K_RIGHT]
        if event.type == const.QUIT or (event.type == const.KEYUP and event.key == const.K_ESCAPE):
            self.cycle = -1
        elif event.type == const.MOUSEBUTTONUP and event.button == 3:
            self.universe.create_new_entity(event.pos, 20, None)
        elif event.type == const.MOUSEBUTTONDOWN and event.button == 1:
            print(f'event pos: {event.pos}')
            for cell in self.universe.all_sprite:
                print(f'{cell}')
                if module_fct.coord_in_rect(event.pos, cell.rect):
                    self.selected_cell = cell
                    print(f'Cell {cell.id} selected')
        elif self.selected_cell is not None and event.type == const.KEYDOWN and event.key in direction_key:
            if event.key == const.K_UP:
                self.selected_cell.acceleration.increase_norm(1)
                print(f'Cell {self.selected_cell.id} new accel: {self.selected_cell.acceleration.get_norm()}')
            elif event.key == const.K_DOWN:
                self.selected_cell.acceleration.increase_norm(-1)
                print(f'Cell {self.selected_cell.id} new accel: {self.selected_cell.acceleration.get_norm()}')
            elif event.key == const.K_LEFT:
                self.selected_cell.acceleration.increase_heading(10 * math.pi / 180.)
                print(f'Cell {self.selected_cell.id} heading changed to {self.selected_cell.acceleration.get_heading_deg()}')
            elif event.key == const.K_RIGHT:
                self.selected_cell.acceleration.increase_heading(-10 * math.pi / 180.)
                print(f'Cell {self.selected_cell.id} heading changed to {self.selected_cell.acceleration.get_heading_deg()}')

    def exe_cycle(self):
        before = time.time()
        #print(self.__str__())
        self.move.move_entity(self.universe.all_sprite)
        self.energy_system.spend_energy(entity_list=self.universe.living_entity)
        self.energy_system.update_energy(entity_list=self.universe.living_entity)
        self.health_system.update_health(entity_list=self.universe.living_entity)
        self.health_system.ageing(entity_list=self.universe.living_entity, cycle=self.cycle)
        self.death.death(self.universe.living_entity, self.cycle)
        for cell in self.universe.living_entity:
            self.collision.collision_with_list(cell, self.universe.all_sprite)
        self.move.move_entity(self.universe.all_sprite)
        self.food_generator.generate(self.universe, cycle=self.cycle)
        self.update_screen()
        self.cycle += 1
        for event in pygame.event.get():
            self.process_event(event)
        #print("cycle {} took {}s to run".format(self.cycle, time.time() - before))

    def start(self):
        self.prepare()
        while self.cycle >= 0:
            self.exe_cycle()
