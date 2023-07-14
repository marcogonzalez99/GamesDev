import pygame,sys,time
from settings import *
from sprites import Player, Ball

class Game:
    def __init__(self):
        
        # General Setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Breakout")
        
        # Background
        self.bg = self.create_bg()
        
        # Sprite Group Setup
        self.all_sprites = pygame.sprite.Group()
        
        # Setup
        self.player = Player(self.all_sprites)
        self.ball = Ball(self.all_sprites, self.player)
    
    def create_bg(self):
        bg_original = pygame.image.load('../graphics/other/bg.png').convert()
        scale_factor = WINDOW_HEIGHT / bg_original.get_height()
        scaled_width = bg_original.get_width() * scale_factor
        scaled_height = bg_original.get_height() * scale_factor
        scaled_bg = pygame.transform.scale(bg_original, (scaled_width,scaled_height))
        return scaled_bg
        
        
    def run(self):
        last_time = time.time()
        while True:
        
            # Delta Time
            dt = time.time() - last_time
            last_time = time.time()   
            
            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.active = True
                    
            # Update the game
            self.all_sprites.update(dt)        
                    
            # Draw the frame
            self.display_surface.blit(self.bg, (0,0))  
            
            # Draw all Sprites
            self.all_sprites.draw(self.display_surface) 
                    
            # Update Window
            pygame.display.update()
            
if __name__ == '__main__':
    game = Game()
    game.run() 