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
h = Highway(0, 0, highway_number)


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
    time_elapsed = time.time() - start_time
    if highway_number == 5:
        highway_number = 1
        print("hi")
    if frame % 1 == 0:
        h = Highway(0, 0, highway_number)
        highway_number += 1
        print(highway_number)



    screen.fill((0, 0, 0))
    screen.blit(h.highway_image, h.rect)
    pygame.display.update()

    frame += 1

pygame.quit()
