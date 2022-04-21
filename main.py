import numpy as np
# from keras.datasets import mnist
from matplotlib import pyplot as plt
from Neural import Neural
import pygame, Paint
from keras.models import model_from_json

# (train_X, train_Y), (test_X, test_Y) = mnist.load_data()
# train_X = np.asfarray(train_X).astype(float)

neural = Neural(784, 100, 10, .001)
# for j in range(10):
#     for i in range(60000):
#         target = np.zeros(10) + 0.01
#         target[train_Y[i]] = 0.99
#         neural.train(train_X[i].reshape(784), target)

# neural.saveWeights()
neural.loadWeights()

# test_count = len(test_Y)
# for i in range(test_count):
#     a = neural.query(test_X[i].reshape(784))
#     if list(a).index(max(abs(a))) == test_Y[i]:
#         right_count += 1
# print(right_count / test_count * 100)
# print(neural.query(train_X[0].reshape(784)))
# for i in range(9):
#     plt.subplot(330 + 1 + i)
#     plt.imshow(train_X[i], cmap=plt.get_cmap("gray"))
# plt.show()

pygame.init()
WIDTH, HEIGHT, FPS = 280 * 2 + 280, 280 * 2, 90
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
run = True

paint = Paint.Paint(screen, WIDTH - 280, HEIGHT)
painting, eraser = False, False
lenet = model_from_json(open('LeNetKeras.json').read())
lenet.load_weights('LeNetKeras.h5')

print(paint.getPicture())
while run:
    clock.tick(FPS)

    # paint.statistic(neural.query(paint.getPicture()))
    paint.statistic(lenet.predict(np.array(paint.getPicture(), ndmin=4)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                paint.paint(event.pos)
                paint.panel.checkClick(event.pos)
                painting = True
            elif event.button == 3:
                paint.eraser(event.pos)
                eraser = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                painting = False
            elif event.button == 3:
                eraser = False
        if event.type == pygame.MOUSEMOTION:
            paint.panel.checkHover(event.pos)
            if painting:
                paint.paint(event.pos)
        if event.type == pygame.MOUSEMOTION and eraser:
            paint.eraser(event.pos)
    screen.fill((0, 0, 0))
    paint.draw()
    pygame.display.update()