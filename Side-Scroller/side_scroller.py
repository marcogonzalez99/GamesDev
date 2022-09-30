import pygame
import sys


def display_score():
    current_time = int((pygame.time.get_ticks() - start_time)/100)
    score_surface = test_font.render(
        f'Score:{current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return current_time


# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2D Side-Scroller")
game_active = False
start_time = 0
score = 0

test_font = pygame.font.Font("Pixeltype.ttf", 50)

# Surfaces
sky_surface = pygame.image.load("sky.png").convert_alpha()
ground_surface = pygame.image.load("ground.png").convert_alpha()

# score_surface = test_font.render("My Game", False, (64, 64, 64))
# score_rect = score_surface.get_rect(center=(400, 50))

go_surface = test_font.render("Game Over", False, (64, 64, 64))
go_rect = go_surface.get_rect(center=(400, 50))

# Snail Image
snail_surface = pygame.image.load("snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600, 300))

#Fly Image
fly_surface = pygame.image.load("Fly1.png").convert_alpha()
fly_rect = fly_surface.get_rect(bottomright = (600,200))

player_surface = pygame.image.load("player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

# Game Over/Intro Screen
player_stand = pygame.image.load('player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Pixel Runners', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press Space to Start', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 320))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks())
                game_active = True

    if game_active:
        screen.blit(sky_surface, (0, 0))  # Drawing the sky
        screen.blit(ground_surface, (0, 300))  # Drawing the ground

        # Drawing the score
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect,
        #                  10)  # Drawing the score
        # screen.blit(score_surface, score_rect)
        score = display_score()

        snail_rect.x -= 5
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)
        
        fly_rect.x -=5
        if fly_rect.right <= 0:
            fly_rect.left = 800
        screen.blit(fly_surface,fly_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        if snail_rect.colliderect(player_rect):
            game_active = False
        if fly_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        score_message = test_font.render(
            f"Your Score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))
        if score != 0:
            screen.blit(score_message, score_message_rect)
        else:
            screen.blit(game_message, game_message_rect)

        screen.blit(game_name, game_name_rect)
        # Drawing the score
        # pygame.draw.rect(screen, '#c0e8ec', go_rect)
        # screen.blit(go_surface, go_rect)

    pygame.display.update()
    clock.tick(60)
