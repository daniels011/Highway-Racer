import pygame

class Banana:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.banana_image = pygame.image.load("banana.png")
        self.image_size = (self.banana_image.get_width() // 20, self.banana_image.get_height() // 20)
        self.banana_image = pygame.transform.scale(self.banana_image, self.image_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def rescale_image(self):
        self.banana_image = pygame.transform.scale(self.banana_image, self.image_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_banana(self):
        if self.y < 1000:
            self.x -= 5  # Move left
            self.y += 5  # Move down
            self.image_size = (self.image_size[0] + 10, self.image_size[1] + 10)  # Increase size
            self.rescale_image()

    def turn(self, direction):  # for turning with the highway
        if self.x <= 1650 and self.x >= 0:
            if self.x == 1650:
                if direction == "right":
                    self.x -= 100
            elif self.x == 0:
                if direction == "left":
                    self.x += 100
            else:
                if direction == "left":
                    self.x += 95
                if direction == "right":
                    self.x -= 95
        self.rect = (self.x, self.y)




