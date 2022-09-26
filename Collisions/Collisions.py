from turtle import speed
import pygame, sys

def bouncing_rect():
    global x_speed,y_speed,other_speed
    moving_rect.x += x_speed
    moving_rect.y += y_speed
    
    #Collision with Screen Borders
    if moving_rect.right >= screen_width or moving_rect.left <= 0:
        x_speed *= -1
    if moving_rect.bottom >= screen_height or moving_rect.top <= 0:
        y_speed *= -1
    #Moving the other rect
    other_rect.y += other_speed
    if other_rect.top <= 0 or other_rect.bottom >= screen_height:
        other_speed *= -1
        
    # Collision with other Rect
    collision_tolerance = 10
    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) < collision_tolerance and y_speed > 0:
            y_speed *= -1
        if abs(other_rect.bottom - moving_rect.top) < collision_tolerance and y_speed < 0:
            y_speed *= -1
        if abs(other_rect.right - moving_rect.left) < collision_tolerance and x_speed < 0:
            x_speed *= -1
        if abs(other_rect.left - moving_rect.right) < collision_tolerance and x_speed > 0:
            x_speed *= -1 
    pygame.draw.rect(screen,(255,255,255),moving_rect)   
    pygame.draw.rect(screen,(255,0,0),other_rect)

pygame.init()
clock = pygame.time.Clock()

#Dimensions
screen_width,screen_height = 700,700
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption(("Collisions"))

moving_rect = pygame.Rect(350,350,75,75)
x_speed, y_speed = 5,4

other_rect = pygame.Rect(300,500,175,75)
other_speed = 2

# Game Loop
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
    
    screen.fill((30,30,30))
    bouncing_rect()
    pygame.display.flip()
    clock.tick(60)