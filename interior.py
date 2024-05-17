import pygame

class Interior:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.interior_image = pygame.image.load("carinterior1.png")
        self.image_size = self.interior_image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


    def rescale_image(self):
        self.image_size = self.interior_image.get_size()
        scale_size = (self.image_size[0] * 2.5, self.image_size[1] * 2.5)
        self.interior_image = pygame.transform.scale(self.interior_image, scale_size)