import pygame
import sys
from game import Game

pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()
pygame.display.set_caption("Pirate's Cove")
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Hide the mouse, run the whole game
    pygame.mouse.set_visible(False)
    game.run()

    pygame.display.update()
    clock.tick(75)
