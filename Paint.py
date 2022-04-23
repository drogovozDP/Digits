from Cell import Cell
from Panel import Panel
import numpy as np


class Paint:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.canvas = []
        self.panel = Panel(width, 0, 280, height, self)
        self._create()

    def _create(self):
        range_w = self.width / 28
        range_h = self.height / 28
        for i in range(28):
            row = []
            for j in range(28):
                row.append(Cell(range_w * j, range_h * i, range_w, range_h))
            self.canvas.append(row)

    def paint(self, coords):
        x, y = int(coords[0] / (self.width / 28)), int(coords[1] / (self.height / 28))
        if x > 27: return
        self.canvas[y][x].color = (255, 255, 255)

    def eraser(self, coords):
        x, y = int(coords[0] / (self.width / 28)), int(coords[1] / (self.height / 28))
        if x > 27: return
        self.canvas[y][x].color = (0, 0, 0)

    def getPicture(self):
        pic = np.zeros((28, 28))
        for i in range(len(self.canvas)):
            for j in range(len(self.canvas[i])):
                pic[i][j] = self.canvas[i][j].getValue()
        new_pic = pic
        new_pic = new_pic[:, :, np.newaxis]
        # return pic.reshape(784)
        return new_pic

    def statistic(self, numbers):
        # print(list(numbers).index(max(numbers)))
        self.panel.showNumbers(numbers)

    def draw(self):
        self.panel.draw()
        for row in self.canvas:
            for col in row:
                col.draw(self.screen)