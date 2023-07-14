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
        image = pygame.Surface(size)
        image.fill('red')
        return image