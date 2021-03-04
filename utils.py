from vpython import *


# for electrons
ELECTRON_CHARGE = 1.60217662e-19
ELECTRON_MASS = 9.10938356e-31


# for proton
PROTON_CHARGE = -1.602176634e-19
PROTON_MASS = 1.6726219e-27


# constants
k = 8.9875517923e9
EPSILON0 = 8.8541878128e-12
c = 299792458e-9

dt = 1e-3




def distance(pos1, pos2):
    return sqrt((pos1.x-pos2.x)**2+(pos1.y-pos2.y)**2+(pos1.z-pos2.z)**2)




def electric_force(p1, p2):
    """force on p1 from p2"""
    q1 = p1.charge
    q2 = p2.charge
    pos_diff = p1.sphere.pos - p2.sphere.pos

    return (q1 * q2 * pos_diff) / ((4*pi*EPSILON0) * (mag(pos_diff) ** 3))
