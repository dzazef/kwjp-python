import numpy as np


def sigmoid(x) -> float:
    return 1.0 / (1 + np.exp(-x))


def sigmoid_der(x) -> float:
    return x * (1.0 - x)


def relu(x) -> float:
    return x * (x > 0)


def relu_der(x) -> float:
    return 1. * (x > 0)


class NeuralNetwork:
    def __init__(self, x, y, eta, seed, layer1_g, layer1_gd, layer2_g, layer2_gd):
        np.random.seed(seed)
        self.input = x
        self.weights1 = np.random.rand(4, self.input.shape[1])
        self.weights2 = np.random.rand(1, 4)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = eta
        self.layer1_g, self.layer1_gd = layer1_g, layer1_gd
        self.layer2_g, self.layer2_gd = layer2_g, layer2_gd
        self.layer1 = np.zeros(4)

    def feedforward(self):
        """Feeding forward"""
        self.layer1 = self.layer1_g(np.dot(self.input, self.weights1.T))
        self.output = self.layer2_g(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        """Back propagation"""
        delta2 = (self.y - self.output) * self.layer2_gd(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = self.layer1_gd(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2


def run_nn(x_, y_, eta, seed, l1g, l1gd, l2g, l2gd):
    """Run NN for single case"""
    nn = NeuralNetwork(x_, y_, eta, seed, l1g, l1gd, l2g, l2gd)
    for i in range(5000):
        nn.feedforward()
        nn.backprop()
    print(nn.output)


def run_log(name_, x_, y_):
    """Run NN for logical operator"""
    print(f'\n\n======{name_}======\n\n')
    print('Sigmoid on layer1 + Sigmoid on end layer')
    run_nn(x_, y_, 0.5, 801010, sigmoid, sigmoid_der, sigmoid, sigmoid_der)
    print('Sigmoid on layer1 + ReLU on end layer')
    run_nn(x_, y_, 0.15, 1487627, sigmoid, sigmoid_der, relu, relu_der)
    print('ReLU on layer1 + Sigmoid on end layer')
    run_nn(x_, y_, 0.5, 34, relu, relu_der, sigmoid, sigmoid_der)
    print('ReLU on layer1 + ReLU on end layer')
    run_nn(x_, y_, 0.02, 444377, relu, relu_der, relu, relu_der)


if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True)
    X = np.array([[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])
    Y = np.array([[0], [1], [1], [0]])
    run_log("XOR", X, Y)
    X = np.array([[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])
    Y = np.array([[0], [0], [0], [1]])
    run_log("AND", X, Y)
    X = np.array([[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])
    Y = np.array([[0], [1], [1], [1]])
    run_log("OR", X, Y)

    # Wniosek: najlepsze rozwiązanie daje sieć oparta całkowicie
    # na funkcji ReLU.
    # Dodanie 1 w kolumne zwiększa dokładność wyników sieci przez
    # dodanie dodatkowych parametrów (wag).
