import pygame,sys,time
from settings import *
from sprites import Player, Ball, Block
from surface_maker import SurfaceMaker

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
        self.block_sprites = pygame.sprite.Group()
        
        # Setup
        self.surface_maker = SurfaceMaker()
        self.player = Player(self.all_sprites, self.surface_maker)
        self.create_stage()
        self.ball = Ball(self.all_sprites, self.player, self.block_sprites)
        
        # Hearts
        self.hearts_surface = pygame.image.load('../graphics/other/heart.png').convert_alpha()
        
    def create_bg(self):
        bg_original = pygame.image.load('../graphics/other/bg.png').convert()
        scale_factor = WINDOW_HEIGHT / bg_original.get_height()
        scaled_width = bg_original.get_width() * scale_factor
        scaled_height = bg_original.get_height() * scale_factor
        scaled_bg = pygame.transform.scale(bg_original, (scaled_width,scaled_height))
        return scaled_bg
    
    def create_stage(self):
        # Cycle through all the rows and columns of the BLOCK MAP
        for row_index,row in enumerate(BLOCK_MAP):
            for col_index, col in enumerate(row):
                if col != ' ':
                    x = col_index * (BLOCK_WIDTH + GAP_SIZE) + GAP_SIZE // 2
                    y = TOP_OFFSET + row_index * (BLOCK_HEIGHT + GAP_SIZE) + GAP_SIZE // 2
                    Block(col,(x,y),[self.all_sprites, self.block_sprites], self.surface_maker)
        # Find the x and y position
        
    def display_hearts(self):
        for i in range(self.player.hearts):
            x = 2+ i * (self.hearts_surface.get_width() + 2)
            self.display_surface.blit(self.hearts_surface, (x,4))
               
    def run(self):
        last_time = time.time()
        while True:
        
            # Delta Time
            dt = time.time() - last_time
            last_time = time.time()   
            
            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.player.hearts:
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
            self.display_hearts()
                    
            # Update Window
            pygame.display.update()
            
if __name__ == '__main__':
    game = Game()
    game.run() 