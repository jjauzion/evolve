import math


class Velocity:

    def __init__(self, vector):
        self._polar_vector = {"r": 0., "theta": 0.}
        self._vector = 0
        self._set_vector(vector)

    def _set_vector(self, vector):
        try:
            r = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
        except KeyError:
            raise KeyError("Velocity vector requires a tuple (x, y) to be set. Got: {}".format(vector))

        if r != 0:
            theta = math.acos(vector[0] / r) if vector[1] >= 0 else -math.acos(vector[0] / r)
        else:
            theta = 0
        self._polar_vector["r"] = r
        self._polar_vector["theta"] = theta
        self._vector = vector

    def _get_vector(self):
        return self._vector

    def _set_polar_vector(self, polar_vect):
        if "r" not in polar_vect or "theta" not in polar_vect:
            raise KeyError("Velocity polar vector requires 'r' and 'theta' keys to be set. Got: {}".format(polar_vect))
        self._vector[0] = polar_vect["r"] * math.cos(polar_vect["theta"])
        self._vector[1] = polar_vect["r"] * math.sin(polar_vect["theta"])
        self._polar_vector = polar_vect

    def _get_polar_vector(self):
        return self._polar_vector

    def get_heading_deg(self):
        return round(self._polar_vector["theta"] * 180 / math.pi)

    polar_vector = property(_get_polar_vector, _set_polar_vector)
    vector = property(_get_vector, _set_vector)
