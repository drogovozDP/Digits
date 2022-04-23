import numpy as np
from scipy.special import expit


class Neural:
    def __init__(self, input_count, hidden_count, output_count, koeff):
        self.wih = np.random.rand(hidden_count, input_count) - 0.5
        self.who = np.random.rand(output_count, hidden_count) - 0.5
        self.act_func = lambda x: expit(x)
        self.lr = koeff

    def train(self, train_input, target):
        inputs = np.array(train_input, ndmin=2).T
        targets = np.array(target, ndmin=2).T

        hidden_inputs = np.dot(self.wih, inputs)
        hidden_outputs = self.act_func(hidden_inputs)

        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.act_func(final_inputs)

        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.who.T, output_errors)

        self.who += self.lr * np.dot((output_errors * final_outputs * (1 - final_outputs)), np.transpose(hidden_outputs))
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1 - hidden_outputs)), np.transpose(inputs))

    def query(self, input):
        hidden = self.act_func(self.wih.dot(input))
        return self.act_func(self.who.dot(hidden))

    def saveWeights(self):
        weights = open("weights.txt", 'w')
        line = ""
        for i in range(len(self.wih)):
            for j in range(len(self.wih[0])):
                line += (str(self.wih[i][j]) + ",")
        line = line[:-1]
        weights.write(line+'\n')
        line = ""
        for i in range(len(self.who)):
            for j in range(len(self.who[0])):
                line += (str(self.who[i][j]) + ",")
        line = line[:-1]
        weights.write(line)
        weights.close()

    def loadWeights(self):
        weights = open("weights.txt", "r")
        self.wih = np.reshape(np.asfarray(weights.readline().split(',')), (100, 784))
        self.who = np.reshape(np.asfarray(weights.readline().split(',')), (10, 100))
        weights.close()
