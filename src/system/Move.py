class Move:

    def __init__(self, screen_size):
        """
        Move entity in the universe.
        The universe is round: When one entity goes beyond the window size it appears back at the side
        of the window.
        :param screen_size:     [tuple of int]  (x, y) -> size of the window,
                                                (0, 0) is the top left corner
                                                x increases toward the right
                                                y increases toward the bottom
        """
        self.screen_size = screen_size

    def move_entity(self, entity_list):
        move_list = [ent for ent in entity_list if hasattr(ent, "velocity") and hasattr(ent, "position")]
        for entity in move_list:
            entity.position.x += entity.velocity.vector[0]
            entity.position.y += entity.velocity.vector[1]
            if entity.position.x > self.screen_size[0]:
                entity.position.x = entity.position.x % self.screen_size[0]
            elif entity.position.x < 0:
                entity.position.x = self.screen_size[0] + entity.position.x
            if entity.position.y > self.screen_size[1]:
                entity.position.y = entity.position.y % self.screen_size[1]
            elif entity.position.y < 0:
                entity.position.y = self.screen_size[1] + entity.position.y
