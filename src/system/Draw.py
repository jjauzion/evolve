class Draw:

    def draw(self, entity, screen):
        entity_list = entity if isinstance(entity, list) else [entity]
        entity_list = [ent for ent in entity_list if "visible" in ent.component]
        for entity in entity_list:
            color = (0, 0, 0)
            position = entity.component["position"].get_position()
            radius = entity.component["visible"].size
            entity.component["visible"].draw(screen, color, position, radius, radius)
