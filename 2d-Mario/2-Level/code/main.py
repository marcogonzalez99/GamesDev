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
        self.max_level = 19
        # PLayer Attributes
        self.current_health = 100
        self.max_health = 100
        self.coins = 99
        self.diamonds = 0
        self.score = 0
        self.lives = 5

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
        self.ui = UI(screen, self.lives)

    def create_level(self, current_level):
        self.level = Level(current_level, screen, self.create_overworld,
                           self.change_coins, self.change_health, self.change_diamond, self.change_score, self.change_lives)
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

    def change_score(self, count):
        self.score += count

    def change_lives(self, count):
        self.lives += count

    def extra_health(self):
        if self.coins >= 100:
            self.lives += 1
            self.coins = 0

    def change_health(self, amount):
        self.current_health += amount

    def check_game_over(self):
        if self.lives == 0:
            self.current_health = 100
            self.coins = 0
            self.diamonds = 0
            self.score = 0
            self.lives = 5
            self.max_level = 0
            self.overworld = Overworld(
                0, self.max_level, screen, self.create_level)
            self.status = 'overworld'
        elif self.current_health <= 0:
            self.level.level_music.stop()
            self.change_lives(-1)
            self.current_health = 100
            self.overworld = Overworld(
                0, self.max_level, screen, self.create_level)
            self.status = 'overworld'
            self.overworld_music.play(loops=-1)

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()
            self.extra_health()
            self.ui.show_health(self.current_health, self.max_health)
            self.ui.show_score(self.score)
            self.ui.display_lives(self.lives)
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
