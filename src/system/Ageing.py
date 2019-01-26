from src.constant import *


class Ageing:

    def ageing(self, entity_list, cycle):
        if cycle % CYCLE_IN_YEAR == 0:
            entity_list = [ent for ent in entity_list if hasattr(ent, "health")]
            for entity in entity_list:
                entity.health.age += 1
                if entity.health.age > AGEING_START:
                    entity.health.life -= AGEING_FACTOR
