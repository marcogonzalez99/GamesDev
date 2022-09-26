import pygame,sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Create the display surface
screen = pygame.display.set_mode((500,500))
second_surface = pygame.Surface([100,200])
second_surface.fill((0,0,205))

image = pygame.image.load("bg_wood.png")
image_rect = image.get_rect()
print(image_rect.center)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
    screen.fill((255,255,255)) 
    screen.blit(second_surface,(0,50))
    screen.blit(image,image_rect)
    image_rect.right += 5
    pygame.display.flip()
    clock.tick(60)