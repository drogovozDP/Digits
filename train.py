import numpy as np
from Neural import Neural
from keras.datasets import mnist

(train_X, train_Y), (test_X, test_Y) = mnist.load_data()
train_X = np.asfarray(train_X).astype(float)

neural = Neural(784, 100, 10, .001)
for j in range(10):
    for i in range(60000):
        target = np.zeros(10) + 0.01
        target[train_Y[i]] = 0.99
        neural.train(train_X[i].reshape(784), target)

neural.saveWeights()