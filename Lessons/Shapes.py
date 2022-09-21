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

#Game Rectanbgles
ball = pygame.Rect(screen_width/2 - 15,screen_height/2-15,30,30) #This places the ball in the middle of the screen
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 120) #This will place the Player Paddle on the right side of the screen
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 120) #This will place the Opponent Paddle on the the left side of the screen

#Colors
light_grey = (200,200,200)
bg_color = pygame.Color('grey12')

# Game Loop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
            
    screen.fill(bg_color)        
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))
    
    
    pygame.display.flip()
    clock.tick(60)