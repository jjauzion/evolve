class Draw:

    def draw(self, entity_list, screen):
        draw_list = [ent for _, ent in entity_list.items() if "visible" in ent.component]
        for entity in draw_list:
            color = (0, 0, 0)
            position = entity.component["position"].get_position()
            radius = entity.component["physic"].size
            vector = entity.component["velocity"].vector
            polar_vector = entity.component["velocity"].polar_vector
            entity.component["visible"].draw(screen, color, position, radius, radius, vector, polar_vector)
