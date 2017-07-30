from scipy.constants import gravitational_constant


def test_reset():
    from solarsystem import constants

    constants.GRAVITATIONAL_CONSTANT = 1.0
    assert constants.GRAVITATIONAL_CONSTANT == 1.0

    constants.reset_to_defaults()
    assert constants.GRAVITATIONAL_CONSTANT == gravitational_constant
