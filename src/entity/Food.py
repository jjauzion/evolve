from src import module_fct
from src import entity


class Food(entity.Cell):

    def __init__(self, cell_id, position):
        super().__init__(cell_id=cell_id,
                         position=position,
                         size=5,
                         vector=(0, 0),
                         life=100,
                         regen=0,
                         ageing_factor=100,
                         ageing_start=5,
                         energy_max=1)
        self.image, self.rect = module_fct.create_food_image(
            color=(0, 255, 0), width=self.physic.size, height=self.physic.size)
        self.rect.center = position
