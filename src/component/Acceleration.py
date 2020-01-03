import math


class Acceleration:

    def __init__(self, vector):
        """
        Cartesian coordinate of the acceleration vector
        :param vector:      [tuple of int OR None] (x, y) coordinate of the acceleration vector.
        """
        self._set_vector(vector)

    def _set_vector(self, vector):
        self._vector = [vector[0], vector[1]]

    def _get_vector(self):
        return tuple(self._vector)

    vector = property(_get_vector, _set_vector)
