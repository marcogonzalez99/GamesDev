import pygame,sys,random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size) 
            pygame.draw.rect(screen,(183,111,122),block_rect)

    def move_snake(self):
        body_copy = self.body[:-1]

class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_size-1)
        self.pos = Vector2(self.x,self.y)
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)
        
#General Setup
pygame.init()
cell_size = 35
cell_number = 20
clock = pygame.time.Clock()

# Screen
screen_width,screen_height = 400,500
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption(("Snake"))

fruit = FRUIT()
snake = SNAKE()

# Game Loop
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
       
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.flip()
    clock.tick(120)