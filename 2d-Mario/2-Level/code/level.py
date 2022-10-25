import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size, screen_height, screen_width
from tiles import Tile, StaticTile, Crate, AnimatedTile, Coin, Palm, Diamond
from enemy import Enemy
from decoration import Sky, Water, Clouds
from player import Player
from particles import ParticleEffect
from game_data import levels


class Level:
    def __init__(self, current_level, surface, create_overworld, change_coins, change_health, change_diamond, change_score, change_lives):
        # General Setup
        self.display_surface = surface
        self.world_shift = 0
        self.current_x = None

        # Overworld Connection
        self.create_overworld = create_overworld
        self.current_level = current_level
        level_data = levels[self.current_level]
        self.new_max_level = level_data['unlock']
        # Player
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.create_player(player_layout, change_health)

        # User Interface
        self.change_coins = change_coins
        self.change_diamond = change_diamond
        self.change_score = change_score
        self.change_lives = change_lives
        self.change_health = change_health
        # Dust
        self.dust_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False
        # Explosion Particle
        self.explosion_sprite = pygame.sprite.Group()

        # Sound Effects
        self.coin_sound = pygame.mixer.Sound('../audio/effects/coin.wav')
        self.coin_sound.set_volume(0.1)
        self.stomp_sound = pygame.mixer.Sound('../audio/effects/stomp.wav')
        self.stomp_sound.set_volume(0.3)
        
        # Death Timer
        self.death_timer = 0
        
        # Win Timer
        self.win_timer = 0

        # Music - Initialized from Game_Data
        self.level_music = pygame.mixer.Sound(level_data['music'])
        self.level_music.play(loops=-1)
        self.level_music.set_volume(0.5)

        # Terrain setup for World 1
        if 0 <= self.current_level <= 5:
            terrain_layout = import_csv_layout(level_data['terrain'])
            self.terrain_sprites = self.create_tile_group(
                terrain_layout, 'terrain')
        # Terrtain setup for World 2
        elif 6 <= self.current_level <= 11:
            terrain_layout = import_csv_layout(level_data['sand_terrain'])
            self.terrain_sprites = self.create_tile_group(
                terrain_layout, 'sand_terrain')
        # Terrain setup for World 3
        elif 12 <= self.current_level <= 17:
            terrain_layout = import_csv_layout(level_data['soft_terrain'])
            self.terrain_sprites = self.create_tile_group(
                terrain_layout, 'soft_terrain')
        # Terrain setup for World x
        if 17 < self.current_level < 20:
            terrain_layout = import_csv_layout(level_data['terrain'])
            self.terrain_sprites = self.create_tile_group(
                terrain_layout, 'terrain')
            
        # Grass Setup
        grass_layout = import_csv_layout(level_data['grass'])
        self.grass_sprites = self.create_tile_group(grass_layout, 'grass')

        # Crates Setup
        crate_layout = import_csv_layout(level_data['crates'])
        self.crates_sprites = self.create_tile_group(crate_layout, 'crates')

        # Coins
        coin_layout = import_csv_layout(level_data['coins'])
        self.coin_sprites = self.create_tile_group(coin_layout, 'coins')

        # Diamonds
        diamond_layout = import_csv_layout(level_data['diamond'])
        self.diamond_sprites = self.create_tile_group(
            diamond_layout, 'diamond')

        # Foreground Palms
        fg_palms_layout = import_csv_layout(level_data['fg palms'])
        self.fg_palm_sprites = self.create_tile_group(
            fg_palms_layout, 'fg palms')

        # Background Palms
        bg_palms_layout = import_csv_layout(level_data['bg palms'])
        self.bg_palm_sprites = self.create_tile_group(
            bg_palms_layout, 'bg palms')

        # Enemies
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemies_sprites = self.create_tile_group(enemy_layout, 'enemies')

        # Constraint
        constraint_layout = import_csv_layout(level_data['constraints'])
        self.constraint_sprites = self.create_tile_group(
            constraint_layout, 'constraints')

        # Decorations
        level_width = len(terrain_layout[0]) * tile_size
        self.water = Water(screen_height - 40, level_width)
        self.clouds = Clouds(400, level_width, 20)

        # Different Skies
        if self.current_level < 6:
            self.sky = Sky(8, 0)
        elif 6 <= self.current_level <= 11:
            self.sky = Sky(8, 1)
        elif 12 <= self.current_level <= 17:
            self.sky = Sky(8, 2)
        else:
            self.sky = Sky(8, 3)

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics(
                            "../graphics/terrain/terrain_tiles.png")
                        tile_surface = (terrain_tile_list[int(val)])
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                    if type == 'sand_terrain':
                        terrain_tile_list = import_cut_graphics(
                            "../graphics/terrain/rock_sand_tiles.png")
                        tile_surface = (terrain_tile_list[int(val)])
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                    if type == 'soft_terrain':
                        terrain_tile_list = import_cut_graphics(
                            "../graphics/terrain/soft_sand_tiles.png")
                        tile_surface = (terrain_tile_list[int(val)])
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                    if type == 'grass':
                        grass_tile_list = import_cut_graphics(
                            "../graphics/decoration/grass/grass.png")
                        tile_surface = grass_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                    if type == 'crates':
                        sprite = Crate(tile_size, x, y)
                    if type == 'coins':
                        if val == '0':
                            sprite = Coin(tile_size, x, y,
                                          '../graphics/coins/gold', 5)
                        if val == '1':
                            sprite = Coin(tile_size, x, y,
                                          '../graphics/coins/silver', 1)
                    if type == 'diamond':
                        if val == '0':
                            sprite = Diamond(
                                tile_size, x, y, '../graphics/coins/diamond', 1)
                    if type == 'fg palms':
                        if val == '0':
                            sprite = Palm(tile_size, x, y,
                                          '../graphics/terrain/palm_small', 38)
                        if val == '1':
                            sprite = Palm(tile_size, x, y,
                                          '../graphics/terrain/palm_large', 70)
                    if type == 'bg palms':
                        sprite = Palm(tile_size, x, y,
                                      '../graphics/terrain/palm_bg', 62)
                    if type == 'enemies':
                        sprite = Enemy(tile_size, x, y)
                    if type == 'constraints':
                        sprite = Tile(tile_size, x, y)
                    sprite_group.add(sprite)
        return sprite_group

    def create_player(self, layout, change_health):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '0':
                    sprite = Player((x, y), self.display_surface,
                                    self.create_jump_particles, change_health)
                    self.player.add(sprite)
                if val == '1':
                    hat_surface = pygame.image.load(
                        "../graphics/character/hat.png").convert_alpha()
                    sprite = StaticTile(tile_size, x, y, hat_surface)
                    self.goal.add(sprite)

    def enemy_collision_reverse(self):
        for enemy in self.enemies_sprites:
            if pygame.sprite.spritecollide(enemy, self.constraint_sprites, False):
                enemy.reverse()

    def create_jump_particles(self, pos):
        if self.player.sprite.facing_right:
            pos -= pygame.math.Vector2(10, 5)
        else:
            pos += pygame.math.Vector2(10, -5)
        jump_particle_sprite = ParticleEffect(pos, 'jump')
        self.dust_sprite.add(jump_particle_sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.collision_rect.x += player.direction.x * player.speed
        collidable_sprites = self.terrain_sprites.sprites(
        ) + self.crates_sprites.sprites() + self.fg_palm_sprites.sprites()
        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.collision_rect):
                if player.direction.x < 0:
                    player.collision_rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.collision_rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        collidable_sprites = self.terrain_sprites.sprites(
        ) + self.crates_sprites.sprites() + self.fg_palm_sprites.sprites()
        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.collision_rect):
                if player.direction.y > 0:
                    player.collision_rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.collision_rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width/3 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width/3) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def create_landing_dust(self):
        if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
            if self.player.sprite.facing_right:
                offset = pygame.math.Vector2(10, 15)
            else:
                offset = pygame.math.Vector2(-10, 15)
            fall_dust_particle = ParticleEffect(
                self.player.sprite.rect.midbottom - offset, 'land')
            self.dust_sprite.add(fall_dust_particle)

    def check_death(self):
        if self.player.sprite.rect.top > screen_height:
            self.level_music.stop()
            self.death_timer += 1
            if self.death_timer > 150:
                self.death_timer = 0
                self.change_lives(-1)
                self.create_overworld(self.current_level, 0)

    def check_win(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.goal, False):
            self.level_music.stop()
            self.win_timer += 1
            if self.win_timer > 150:
                self.change_score(10000)
                self.change_health(20)
                self.create_overworld(self.current_level, self.new_max_level)

    def check_coin_collisions(self):
        collided_coins = pygame.sprite.spritecollide(
            self.player.sprite, self.coin_sprites, True)
        if collided_coins:
            self.coin_sound.play()
            for coin in collided_coins:
                self.change_coins(coin.value)
                self.change_score(coin.value * 200)

    def check_diamond_collisions(self):
        collided_diamond = pygame.sprite.spritecollide(
            self.player.sprite, self.diamond_sprites, True)
        if collided_diamond:
            self.coin_sound.play()
            for diamond in collided_diamond:
                self.change_diamond(diamond.count)
                self.change_score(diamond.count * 5000)

    def check_enemy_collisions(self):
        enemy_collisions = pygame.sprite.spritecollide(
            self.player.sprite, self.enemies_sprites, False)
        if enemy_collisions:
            for enemy in enemy_collisions:
                enemy_center = enemy.rect.centery
                enemy_top = enemy.rect.top
                player_bottom = self.player.sprite.rect.bottom
                if enemy_top < player_bottom < enemy_center and self.player.sprite.direction.y >= 0:
                    self.player.sprite.direction.y = -20
                    explosion_sprite = ParticleEffect(
                        enemy.rect.center, 'explosion')
                    self.explosion_sprite.add(explosion_sprite)
                    self.stomp_sound.play()
                    self.change_score(1000)
                    enemy.kill()
                else:
                    self.player.sprite.get_damage()

    def run(self):
        # Run the whole game
        # Decoration
        self.sky.draw(self.display_surface)
        self.clouds.draw(self.display_surface, self.world_shift)
        # BG Palms
        self.bg_palm_sprites.update(self.world_shift)
        self.bg_palm_sprites.draw(self.display_surface)
        # Dust Particles
        self.dust_sprite.update(self.world_shift)
        self.dust_sprite.draw(self.display_surface)
        # Terrain
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)
        # Enemy
        self.enemies_sprites.update(self.world_shift)
        self.enemies_sprites.draw(self.display_surface)
        self.constraint_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        self.explosion_sprite.update(self.world_shift)
        self.explosion_sprite.draw(self.display_surface)
        # Crate
        self.crates_sprites.draw(self.display_surface)
        self.crates_sprites.update(self.world_shift)
        # Grass
        self.grass_sprites.draw(self.display_surface)
        self.grass_sprites.update(self.world_shift)
        # Coins
        self.coin_sprites.update(self.world_shift)
        self.coin_sprites.draw(self.display_surface)
        # Diamonds
        self.diamond_sprites.update(self.world_shift)
        self.diamond_sprites.draw(self.display_surface)
        # FG Palms
        self.fg_palm_sprites.update(self.world_shift)
        self.fg_palm_sprites.draw(self.display_surface)

        # Player Sprite
        self.player.update()
        self.horizontal_movement_collision()

        self.get_player_on_ground()
        self.vertical_movement_collision()
        self.create_landing_dust()

        self.player.draw(self.display_surface)
        self.scroll_x()
        # Player Goal
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)

        # Overworld Checks
        self.check_death()
        self.check_win()

        # Coins
        self.check_coin_collisions()
        self.check_diamond_collisions()
        self.check_enemy_collisions()
        # Water
        self.water.draw(self.display_surface, self.world_shift)
