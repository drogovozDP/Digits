import pygame
from visualisation.Scroll import Scroll
from visualisation.Buttons import*

class Panel:
    def __init__(self, x, y, width, height, paint):
        self.x = x
        self.y = y
        self.paint = paint
        self.screen = paint.screen
        self.width = width
        self.height = height
        self.renderer = pygame.font.SysFont('serif', 25)
        self.color = (50, 50, 50)
        self.numbers = []
        self.buttons = []
        self._createPanel()

    def _createPanel(self):
        for i in range(10):
            digit = self.getText(i)
            percentText = self.getText(0)
            self.numbers.append(Scroll(self.x + 50, 20 + 25 * i, self.width / 2, 25, digit, percentText))
        word = self.renderer.render("Clear", True, (234, 54, 123))
        self.buttons.append(DeleteBtn(self.x + (self.width - 100) / 2, 300, 100, 50, word, self))

    def showNumbers(self, numbers):
        numbers = numbers
        for i in range(len(self.numbers)):
            self.numbers[i].percent = numbers[i]
            self.numbers[i].percentText = self.getText(round(numbers[i] * 100, 2))

    def checkClick(self, pos):
        for btn in self.buttons:
            btn.checkClick(pos)

    def checkHover(self, pos):
        for btn in self.buttons:
            btn.checkHover(pos)

    def getText(self, text):
        return self.renderer.render(str(text), True, (234, 54, 123))

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        for number in self.numbers:
            number.draw(self.screen)
        for btn in self.buttons:
            btn.draw(self.screen)
