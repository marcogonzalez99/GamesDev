import pygame
import sys
from settings import *
from overworld import Overworld
from level import Level


class Game:
    def __init__(self):
        self.max_level = 1
        self.overworld = Overworld(
            0, self.max_level, screen, self.create_level)

        self.status = 'overworld'

    def create_level(self, current_level):
        self.level = Level(current_level, screen, self.create_overworld)
        self.status = 'level'

    def create_overworld(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(
            current_level, self.max_level, screen, self.create_level)
        self.status = 'overworld'

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()


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
