import numpy as np
from keras.datasets import mnist
from Neural import Neural

(train_X, train_Y), (test_X, test_Y) = mnist.load_data()
train_X = np.asfarray(train_X).astype(float)
test_X = np.asfarray(test_X).astype(float)

neural = Neural(784, 100, 10, .001)
neural.loadWeights('./models/perceptron/weights.txt')

right_count = 0
test_count = len(test_Y)
for i in range(test_count):
    a = neural.predict(test_X[i].reshape(784))
    if list(a).index(max(abs(a))) == test_Y[i]:
        right_count += 1

print(f"Accuracy: {right_count / test_count * 100}%")
