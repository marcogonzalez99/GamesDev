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
        self.coins = 0
        self.diamonds = 0
        self.score = 0
        self.lives = 1

        # Audio
        self.overworld_music = pygame.mixer.Sound(
            '../audio/main_overworld.wav')
        self.overworld_music.set_volume(0.4)
        
        self.game_over_music = pygame.mixer.Sound('../audio/game_over.wav')
        self.game_over_music.set_volume(1)
        
        self.main_menu_music = pygame.mixer.Sound('../audio/main.wav')
        self.main_menu_music.set_volume(0.5)

        # Overworld Creation
        self.overworld = Overworld(
            0, self.max_level, screen, self.create_level)
        self.status = 'main-menu'
        self.main_menu_music.play(loops=-1)
        # User interface
        self.ui = UI(screen, self.lives)
        # Game Over Stuff
        self.game_over_font = pygame.font.Font('../graphics/Pixeltype.ttf',45)
        

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
            self.current_health = 100
            self.overworld = Overworld(
                0, self.max_level, screen, self.create_level)
            self.status = 'overworld'
            self.overworld_music.play(loops=-1)
            
    def restart_game(self):
        self.current_health = 100
        self.coins = 0
        self.diamonds = 0
        self.score = 0
        self.lives = 5
        self.max_level = 0
        self.overworld_music.play(loops=-1)
        self.overworld = Overworld(
                0, self.max_level, screen, self.create_level)
        self.status = 'overworld'
    
    def game_over(self):
            bg = pygame.image.load('../graphics/overworld/menu.png').convert_alpha()
            screen.blit(bg,(0,0))
            game_over_message = self.game_over_font.render(f"Game Over, Press Space to Start Fresh",False,'black')
            game_over_message_rect = game_over_message.get_rect(center = (screen_width/2,screen_height/2))
            screen.blit(game_over_message,game_over_message_rect)
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.game_over_music.stop()
                self.restart_game()   
            
    def main_menu(self):
            bg = pygame.image.load('../graphics/overworld/menu.png').convert_alpha()
            screen.blit(bg,(0,0))
            
            main_menu_message = self.game_over_font.render(f"Pirate Journey",False,'black')
            main_menu_message_rect = main_menu_message.get_rect(center = (screen_width/2,screen_height/2))
            screen.blit(main_menu_message,main_menu_message_rect)
            
            menu_message = self.game_over_font.render(f"Press Space to Start",False,'black')
            menu_message_rect = menu_message.get_rect(center = (screen_width/2,screen_height/2 + 50))
            screen.blit(menu_message,menu_message_rect)
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.main_menu_music.stop()
                self.restart_game() 

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        elif self.status == 'gameover':
            self.game_over()
        elif self.status == 'main-menu':
            self.main_menu()
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
