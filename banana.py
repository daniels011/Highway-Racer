import pygame

class Banana:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.banana_image = pygame.image.load("banana.png")
        self.image_size = self.banana_image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def rescale_image(self, size):
        self.image_size = self.banana_image.get_size()
        scale_size = (self.image_size[0] * size, self.image_size[1] * size)
        self.banana_image = pygame.transform.scale(self.banana_image, scale_size)

