import pygame
from highway import Highway
import time

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Highway Racer")

# set up variables for the display
size = (1778, 1000)
screen = pygame.display.set_mode(size)
game_name = "Highway Racer"
start_time = time.time()
highway_number = 1
h = Highway(-20, 0, highway_number)
h.rescale_image()


frame = 0
run = True
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while run:
    clock.tick(60)  #60 fps
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    keys = pygame.key.get_pressed()

    #turning
    if keys[pygame.K_d]:
        h.turn("right")
    if keys[pygame.K_a]:
        h.turn("left")
    print(h.x)

    time_elapsed = time.time() - start_time
    if highway_number == 5:
        highway_number = 1
    if frame % 1 == 0:
        h.rescale_image()
        h = Highway(h.x, 0, highway_number)
        highway_number += 1

    h.rescale_image()

    screen.fill((0, 0, 0))
    screen.blit(h.highway_image, h.rect)
    pygame.display.update()

    frame += 1

pygame.quit()
