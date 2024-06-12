import pygame
from highway import Highway
from interior import Interior
from banana import Banana

pygame.init()
pygame.font.init()
welcome_font = pygame.font.SysFont('montserrat', 150)
pygame.display.set_caption("Highway Racer")


size = (1778, 1000)
screen = pygame.display.set_mode(size)
game_name = "Highway Racer"
highway_number = 1
h = Highway(-20, 0, highway_number)
h.rescale_image()
i = Interior(-50, 100)
i.rescale_image()
b = Banana(1000, 700)
b.rescale_image()
start1 = True
frame = 0
run = True
clock = pygame.time.Clock()
s_image = pygame.image.load("startimage.jpg")
s_image_size = s_image.get_size()
scale_size = (s_image_size[0] * 3, s_image_size[1] * 2.5)
s_image = pygame.transform.scale(s_image, scale_size)
game_end = False


while run:
    clock.tick(60)  #60 fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #turning
    if keys[pygame.K_d]:
        h.turn("right")
        if (h.x < 30) and (h.x > -270):
            b.turn("right")

    if keys[pygame.K_a]:
        h.turn("left")
        b.turn("left")

    if b.y >= 770:
        if b.x >= 250 and b.x <= 1400:
            game_end = True
        b = Banana(1000, 700)

    if keys[pygame.K_SPACE]:
        start1 = False

    if highway_number == 5:
        highway_number = 1

    if frame % 1 == 0:
        h.rescale_image()
        h = Highway(h.x, 0, highway_number)
        highway_number += 1

    if frame % 5 == 0 and b.image_size[0] < 800:
        b.move_banana()
        screen.blit(b.banana_image, b.rect)

    if start1:
        welcome = welcome_font.render("Welcome To Highway Racer!", True, (255, 255, 255))
        welcome2 = welcome_font.render("Avoid The Bananas By Turning!", True, (255, 255, 255))
        screen.blit(s_image, (0, 0))
        screen.blit(welcome, (180, 500))
        screen.blit(welcome2, (170, 650))
    elif game_end:
        game_end_text1 = welcome_font.render("Game Over!", True, (255, 255, 255))
        game_end_text2 = welcome_font.render("Avoid The Bananas Next Time!", True, (255, 255, 255))
        screen.blit(s_image, (0, 0))
        screen.blit(game_end_text1, (600, 500))
        screen.blit(game_end_text2, (180, 650))
    else:
        screen.fill((0, 0, 0))
        screen.blit(h.highway_image, h.rect)
        screen.blit(b.banana_image, b.rect)
        screen.blit(i.interior_image, i.rect)

    pygame.display.update()

    frame += 1

pygame.quit()
