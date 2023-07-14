import pygame
from settings import *
from random import choice

class Player(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        
        # Setup
        self.image = pygame.Surface((WINDOW_WIDTH // 10, WINDOW_HEIGHT // 20))
        self.image.fill('red')
        
        # Position
        self.rect = self.image.get_rect(midbottom = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 20))
        self.direction = pygame.math.Vector2()
        self.speed = 300
        self.pos = pygame.math.Vector2(self.rect.topleft)
        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
            
    def screen_constraint(self):
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
            self.pos.x = self.rect.x
        elif self.rect.left < 0:
            self.rect.left = 0      
            self.pos.x = self.rect.x  
            
    def update(self, dt):
        self.input()
        
        # Checks for screen constraint
        self.screen_constraint()
        
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        
class Ball(pygame.sprite.Sprite):
    def __init__(self,groups, player):
        super().__init__(groups)
        
        # Collision Objects
        self.player = player
        
        # Graphics Setup
        self.image = pygame.image.load('../graphics/other/ball.png')
        
        # Position Setup
        self.rect = self.image.get_rect(midbottom = player.rect.midtop)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(choice((1,-1)),-1)
        self.speed = 400
        
        # Active
        self.active = False
    
    def window_collision(self,direction):
        if direction == 'horizontal':
            pass
        if direction == 'vertical':
            pass
        
    
    def collision(self):
        pass
        
    
    def update(self,dt):
        if self.active:
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()
            
            self.pos.x += self.direction.x * self.speed * dt
            self.rect.x = round(self.pos.x)
            self.window_collision('horizontal')
            
            self.pos.y += self.direction.y * self.speed * dt
            self.rect.y = round(self.pos.y)
            self.window_collision('vertical')
        else:
            self.rect.midbottom = self.player.rect.midtop
            self.pos = pygame.math.Vector2(self.rect.topleft)
        