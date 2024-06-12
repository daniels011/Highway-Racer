import pygame

class Highway:

    def __init__(self, x, y, number_highway):
        self.x = x
        self.y = y
        self.number = number_highway
        self.highway_image = pygame.image.load("highway" + str(number_highway) + ".png")
        self.turn_delta = 25
        self.speed_delta = .2
        self.image_size = self.highway_image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def rescale_image(self):
        self.image_size = self.highway_image.get_size()
        scale_size = (self.image_size[0] * 1.1, self.image_size[1] * 1.1)
        self.highway_image = pygame.transform.scale(self.highway_image, scale_size)

    def turn(self, direction):
        if self.x <= 230 and self.x >= -270:
            if self.x == 230:
                if direction == "right":
                    self.x -= self.turn_delta
            elif self.x == -270:
                if direction == "left":
                    self.x += self.turn_delta
            else:
                if direction == "left":
                    self.x += self.turn_delta
                if direction == "right":
                    self.x -= self.turn_delta









