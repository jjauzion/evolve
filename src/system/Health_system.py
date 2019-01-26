from src.constant import *


class Health_system:

    def ageing(self, entity_list, cycle):
        if cycle % CYCLE_IN_YEAR == 0:
            entity_list = [ent for ent in entity_list if hasattr(ent, "health")]
            for entity in entity_list:
                entity.health.age += 1
                if entity.health.age > entity.health.ageing_start:
                    entity.health.max_life -= entity.health.ageing_factor

    def update_health(self, entity_list):
        entity_list = [ent for ent in entity_list if hasattr(ent, "health")]
        for entity in entity_list:
            if entity.health.life < entity.health.max_life:
                entity.health.life += entity.health.regen
            if entity.health.life > entity.health.max_life:
                entity.health.life = entity.health.max_life
