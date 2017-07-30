from . import constants as c
from scipy.spatial.distance import euclidean


def gravitational_force(m1, m2, pos1, pos2):
    ''' Newtons law of universal gravity in vectorial form '''
    return - (
        c.GRAVITATIONAL_CONSTANT
        * m1 * m2
        * (pos1 - pos2) / (euclidean(pos1, pos2) + c.DISTANCE_EPS)**3
    )
