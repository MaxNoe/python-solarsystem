import numpy as np
from pytest import approx


def test_distance():
    from solarsystem import Body

    b1 = Body(
        mass=1,
        position=[3, 0, 0],
        velocity=[0, 0, 0],
    )
    b2 = Body(
        mass=1,
        position=[0, 4, 0],
        velocity=[0, 0, 0],
    )

    assert b1.distance(b1) == 0.0
    assert b1.distance(b2) == 5.0

    b1.position = [5, 2, 3]
    b2.position = [1, 0, 2]

    assert b1.distance(b2) == b2.distance(b1)
    assert b1.distance(b2) == approx(np.sqrt(21))


def test_kinetic_energy():
    from solarsystem import Body

    b = Body(
        mass=1,
        position=[3, 0, 0],
        velocity=[0, 0, 0],
    )

    assert b.kinetic_energy == 0.0

    b.velocity = [1, 0, 0]
    assert b.kinetic_energy == approx(0.5)

    b.mass = 2
    assert b.kinetic_energy == approx(1.0)

    b.velocity = [2, 2, 2]
    assert b.kinetic_energy == approx(12.0)
