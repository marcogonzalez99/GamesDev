import pygame
import sys

#General Setup
pygame.init()
clock = pygame.time.Clock()

screen_width,screen_height = 600,600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(("Bullets"))

# Game Loop
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
    
    screen.fill((30,30,30))   
    pygame.display.flip()
    clock.tick(60)