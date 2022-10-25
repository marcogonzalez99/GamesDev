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
        self.max_level = 0
        # PLayer Attributes
        self.current_health = 100
        self.max_health = 100
        self.coins = 0
        self.total_coins = 0
        self.diamonds = 0
        self.score = 0
        self.lives = 5

        # Audio
        self.overworld_music = pygame.mixer.Sound(
            '../audio/main_overworld.wav')
        self.overworld_music.set_volume(0.4)

        self.game_over_music = pygame.mixer.Sound('../audio/game_over.wav')
        self.game_over_music.set_volume(1)

        self.main_menu_music = pygame.mixer.Sound('../audio/main.wav')
        self.main_menu_music.set_volume(0.7)

        # Overworld Creation
        self.overworld = Overworld(
            0, self.max_level, screen, self.create_level)
        self.status = 'main-menu'
        self.main_menu_music.play(loops=-1)
        # User interface
        self.ui = UI(screen, self.lives)
        # Game Over Stuff
        self.game_font = pygame.font.Font('../graphics/Pixeltype.ttf', 45)

    def create_level(self, current_level):
        self.overworld_music.stop()
        self.level = Level(current_level, screen, self.create_overworld,
                           self.change_coins, self.change_health, self.change_diamond, self.change_score, self.change_lives)
        self.status = 'level'

    def create_overworld(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(
            current_level, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.overworld_music.play(loops=-1)

    def change_coins(self, amount):
        self.total_coins += amount
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
        if amount > 0:
            if self.current_health <= self.max_health - 20:
                self.current_health += amount
        else:
            self.current_health += amount

    def check_game_over(self):
        if self.lives == 0:
            self.status = 'gameover'
            self.overworld_music.stop()
            self.game_over_music.play()
            self.game_over()
        elif self.lives == 0 and self.current_health <= 0:
            self.status = 'gameover'
            self.overworld_music.stop()
            self.game_over_music.play()
            self.game_over()
        elif self.current_health <= 0:
            self.level.level_music.stop()
            self.change_lives(-1)
            if self.lives == 0:
                self.status = 'gameover'
                self.overworld_music.stop()
                self.game_over_music.play()
                self.game_over()
                pass
            self.current_health = 100
            self.overworld = Overworld(
                self.max_level, self.max_level, screen, self.create_level)
            self.status = 'overworld'
            self.overworld_music.play(loops=-1)

    def restart_game(self):
        self.current_health = 100
        self.coins = 0
        self.diamonds = 0
        self.score = 0
        self.lives = 5
        if self.max_level < 6:
            self.max_level = 19
        elif 6 < self.max_level < 11:
            self.max_level = 6
        elif 12 < self.max_level <= 17:
            self.max_level = 12
        elif 18 < self.max_level:
            self.max_level = 18
        self.overworld_music.play(loops=-1)
        self.overworld = Overworld(
            self.max_level, self.max_level, screen, self.create_level)
        self.status = 'overworld'

    def check_completion(self):
        if self.max_level == 20:
            self.status = "end_game"

    def game_over(self):
        bg = pygame.image.load(
            '../graphics/overworld/menu.png').convert_alpha()
        screen.blit(bg, (0, 0))

        game_over_photo_1 = pygame.image.load(
            '../graphics/overworld/game_over_1.png').convert_alpha()

        game_over_photo_2 = pygame.image.load(
            '../graphics/overworld/game_over_2.png').convert_alpha()

        game_over_1_rect = game_over_photo_1.get_rect(
            center=(screen_width/2, screen_height/2 - 75))
        screen.blit(game_over_photo_1, game_over_1_rect)

        game_over_2_rect = game_over_photo_2.get_rect(
            center=(screen_width/2 - 13, screen_height/2 + 100))
        screen.blit(game_over_photo_2, game_over_2_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.game_over_music.stop()
            self.restart_game()

    def main_menu(self):
        bg = pygame.image.load(
            '../graphics/overworld/menu.png').convert_alpha()
        screen.blit(bg, (0, 0))

        intro_photo_1 = pygame.image.load(
            '../graphics/overworld/Intro_1.png').convert_alpha()

        intro_photo_2 = pygame.image.load(
            '../graphics/overworld/Intro_2.png').convert_alpha()

        intro_1_rect = intro_photo_1.get_rect(
            center=(screen_width/2 + 17, screen_height/2 - 75))
        screen.blit(intro_photo_1, intro_1_rect)

        intro_2_rect = intro_photo_2.get_rect(
            center=(screen_width/2 - 17, screen_height/2 + 125))
        screen.blit(intro_photo_2, intro_2_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.main_menu_music.stop()
            self.restart_game()

    def end_game(self):
        screen.fill((30, 30, 30))
        end_text = self.game_font.render("Thank You for Playing")
        end_text_rect = end_text.get_rect(
            center=(screen_width/2, screen_height/2))
        screen.blit(end_text, end_text_rect)

        score_text = self.game_font.render(f"Total Score: {self.score}")
        score_text_rect = score_text.get_rect(
            center=(screen_width/2, screen_height/2 + 50))
        screen.blit(score_text, score_text_rect)

        coin_text = self.game_font.render(
            f"Total Coins Collected: {self.total_coins}")
        coin_text_rect = coin_text.get_rect(
            center=(screen_width/2, screen_height/2 + 100))
        screen.blit(coin_text, coin_text_rect)

        self.end_text = self.game_font.render(
            f"Total Diamonds Collected: {self.diamonds}")
        self.end_text_rect = self.end_text.get_rect(
            center=(screen_width/2, screen_height/2 + 150))
        screen.blit(self.end_text, self.end_text_rect)

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        elif self.status == 'gameover':
            self.game_over()
        elif self.status == 'main-menu':
            self.main_menu()
        elif self.status == 'end_game':
            self.end_game()
        else:
            self.level.run()
            self.extra_health()
            self.check_game_over()
            self.check_completion()
            self.ui.show_health(self.current_health, self.max_health)
            self.ui.show_score(self.score)
            self.ui.display_lives(self.lives)
            self.ui.show_coins(self.coins)
            self.ui.show_diamonds(self.diamonds)


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
    clock.tick(74)
