import pygame

class Scroll:
    def __init__(self, x, y, width, height, digit, percentText):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.digit = digit
        self.percent = .5
        self.percentText = percentText
        self.defaultColor = (255, 50, 50)
        self.fillColor = (0, 255, 70)

    def draw(self, screen):
        x, y, w, h = self.x, self.y, self.width, self.height
        pygame.draw.rect(screen, (30, 30, 30), (x - h * .1, y - h * .1, w + h * .2, h + h * .2))
        pygame.draw.rect(screen, self.defaultColor, (x, y, w, h))
        pygame.draw.rect(screen, self.fillColor, (x, y, w * self.percent, h))
        screen.blit(self.digit, (self.x - self.digit.get_width() * 2, self.y - 3))
        screen.blit(self.percentText, (self.x + self.digit.get_width() + self.width, self.y - 3))