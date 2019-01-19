import pygame

from src import module_fct

class Move:

    def move_entity(self, entity_list):
        move_list = [ent for ent in entity_list if "velocity" in ent.component]
        for entity in move_list:
            entity.component["position"].x += entity.component["velocity"].vector[0]
            entity.component["position"].y += entity.component["velocity"].vector[1]
            angle = entity.component["velocity"].get_heading_deg()
            entity.image, entity.rect = module_fct.rotation_image(entity.image, entity.rect, angle)
