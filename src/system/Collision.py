class Collision:

    def collision_with_list(self, cell, cell_list):
        rect_list = [ent.rect for ent in cell_list if ent is not cell]
        if cell.rect.collidelist(rect_list) != -1:
            cell.velocity.vector = (0, 0)
            return True
        return False
