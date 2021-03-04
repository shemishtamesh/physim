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


class Particle:
    def __init__(self, position, velocity, acceleration, charge, mass, color, radius=0.1):
        self.velocity = velocity
        self.charge = charge
        self.acceleration = acceleration
        self.mass = mass
        self.color = color
        self.radius = radius

        self.sphere = self.draw(position)

    def draw(self, position):
        return sphere(pos=position, color=self.color, radius=self.radius)

    def update(self, force):
        self.acceleration = force * (1/self.mass)
        self.velocity += self.acceleration * dt
        self.sphere.pos += self.velocity * dt


class Electron(Particle):
    def __init__(self, position, velocity=vector(0, 0, 0), acceleration=vector(0, 0, 0)):
        super(Electron, self).__init__(position, velocity, acceleration, ELECTRON_CHARGE, ELECTRON_MASS, color.blue)


class Proton(Particle):
    def __init__(self, position, velocity=vector(0, 0, 0), acceleration=vector(0, 0, 0)):
        super(Proton, self).__init__(position, velocity, acceleration, PROTON_CHARGE, PROTON_MASS, color.red)


def main():
    e1 = Electron(vector(-1, 0, 0))
    e2 = Electron(vector(1, 0, 0))
    p1 = Proton(vector(0, sin(pi/3), 0))
    sys = System([e1, e2, p1])
    while True:
        rate(60)
        # input()
        for p in sys.particles:
            print(p.sphere.pos)
        sys.update()


if __name__ == "__main__":
    main()
