import numpy as np
from scipy.spatial.distance import euclidean
from .constants import GRAVITATIONAL_CONSTANT


class Body:

    def __init__(self, position, velocity, mass):
        self._position = np.asanyarray(position, dtype='float64')
        self._velocity = np.asanyarray(velocity, dtype='float64')
        self.mass = mass
        self.system = None

    def distance(self, other):
        return euclidean(self.position, other.position)

    def force(self, other):
        '''The gravitational force other inflicts on this Body'''
        return - (
            GRAVITATIONAL_CONSTANT
            * self.mass * other.mass
            * (self.position - other.position) / self.distance(other)**3
        )

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
