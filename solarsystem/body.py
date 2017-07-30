import numpy as np
from scipy.spatial.distance import euclidean


class Body:

    def __init__(self, position, velocity, mass):
        self._position = np.asanyarray(position, dtype='float64')
        self._velocity = np.asanyarray(velocity, dtype='float64')
        self.mass = mass
        self.system = None

    def distance(self, other):
        return euclidean(self.position, other.position)

    @property
    def kinetic_energy(self):
        return 0.5 * self.mass * np.linalg.norm(self.velocity)**2

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = np.asanyarray(value, dtype='float64')

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = np.asanyarray(value, dtype='float64')
