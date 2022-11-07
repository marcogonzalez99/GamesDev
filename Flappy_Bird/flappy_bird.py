import pygame
import sys
import random

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,900))
    screen.blit(floor_surface,(floor_x_pos + 576,900))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos - 300))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface,pipe)
        else:
            flipped_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flipped_pipe,pipe)
    

#General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Variables
gravity = 0.25
bird_movement = 0

screen_width,screen_height = 576,1024
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(("Flappy Bird"))

# Background Surface
bg_surface = pygame.image.load('images/background-day.png').convert_alpha()
bg_surface = pygame.transform.scale2x(bg_surface)

# Floor Surface
floor_surface = pygame.image.load('images/base.png').convert_alpha()
floor_surface = pygame.transform.scale2x(floor_surface)

floor_x_pos = 0

# Birds
bird_surface = pygame.image.load('images/bluebird-midflap.png').convert_alpha()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,512))

# Pipes
pipe_surface = pygame.image.load('images/pipe-red.png').convert_alpha()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list= []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,2400)
pipe_height = [400,600,800]

# Game Loop
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
    
    screen.blit(bg_surface,(0,0))  
    # Bird 
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface,bird_rect)
    
    # Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)
    
    # Floor
    floor_x_pos -= 2
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0
    pygame.display.flip()
    clock.tick(60)