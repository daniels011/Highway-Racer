import pygame

class Banana:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.banana_image = pygame.image.load("banana.png")
        self.image_size = self.banana_image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.size = size

    def rescale_image(self):
        self.image_size = self.banana_image.get_size()
        scale_size = (self.image_size[0] * self.size, self.image_size[1] * self.size)
        self.banana_image = pygame.transform.scale(self.banana_image, scale_size)

    def move_banana(self):
        self.x -= 1
        if self.y < 500:
            self.y += 1
        scale_size = (self.image_size[0] + 1, self.image_size[1] + 1)
        self.banana_image = pygame.transform.scale(self.banana_image, scale_size)
        self.image_size = self.banana_image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

