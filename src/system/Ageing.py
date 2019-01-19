from src.constant import *


class Ageing:

    def ageing(self, entity_list, cycle):
        if cycle % CYCLE_IN_YEAR == 0:
            entity_list = [ent for ent in entity_list if "health" in ent.component]
            for entity in entity_list:
                entity.component["health"].age += 1
                if entity.component["health"].age > AGEING_START:
                    entity.component["health"].life -= AGEING_FACTOR
