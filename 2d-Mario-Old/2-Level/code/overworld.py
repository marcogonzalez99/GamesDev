import pygame
from game_data import levels
from support import import_folder
from decoration import Sky
from settings import *


class Node(pygame.sprite.Sprite):
    def __init__(self, pos, status, icon_speed, path):
        super().__init__()
        # Animation for Levels
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        # Creating the image
        if status == 'available':
            self.status = 'available'
        else:
            self.status = 'locked'
        self.rect = self.image.get_rect(center=pos)

        self.detection_zone = pygame.Rect(
            self.rect.centerx - (icon_speed/2), self.rect.centery - (icon_speed/2), icon_speed, icon_speed)

    def animate(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        if self.status == 'available':
            self.animate()
        else:
            tint_surface = self.image.copy()
            tint_surface.fill('black', None, pygame.BLEND_RGB_MULT)
            self.image.blit(tint_surface, (0, 0))


class Icon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = pygame.image.load(
            '../graphics/overworld/hat.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.rect.center = self.pos


class Overworld():
    def __init__(self, start_level, max_level, surface, create_level):
        # Setup
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level
        self.create_level = create_level
        # Movement Logic
        self.moving = False
        self.move_direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        # Sky Setup
        if self.max_level < 6:
            self.sky = Sky(8, 0, 'overworld')
        elif 6 <= self.max_level < 11:
            self.sky = Sky(8, 1, 'overworld')
        elif 12 <= self.max_level < 17:
            self.sky = Sky(8, 2, 'overworld')
        else:
            self.sky = Sky(8, 2, 'overworld')
        # Sprites
        self.setup_stages()
        self.setup_icon()

        # Time
        self.start_time = pygame.time.get_ticks()
        self.allow_input = False
        self.time_length = 400
        # World Images
        self.world_1 = pygame.image.load(
            "../graphics/overworld/World_1.png").convert_alpha()
        self.world_1_rect = self.world_1.get_rect(
            center=(200, 225))

        self.world_2 = pygame.image.load(
            "../graphics/overworld/World_2.png").convert_alpha()
        self.world_2_rect = self.world_2.get_rect(
            center=(1700, 525))

        self.world_3 = pygame.image.load(
            "../graphics/overworld/World_3.png").convert_alpha()
        self.world_3_rect = self.world_3.get_rect(
            center=(200, 830))

        self.world_4 = pygame.image.load(
            "../graphics/overworld/World_4.png").convert_alpha()
        self.world_4_rect = self.world_4.get_rect(
            center=(1550, 925))

    def setup_stages(self):
        self.nodes = pygame.sprite.Group()
        for index, node_data in enumerate(levels.values()):
            if index <= self.max_level:
                node_sprite = Node(
                    node_data['node_pos'], 'available', self.speed + 2, node_data['graphics'])
            else:
                node_sprite = Node(
                    node_data['node_pos'], 'locked', self.speed + 2, node_data['graphics'])

            self.nodes.add(node_sprite)

    def setup_icon(self):
        self.icon = pygame.sprite.GroupSingle()
        icon_sprite = Icon(self.nodes.sprites()
                           [self.current_level].rect.center)
        self.icon.add(icon_sprite)

    def draw_paths(self):
        if self.max_level > 0:
            points = [node['node_pos'] for index, node in enumerate(
                levels.values()) if index <= self.max_level]

            pygame.draw.lines(self.display_surface,
                              '#a04f45', False, points, 6)

    def draw_worlds(self):
        self.display_surface.blit(self.world_1, self.world_1_rect)
        self.display_surface.blit(self.world_2, self.world_2_rect)
        self.display_surface.blit(self.world_3, self.world_3_rect)
        self.display_surface.blit(self.world_4, self.world_4_rect)

    def input(self):
        keys = pygame.key.get_pressed()
        if not self.moving and self.allow_input:
            if keys[pygame.K_d] and self.current_level < self.max_level:
                self.move_direction = self.get_movement_data('next')
                self.current_level += 1
                self.moving = True
            elif keys[pygame.K_a] and self.current_level > 0:
                self.move_direction = self.get_movement_data('previous')
                self.current_level -= 1
                self.moving = True
            elif keys[pygame.K_SPACE]:
                self.create_level(self.current_level)

    def get_movement_data(self, target):
        start = pygame.math.Vector2(
            self.nodes.sprites()[self.current_level].rect.center)
        if target == 'next':
            end = pygame.math.Vector2(
                self.nodes.sprites()[self.current_level + 1].rect.center)
        else:
            end = pygame.math.Vector2(
                self.nodes.sprites()[self.current_level - 1].rect.center)

        return (end - start).normalize()

    def update_icon_pos(self):
        if self.moving and self.move_direction:
            self.icon.sprite.pos += self.move_direction * self.speed
            target_node = self.nodes.sprites()[self.current_level]
            if target_node.detection_zone.collidepoint(self.icon.sprite.pos):
                self.moving = False
                self.move_direction = pygame.math.Vector2(0, 0)

    def input_timer(self):
        if not self.allow_input:
            current_time = pygame.time.get_ticks()
            if current_time - self.start_time >= self.time_length:
                self.allow_input = True

    def run(self):
        self.input()
        self.input_timer()
        self.update_icon_pos()
        self.icon.update()
        self.nodes.update()
        self.sky.draw(self.display_surface)

        self.draw_paths()
        self.draw_worlds()
        self.nodes.draw(self.display_surface)
        self.icon.draw(self.display_surface)