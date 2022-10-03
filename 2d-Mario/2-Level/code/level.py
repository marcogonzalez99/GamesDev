import pygame
from support import import_csv_layout

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')
        
    
    def run(self):
        # Run the whole game
        pass