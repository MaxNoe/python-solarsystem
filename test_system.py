from pytest import approx


def test_len():
    from solarsystem import SolarSystem, Body

    s = SolarSystem(bodies=[
        Body(mass=1, position=[0, 0, 0], velocity=[0, 0, 0]),
        Body(mass=2, position=[1, 1, 0], velocity=[2, 1, 0]),
    ])

    assert len(s) == 2


def test_kinetic_energy():
    from solarsystem import SolarSystem, Body

    s = SolarSystem(bodies=[
        Body(mass=1, position=[0, 0, 0], velocity=[1, -1, 0]),
        Body(mass=2, position=[1, 1, 0], velocity=[2, 1, 0]),
    ])

    assert s.kinetic_energy == approx(6.0)


def test_potential_energy():
    from solarsystem import SolarSystem, Body

    s = SolarSystem(gravitational_constant=1.0, bodies=[
        Body(mass=1, position=[0, 0, 0], velocity=[1, -1, 0]),
        Body(mass=2, position=[3, 4, 0], velocity=[2, 1, 0]),
    ])

    assert s.potential_energy == approx(-10.0)
