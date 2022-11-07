import pygame
import sys

#General Setup
pygame.init()
clock = pygame.time.Clock()

screen_width,screen_height = 576,1024
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(("Flappy Bird"))

bg_surface = pygame.image.load('images/background-day.png').convert_alpha()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('images/base.png').convert_alpha()
floor_surface = pygame.transform.scale2x(floor_surface)

floor_x_pos = 0

# Game Loop
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
    
    screen.blit(bg_surface,(0,0))  
    floor_x_pos += 1
    screen.blit(floor_surface,(floor_x_pos,900))
    pygame.display.flip()
    clock.tick(60)