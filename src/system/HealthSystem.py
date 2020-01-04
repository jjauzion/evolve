from src.constant import *


class HealthSystem:

    def ageing(self, entity_list, cycle):
        if cycle % CYCLE_IN_YEAR == 0:
            for entity in entity_list:
                entity.health.age += 1
                if entity.health.ageing_start is not None and entity.health.age > entity.health.ageing_start:
                    entity.health.max_life -= entity.health.ageing_factor

    def update_health(self, entity_list):
        for entity in entity_list:
            if entity.health.life < entity.health.max_life:
                entity.health.life += entity.health.regen
            if entity.health.life > entity.health.max_life:
                entity.health.life = entity.health.max_life
            if entity.energy.level <= 0:
                entity.health.life -= 1
                entity.energy.level += CELL_ENERGY_TO_LIFE_RATIO
