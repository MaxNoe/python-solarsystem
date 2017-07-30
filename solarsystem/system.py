from itertools import combinations
from . import constants as c


class SolarSystem:
    def __init__(self, bodies=None):
        self.bodies = bodies or []

    @property
    def total_energy(self):
        return self.potential_energy + self.kinetic_energy

    @property
    def potential_energy(self):
        return -sum(
            c.GRAVITATIONAL_CONSTANT * b1.mass * b2.mass * b1.distance(b2)
            for b1, b2 in combinations(self.bodies, 2)
        )

    @property
    def kinetic_energy(self):
        return sum(b.kinetic_energy for b in self.bodies)

    def __len__(self):
        return len(self.bodies)
