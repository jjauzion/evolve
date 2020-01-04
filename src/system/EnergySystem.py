from src.constant import *
from src import module_fct


class EnergySystem:

    @staticmethod
    def update_energy(entity_list):
        for entity in entity_list:
            entity.energy.level -= CELL_ENERGY_DECREASE_RATE
            if entity.energy.level > entity.energy.max:
                entity.energy.level = entity.energy.max

    @staticmethod
    def spend_energy(entity_list):
        for entity in entity_list:
            if entity.acceleration.vector[0] != 0 or entity.acceleration.vector[1] != 0:
                cost = (entity.acceleration.vector[0] ** 2 + entity.acceleration.vector[1] ** 2) * entity.physic.mass
                if entity.energy.level > cost:
                    new_velocity = module_fct.sum_vector(entity.velocity.vector, entity.acceleration.vector)
                    entity.velocity.vector = new_velocity
                    entity.energy.level -= cost
                    print(f'Cell {entity.id} lost {cost} energy')
                entity.acceleration.set_norm(0)
