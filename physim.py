from utils import *


class System:
    def __init__(self, particles=None, frame_rate=0):
        if particles:
            self.particles = particles
        else:
            self.particles = []

    def update(self):
        for p1 in self.particles:
            for p2 in self.particles:
                if p1 != p2:
                    p1.update(electric_force(p1, p2))
                    # p1.update(magnetic_force(p1, p2))
                elif p1 == p2:
                    p1.update(vector(0, 0, 0))

    def remove_particle(self, index):
        selected_particle = self.particles[index]
        selected_particle.visible = False
        self.particles.remove(selected_particle)

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


def update(self, force):
    self.acceleration = force * (1/self.mass)
    self.velocity += self.acceleration * dt
    if mag(self.velocity) > max_speed:  # make sure speed isn't over the limit
        self.velocity = max_speed * norm(self.velocity)  # if it is, consider only the speed's direction
    self.pos += self.velocity * dt


sphere.update = update
