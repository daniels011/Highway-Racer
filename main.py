import pygame
from highway import

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Highway Racer")

# set up variables for the display
size = (1778, 1000)
screen = pygame.display.set_mode(size)
game_name = "Highway Racer"




run = True

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((0, 0, 0))
    pygame.display.update()


pygame.quit()
