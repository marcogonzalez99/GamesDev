# Lesson 3
import pygame
import sys

#General Setup
pygame.init()
clock = pygame.time.Clock()

#Screen Sizes
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(("Pong"))

# Game Loop
while True:
    
    print("Hello Pong")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
            
    pygame.display.flip()
    clock.tick(60)