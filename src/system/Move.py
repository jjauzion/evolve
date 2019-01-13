class Move:

    def move_entity(self, entity_list):
        move_list = [ent for _, ent in entity_list.items() if "velocity" in ent.component]
        for entity in move_list:
            entity.component["position"].x += entity.component["velocity"].vector[0]
            entity.component["position"].y += entity.component["velocity"].vector[1]
