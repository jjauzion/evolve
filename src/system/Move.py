class Move:

    def move_entity(self, entity):
        entity_list = entity if isinstance(entity, list) else [entity]
        entity_list = [ent for ent in entity_list if "velocity" in ent.component]
        for entity in entity_list:
            entity.component["position"].x += entity.component["velocity"].get_xspeed()
            entity.component["position"].y += entity.component["velocity"].get_yspeed()
