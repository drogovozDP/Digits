import pygame

class Cell:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (0, 0, 0)

    def getValue(self):
        # return self.color[0] / 255 * 0.99 + 0.01
        return self.color[0] / 255

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))