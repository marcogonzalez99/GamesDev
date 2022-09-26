import pygame
import sys

#General Setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption(("Collisions"))

# Game Loop
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
    
    screen.fill((30,30,30))   
    pygame.display.flip()
    clock.tick(60)