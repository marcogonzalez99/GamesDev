import pygame


class UI:
    def __init__(self, surface):
        # Setup
        self.display_surface = surface

        # Health
        self.health_bar = pygame.image.load(
            '../graphics/ui/health_bar.png').convert_alpha()
        self.health_bar_topleft = (54, 39)
        self.bar_max_width = 152
        self.bar_height = 4
        # Coins
        self.coin = pygame.image.load(
            '../graphics/ui/coin.png').convert_alpha()
        self.coin_rect = self.coin.get_rect(topleft=(50, 60))
        self.font = pygame.font.Font('../graphics/ui/ARCADEPI.ttf', 32)

        # Diamonds
        self.diamond = pygame.image.load(
            '../graphics/coins/diamond.png').convert_alpha()
        self.diamond_rect = self.diamond.get_rect(topleft=(50, 75))

    def show_health(self, current, full):
        self.display_surface.blit(self.health_bar, (20, 10))
        current_health_ratio = current/full
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(
            self.health_bar_topleft, (current_bar_width, self.bar_height))
        pygame.draw.rect(self.display_surface, '#cd4949', health_bar_rect)

    def show_coins(self, amount):
        self.display_surface.blit(self.coin, self.coin_rect)
        coin_amount_surface = self.font.render(str(amount), False, ('white'))
        coin_amount_rect = coin_amount_surface.get_rect(topleft=(85, 60))
        self.display_surface.blit(coin_amount_surface, coin_amount_rect)

    def show_diamonds(self, amount):
        self.display_surface.blit(self.diamond, self.diamond_rect)
        diamond_amount_surface = self.font.render(
            str(amount), False, ('white'))
        diamond_amount_rect = diamond_amount_surface.get_rect(
            topleft=(100, 90))
        self.display_surface.blit(diamond_amount_surface, diamond_amount_rect)

    def show_score(self, amount):
        score_amount_surface = self.font.render(
            f"Score: " + str(amount), False, ('white'))
        score_amount_rect = score_amount_surface.get_rect(
            topleft=(1700, 50))
        self.display_surface.blit(score_amount_surface, score_amount_rect)
