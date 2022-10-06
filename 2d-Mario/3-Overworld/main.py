import pygame
import sys
from settings import *
from overworld import Overworld


class Game:
    def __init__(self):
        self.max_level = 2
        self.overworld = Overworld(1, self.max_level, screen)

    def run(self):
        self.overworld.run()


# General Setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Overworld")
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(('black'))
    game.run()
    pygame.display.flip()
    clock.tick(75)
