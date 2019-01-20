import pygame

from src import module_fct

class Move:

    def move_entity(self, entity_list):
        move_list = [ent for ent in entity_list if "velocity" in ent.component]
        for entity in move_list:
            entity.component["position"].x += entity.component["velocity"].vector[0]
            entity.component["position"].y += entity.component["velocity"].vector[1]
            """
            angle = entity.component["velocity"].get_heading_deg()
            angle = angle if angle >= 0 else 360 + angle
            print("heading = ", angle)
            entity.image, entity.rect = module_fct.rotation_image(entity.original, entity.rect, angle)
            """
