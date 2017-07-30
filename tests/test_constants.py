
def test_reset():
    from solarsystem import constants

    old = constants.GRAVITATIONAL_CONSTANT
    constants.GRAVITATIONAL_CONSTANT = 1.0
    assert constants.GRAVITATIONAL_CONSTANT == 1.0

    constants.reset_to_defaults()
    assert constants.GRAVITATIONAL_CONSTANT == old

    old = constants.DISTANCE_EPS
    constants.DISTANCE_EPS = 0.0
    assert constants.DISTANCE_EPS == 0.0

    constants.reset_to_defaults()
    assert constants.DISTANCE_EPS == old
