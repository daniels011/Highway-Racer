import pygame
import time
from highway import Highway
from interior import Interior
from banana import Banana

pygame.init()
pygame.font.init()
welcome_font = pygame.font.SysFont('montserrat', 150)
pygame.display.set_caption("Highway Racer")

# set up variables for the display
size = (1778, 1000)
screen = pygame.display.set_mode(size)
game_name = "Highway Racer"
start_time = time.time()
highway_number = 1
h = Highway(-20, 0, highway_number)
h.rescale_image()
i = Interior(-50, 50)
i.rescale_image()
b = Banana(900, 600, .1)
b.rescale_image()
speed = 30 #mph
start1 = True
frame = 0
run = True
clock = pygame.time.Clock()
s_image = pygame.image.load("startimage.jpg")


# -------- Main Program Loop -----------
while run:
    clock.tick(60)  #240 fps
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



    #accelarating
    if keys[pygame.K_w]:
        speed += 5
    if keys[pygame.K_s]:
        speed -= 5
    if keys[pygame.K_SPACE]:
        start1 = False
    speed_change_divisor = speed / 5

    time_elapsed = time.time() - start_time
    if highway_number == 5:
        highway_number = 1
    if frame % 1 == 0:
        h.rescale_image()
        h = Highway(h.x, 0, highway_number)
        highway_number += 1

    h.rescale_image()
    if frame % 5 == 0:
        print(b.x)
        b.x -= 5
        b.rescale_image()
        b.y += 1
    if start1:
        welcome = welcome_font.render("Welcome To Highway Racer!", True, (255, 255, 255))
        screen.blit(welcome, (180, 500))
        screen.blit(s_image, (0, 0))
    else:
        screen.fill((0, 0, 0))
        screen.blit(h.highway_image, h.rect)
        screen.blit(i.interior_image, i.rect)
        screen.blit(b.banana_image, b.rect)

    pygame.display.update()

    frame += 1

pygame.quit()
