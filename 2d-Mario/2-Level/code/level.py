import pygame
from support import import_csv_layout,import_cut_graphics
from settings import tile_size
from tiles import Tile, StaticTile, Crate,AnimatedTile,Coin,Palm
from enemy import Enemy

class Level:
    def __init__(self,level_data,surface):
        # General Setup
        self.display_surface = surface
        self.world_shift = -4
        
        # Player
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle() 
        self.goal = pygame.sprite.GroupSingle()
        self.create_player(player_layout)
        # Terrain setup
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')
        # Grass Setup
        grass_layout = import_csv_layout(level_data['grass'])
        self.grass_sprites = self.create_tile_group(grass_layout,'grass')
        # Crates Setup
        crate_layout = import_csv_layout(level_data['crates'])
        self.crates_sprites = self.create_tile_group(crate_layout,'crates')
        # Coins
        coin_layout = import_csv_layout(level_data['coins'])
        self.coin_sprites = self.create_tile_group(coin_layout,'coins')
        # Foreground Palms
        fg_palms_layout = import_csv_layout(level_data['fg palms'])
        self.fg_palm_sprites = self.create_tile_group(fg_palms_layout,'fg palms')
        # Background Palms
        bg_palms_layout = import_csv_layout(level_data['bg palms'])
        self.bg_palm_sprites = self.create_tile_group(bg_palms_layout,'bg palms')
        # Enemies
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemies_sprites = self.create_tile_group(enemy_layout,'enemies')
        # Constraint
        constraint_layout = import_csv_layout(level_data['constraints'])
        self.constraint_sprites = self.create_tile_group(constraint_layout,'constraints')

        
    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()
        
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size     
                    
                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics("../graphics/terrain/terrain_tiles.png")
                        tile_surface = (terrain_tile_list[int(val)])
                        sprite = StaticTile(tile_size,x,y,tile_surface)  
                    if type == 'grass':
                        grass_tile_list = import_cut_graphics("../graphics/decoration/grass/grass.png")
                        tile_surface = grass_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)
                    if type == 'crates':
                        sprite = Crate(tile_size,x,y)
                    if type == 'coins':
                        if val == '0':
                            sprite = Coin(tile_size,x,y,'../graphics/coins/gold')
                        if val == '1':
                            sprite = Coin(tile_size,x,y,'../graphics/coins/silver')
                    if type == 'fg palms':
                        if val == '0':
                            sprite = Palm(tile_size,x,y,'../graphics/terrain/palm_small',38)
                        if val == '1':
                            sprite = Palm(tile_size,x,y,'../graphics/terrain/palm_large',70)
                    if type == 'bg palms':
                        sprite = Palm(tile_size,x,y,'../graphics/terrain/palm_bg',62)
                    if type == 'enemies':
                        sprite = Enemy(tile_size,x,y)
                    if type == 'constraints':
                        sprite = Tile(tile_size,x,y)
                    sprite_group.add(sprite)
        return sprite_group
    
    def create_player(self,layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val != '0':
                    print ("Player Goes Here")
                if val == '1':
                    hat_surface = pygame.image.load("../graphics/character/hat.png")
                    sprite = StaticTile(tile_size,x,y,hat_surface)
                    self.goal.add(sprite)
                    
    def enemy_collision_reverse(self):
        for enemy in self.enemies_sprites:
            if pygame.sprite.spritecollide(enemy,self.constraint_sprites,False):
                enemy.reverse()
                                    
    def run(self):
        # Run the whole game
        
        # BG Palms
        self.bg_palm_sprites.update(self.world_shift)
        self.bg_palm_sprites.draw(self.display_surface)
        # Terrain
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)
        # Enemy
        self.enemies_sprites.update(self.world_shift)
        self.enemies_sprites.draw(self.display_surface)
        self.constraint_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        # Crate
        self.crates_sprites.draw(self.display_surface)
        self.crates_sprites.update(self.world_shift)
        # Grass
        self.grass_sprites.draw(self.display_surface)
        self.grass_sprites.update(self.world_shift)
        # Coins
        self.coin_sprites.update(self.world_shift)
        self.coin_sprites.draw(self.display_surface)
        # FG Palms
        self.fg_palm_sprites.update(self.world_shift)
        self.fg_palm_sprites.draw(self.display_surface)
        # Player Goal
        self.player.update(self.world_shift)
        self.player.draw(self.display_surface)
        
        
        