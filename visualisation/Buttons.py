import pygame

class Button:
    def __init__(self, x, y, width, height, text, panel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.panel = panel
        self.color = (100, 100, 100)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        offset_x = (self.width - self.text.get_width()) / 2
        offset_y = (self.height - self.text.get_height()) / 2
        screen.blit(self.text, (self.x + offset_x, self.y + offset_y))

    def checkClick(self, pos):
        x, y = pos[0], pos[1]
        if self.x <= x and self.y <= y and self.x + self.width >= x and self.y + self.height >= y:
            self.onClick()

    def checkHover(self, pos):
        x, y = pos[0], pos[1]
        if self.x <= x and self.y <= y and self.x + self.width >= x and self.y + self.height >= y:
            self.color = (70, 70, 70)
        else:
            self.color = (100, 100, 100)

    def onClick(self):
        pass

class DeleteBtn(Button):
    def __init__(self, x, y, width, height, text, panel):
        Button.__init__(self, x, y, width, height, text, panel)

    def onClick(self):
        for row in self.panel.paint.canvas:
            for col in row:
                col.color = (0, 0, 0)
