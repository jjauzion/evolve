import pygame

from src import module_fct

class Move:

    def move_entity(self, entity_list):
        move_list = [ent for ent in entity_list if hasattr(ent, "velocity") and hasattr(ent, "position")]
        for entity in move_list:
            entity.position.x += entity.velocity.vector[0]
            entity.position.y += entity.velocity.vector[1]
