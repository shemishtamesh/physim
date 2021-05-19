from vpython import *


# for electrons
ELECTRON_CHARGE = 1.60217662e-19
ELECTRON_MASS = 9.10938356e-31


# for proton
PROTON_CHARGE = -1.602176634e-19
# PROTON_MASS = 1.6726219e-27
PROTON_MASS = 9999999999


# constants
k = 8.9875517923e9
EPSILON0 = 8.8541878128e-12
# mu0 = 1.25663706212e-6
mu0 = 1.25663706212e20


max_speed = 9e1


dt = 1e-3


def distance(pos1, pos2):
    return sqrt((pos1.x-pos2.x)**2+(pos1.y-pos2.y)**2+(pos1.z-pos2.z)**2)


def electric_force(p1, p2):
    """force on p1 from p2"""
    q1 = p1.charge
    q2 = p2.charge
    pos_diff = p1.pos - p2.pos

    if ((4 * pi * EPSILON0) * (mag(pos_diff) ** 3)) != 0:
        return (q1 * q2 * pos_diff) / ((4*pi*EPSILON0) * (mag(pos_diff) ** 3))
    else:
        return vector(0, 0, 0)

def magnetic_force(p1, p2):
    """force on p1 from p2"""
    q1 = p1.charge
    q2 = p2.charge
    v1 = p1.velocity
    v2 = p2.velocity
    pos_diff = p1.sphere.pos - p2.sphere.pos

    return (mu0/(4*pi)) * (q1 * q2 / (mag(pos_diff)**2)) * cross(v1, cross(v2, norm(pos_diff)))


def default_value(string):
    if string == '':
        return 0
    else:
        return float(string)  # we catch the potentioal error when calling this function


def default_value_mass(string):
    if string == '':
        return 1
    else:
        return float(string)  # we catch the potentioal error when calling this function
