import random

from src import entity


class FoodGenerator:

    def __init__(self, proba=0.9, seed=None):
        random.seed(seed)
        self.proba = proba

    def generate(self, universe, cycle):
        nb = random.random()
        if nb < self.proba:
            print(f'nb= {nb} | proba = {self.proba}')
            x = random.randint(0, universe.size[0])
            y = random.randint(0, universe.size[1])
            ent_id = universe.get_new_id()
            new_food = entity.Food(ent_id, (x, y))
            universe.all_sprite.add(new_food)
            universe.living_entity.add(new_food)
            print(f'{cycle} | New food {new_food.id} generated')
