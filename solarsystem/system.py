from itertools import combinations

from . import constants as c


class SolarSystem:
    def __init__(self, bodies=None):
        self.bodies = bodies or []
        self.accelerations = [
            b.force(self.bodies) / b.mass
            for b in self.bodies
        ]

    @property
    def total_energy(self):
        return self.potential_energy + self.kinetic_energy

    @property
    def potential_energy(self):
        return -c.GRAVITATIONAL_CONSTANT * sum(
            b1.mass * b2.mass / b1.distance(b2)
            for b1, b2 in combinations(self.bodies, 2)
        )

    @property
    def kinetic_energy(self):
        return sum(b.kinetic_energy for b in self.bodies)

    def __len__(self):
        return len(self.bodies)

    def do_velocity_verlet_step(self, delta_t=1e-2):
        for i, (a, body) in enumerate(zip(self.accelerations, self.bodies)):
            body.position += body.velocity * delta_t + a * delta_t**2

        for i, (a, body) in enumerate(zip(self.accelerations, self.bodies)):
            new_a = body.force(self.bodies) / body.mass
            body.velocity += 0.5 * (a + new_a) * delta_t
            self.accelerations[i] = new_a
