from asyncore import loop
import pygame
import sys
from settings import *
from level import Level
from overworld import Overworld
from ui import UI


class Game:
    def __init__(self):
        # Game Attributes
        self.max_level = 6
        # PLayer Attributes
        self.current_health = 500
        self.max_health = 500
        self.coins = 0
        self.diamonds = 0

        # Audio
        self.overworld_music = pygame.mixer.Sound(
            '../audio/main_overworld.wav')
        self.overworld_music.set_volume(0.4)

        # Overworld Creation
        self.overworld = Overworld(
            0, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.overworld_music.play(loops=-1)
        # User interface
        self.ui = UI(screen)

    def create_level(self, current_level):
        self.level = Level(current_level, screen, self.create_overworld,
                           self.change_coins, self.change_health, self.change_diamond)
        self.status = 'level'
        self.overworld_music.stop()

    def create_overworld(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(
            current_level, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.overworld_music.play(loops=-1)

    def change_coins(self, amount):
        self.coins += amount

    def change_diamond(self, count):
        self.diamonds += count

    def extra_health(self):
        if self.coins >= 25:
            self.current_health += 20
            self.coins = 0

    def change_health(self, amount):
        self.current_health += amount

    def check_game_over(self):
        if self.current_health <= 0:
            self.current_health = 100
            self.coins = 0
            self.diamonds = 0
            self.max_level = 0
            self.overworld = Overworld(
                0, self.max_level, screen, self.create_level)
            self.status = 'overworld'
            self.level_music.stop()
            self.overworld_music.play(loops=-1)

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()
            self.extra_health()
            self.ui.show_health(self.current_health, self.max_health)
            self.ui.show_coins(self.coins)
            self.ui.show_diamonds(self.diamonds)
            self.check_game_over()


# Pygame setup
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pirates")
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('lightgrey')
    game.run()

    pygame.display.update()
    clock.tick(75)
