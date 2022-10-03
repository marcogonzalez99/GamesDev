import pygame
import sys
from settings import *
from level import Level
# General Setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2d-Mario Game")
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 5, 0))

    level.run()

    pygame.display.flip()
    clock.tick(75)
