from utils import *


class System:
    def __init__(self, particles=None):
        if particles:
            self.particles = particles
        else:
            self.particles = []

    def update(self):
        for p1 in self.particles:
            for p2 in self.particles:
                if p1 != p2:
                    p1.update(electric_force(p1, p2))


class Field:
    def __init__(self, value, position, size, direction, field_color):
        self.value = value  # size of the field at distance 1 from the the self.position
        self.position = position
        self.size = size
        self.direction = direction
        self.field_color = field_color

        self.box = box(pos=vector(0, 0, 0), axis=vector(0, 0, 0), size=vector(0, 0, 0))

    def draw(self, position):
        pass  # TODO: implement draw with small arrows


class UniformField(Field):
    pass

class Particle:
    def __init__(self, position, velocity, acceleration, charge, mass, particle_color, radius=0.1):
        self.velocity = velocity
        self.charge = charge
        self.acceleration = acceleration
        self.mass = mass
        self.particle_color = particle_color
        self.radius = radius

        self.sphere = self.draw(position)

    def draw(self, position):
        return sphere(pos=position, color=self.particle_color, radius=self.radius)

    def update(self, force):
        self.acceleration = force * (1/self.mass)
        self.velocity += self.acceleration * dt
        if mag(self.velocity) > max_speed:
            self.velocity = max_speed * norm(self.velocity)
        self.sphere.pos += self.velocity * dt


class Electron(Particle):
    def __init__(self, position, velocity=vector(0, 0, 0), acceleration=vector(0, 0, 0)):
        super(Electron, self).__init__(position, velocity, acceleration, ELECTRON_CHARGE, ELECTRON_MASS, color.blue)


class Proton(Particle):
    def __init__(self, position, velocity=vector(0, 0, 0), acceleration=vector(0, 0, 0)):
        super(Proton, self).__init__(position, velocity, acceleration, PROTON_CHARGE, PROTON_MASS, color.red)


def main():
    e1 = Electron(vector(-1, 0, 0))
    p1 = Proton(vector(0, sin(pi/3), 0))
    e2 = Electron(vector(1, 0, 0))
    sys = System([e1, p1, e2])
    while True:
        # rate(24)
        input()
        for p in sys.particles:
            print(p.sphere.pos)
        sys.update()


if __name__ == "__main__":
    main()
