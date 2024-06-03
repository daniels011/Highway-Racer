import pygame

class Banana:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.banana_image = pygame.image.load("banana.png")
        self.image_size = self.banana_image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def rescale_image(self):
        self.image_size = self.banana_image.get_size()
        scale_size = (self.image_size[0] * .01, self.image_size[1] * .01)
        self.banana_image = pygame.transform.scale(self.banana_image, scale_size)

    def move_banana(self):
        if self.y < 1000:
            self.x -= 1
            self.y += 1
            self.image_size = (self.image_size[0] + 2, self.image_size[1] + 2)
        scale_size = (self.image_size[0], self.image_size[1])
        self.banana_image = pygame.transform.scale(self.banana_image, scale_size)
        self.image_size = self.banana_image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        print(self.x)
        print(self.y)

