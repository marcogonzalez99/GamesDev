import pygame
import sys


class ParticlePrinciple:
    def __init__(self):
        self.particles = []

    def emit(self):
        if self.particles:
            for particle in self.particles:
                particle[0][1] += particle[2]  # Move
                particle[1] -= 0.2  # Shrink
                pygame.draw.circle(screen, pygame.Color(
                    'White'), particle[0], int(particle[1]))  # Draw a circle

    def add_particles(self):
        pos_x = 250
        pos_y = 250
        radius = 10
        direction = -1
        particle_circle = [[pos_x, pos_y], radius, direction]
        self.particles.append(particle_circle)

    def delete_particles(self):
        pass  # Deletes particles after a certain time


# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Particle Effects")

particle1 = ParticlePrinciple()

# Particle Event
PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == PARTICLE_EVENT:
            particle1.add_particles()

    particle1.emit()
    screen.fill((30, 30, 30))
    pygame.display.flip()
    clock.tick(120)
