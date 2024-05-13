import pygame

class Highway:

    def __init__(self, x, y, number_highway):
        self.x = x
        self.y = y
        self.number = number_highway
        self.highway_image = pygame.image.load("highway" + str(number_highway) + ".png")
        self.image_size = self.highway_image.get_size()
        self.rect = pygame.Rect(self.x, self. y, self.image_size[0], self.image_size[1])

    #def turn(self, x, key):




