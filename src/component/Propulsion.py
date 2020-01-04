from src import component
from src import module_fct


class Propulsion(component.Vector):

    def __init__(self, vector, cell):
        super().__init__(vector)
        self.cell = cell

    def set_heading(self, heading):
        """set a new heading (rad)"""
        super().set_heading(heading)
        image, _ = module_fct.create_cell_image((255, 255, 255), (255, 0, 0), self.cell.physic.size, heading)
        self.cell.change_image(image)

    def increase_heading(self, increment):
        """Increase the heading by 'increment' value (in rad)"""
        new_heading = self.get_heading_rad() + increment
        self.set_heading(new_heading)

    def increase_norm(self, value):
        """Increase the vector norm by 'value'"""
        self.set_norm(self.get_norm() + value)
