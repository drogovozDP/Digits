import numpy as np
# from keras.datasets import mnist
from matplotlib import pyplot as plt
from Neural import Neural, Lenet
import pygame
import visualisation.Paint as Paint
from keras.models import model_from_json
import argparse


def run(model_name):
    pygame.init()
    WIDTH, HEIGHT, FPS = 280 * 2 + 280, 280 * 2, 90
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    run = True

    paint = Paint.Paint(screen, WIDTH - 280, HEIGHT)
    painting, eraser = False, False

    if model_name == 'perceptron':
        model = Neural(784, 100, 10, .001)
        model.loadWeights('./models/perceptron/weights.txt')
    elif model_name == 'lenet':
        model = model_from_json(open('./models/lenet/LeNetKeras.json').read())
        model.load_weights('./models/lenet/LeNetKeras.h5')
        model = Lenet(model)

    while run:
        clock.tick(FPS)

        # draw prediction
        paint.statistic(model.predict(paint.getPicture()))

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('model', help="You can choose between two models: 'lenet' or 'perceptron'")

    args = parser.parse_args()
    if {args.model}.issubset({'lenet', 'perceptron'}):
        run(args.model)
