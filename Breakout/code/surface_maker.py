import pygame
from settings import *
from os import walk

class SurfaceMaker:
    # Import all the graphics
    def __init__(self):
        for index,info in enumerate(walk('../graphics/blocks')):
            if index == 0:
                self.assets = {color: {} for color in info[1]}
            else:
                for image_name in info[2]:
                    color_type = list(self.assets.keys())[index-1]
                    full_path = '../graphics/blocks' + f'/{color_type}/' + image_name
                    surface = pygame.image.load(full_path).convert_alpha()
                    self.assets[color_type][image_name.split('.')[0]] = surface
    
    def get_surface(self,block_type,size):
        
        # Create one surface with the graphics at any size
        image = pygame.Surface(size)
        sides = self.assets[block_type]
        
        
        # 4 Corners
        image.blit(sides['topleft'],(0,0))
        image.blit(sides['topright'],(size[0] - sides['topright'].get_width(),0))
        image.blit(sides['bottomleft'],(0,size[1] - sides['bottomleft'].get_height()))
        image.blit(sides['bottomright'],(size[0] - sides['topright'].get_width(),size[1] - sides['bottomleft'].get_height()))
        
        # Top Side
        top_width = size[0] - (sides['topleft'].get_width() + sides['topright'].get_width())
        scaled_top_surface = pygame.transform.scale(sides['top'], (top_width, sides['top'].get_height()))
        image.blit(scaled_top_surface, (sides['topleft'].get_width(),0))
        
        # Left Side
        top_height = size[1] - (sides['topleft'].get_height() + sides['bottomleft'].get_height())
        scaled_top_surface = pygame.transform.scale(sides['top'], (top_width, sides['top'].get_height()))
        image.blit(scaled_top_surface, (sides['topleft'].get_width(),0))
        
        # Right Side
        
        # Bottom Side
        
        # Center Color
        
        
        
        return image