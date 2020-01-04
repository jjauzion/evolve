import math


class Vector:

    def __init__(self, vector):
        self._polar_vector = {"r": 0., "theta": 0.}
        self._vector = [0, 0]
        self._set_vector(vector)

    def _set_vector(self, vector):
        try:
            r = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
        except [KeyError, TypeError]:
            raise AttributeError("Velocity vector requires a tuple of int (x, y) to be set. Got: {}".format(vector))

        if r != 0:
            theta = math.acos(vector[0] / r) if vector[1] >= 0 else -math.acos(vector[0] / r)
        else:
            theta = 0
        self._polar_vector["r"] = r
        self._polar_vector["theta"] = theta
        self._vector = [vector[0], vector[1]]

    def _get_vector(self):
        return tuple(self._vector)

    def _set_polar_vector(self, polar_vect):
        if "r" not in polar_vect or "theta" not in polar_vect:
            raise KeyError("Velocity polar vector requires 'r' and 'theta' keys to be set. Got: {}".format(polar_vect))
        if polar_vect["r"] > 2 * math.pi:
            polar_vect["r"] = polar_vect["r"] % (2 * math.pi)
        self._vector[0] = polar_vect["r"] * math.cos(polar_vect["theta"])
        self._vector[1] = polar_vect["r"] * math.sin(polar_vect["theta"])
        self._polar_vector = polar_vect

    def _get_polar_vector(self):
        return self._polar_vector

    def get_heading_deg(self):
        return self._polar_vector["theta"] * 180 / math.pi

    def get_heading_rad(self):
        return self._polar_vector["theta"]

    def get_norm(self):
        return self._polar_vector["r"]

    def set_heading(self, heading):
        """
        Change the vector direction
        :param heading:     [float] new heading value in Radian
        """
        if heading > 2 * math.pi:
            heading = heading % (2 * math.pi)
        new_vector = {
            "r": self._polar_vector["r"],
            "theta": heading
        }
        self._set_polar_vector(new_vector)

    def set_norm(self, value):
        """
        Change the vector norm value. Negative value is not possible (will be set to 0 instead).
        :param value:     [float] new norm value
        """
        new_vector = {
            "r": value if value > 0 else 0,
            "theta": self._polar_vector["theta"]
        }
        self._set_polar_vector(new_vector)

    polar_vector = property(_get_polar_vector, _set_polar_vector)
    vector = property(_get_vector, _set_vector)
