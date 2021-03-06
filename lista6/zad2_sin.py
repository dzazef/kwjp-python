import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


def sigmoid(x) -> float:
    return 1.0 / (1.0 + np.exp(-x))


def sigmoid_der(x) -> float:
    return x * (1.0 - x)


class NeuralNetwork:

    def __init__(self, eta, seed, f, fd):
        np.random.seed(seed)
        self.weights1 = np.random.rand(1, 10)
        self.weights2 = np.random.rand(10, 1)
        self.output = np.zeros(10)
        self.eta = eta
        self.f, self.fd = f, fd
        self.layer1 = np.zeros(10)

    def feedforward(self, x_):
        """Feeding forward"""
        self.layer1 = self.f(np.dot(x_, self.weights1))
        self.output = self.f(np.dot(self.layer1, self.weights2))

    def backprop(self, x_, y_):
        """Back propagation"""
        d_weights2 = np.dot(self.layer1.T, 2 * (y_ - self.output) * self.fd(self.output))
        d_weights1 = np.dot(x_.T,
                            np.dot(2 * (y_ - self.output) * self.fd(self.output),
                                   self.weights2.T
                                   ) * self.fd(self.layer1)
                            )

        self.weights1 += d_weights1
        self.weights2 += d_weights2


class Animation:
    def __init__(self, x_, y_snapshots_, epochs_, anim_steps_):
        self.x = x_
        self.y_snapshots = y_snapshots_
        self.epochs = epochs_
        self.anim_step = anim_steps_
        self.fig = plt.figure()
        self.axes = plt.axes(xlim=(0, 2), ylim=(0, 1.1))
        self.scatter = self.axes.scatter([], [])
        self.text = self.axes.text(.8, 1.15, '', fontsize=15)

    def update(self, i_):
        """Update plot values"""
        self.scatter.set_offsets(np.concatenate((self.x, self.y_snapshots[i_]),
                                                axis=1))
        self.text.set_text(f'Step {i_ * self.anim_step}')
        return self.scatter, self.text,

    def draw(self):
        """Create animation"""
        anim = FuncAnimation(self.fig, self.update,
                             frames=(self.epochs // self.anim_step),
                             interval=40, blit=True)
        anim.save('anim_sin.gif', writer='imagemagick')


def run_nn(x_, x2_, epochs_, anim_steps_):
    """Run Neural Network"""
    snapshots_ = []
    nn_ = NeuralNetwork(0.5, 17, sigmoid, sigmoid_der)
    y_ = np.sin(x_)
    for i in range(epochs_):
        nn_.feedforward(x_ / 2)
        nn_.backprop(x_ / 2, y_)
        if i % anim_steps_ == 0:
            nn_.feedforward(x2_ / 2)
            snapshots_.append(nn_.output)
    return nn_, snapshots_


if __name__ == '__main__':
    epochs = 20000
    anim_steps = 100
    X = np.reshape(np.linspace(0, 2, 21), (-1, 1))
    X2 = np.reshape(np.linspace(0, 2, 161), (-1, 1))

    nn, snapshots = run_nn(X, X2, epochs, anim_steps)
    print('NN created, now running animation...')
    Animation(X2, snapshots, epochs, anim_steps).draw()
    print('Animation saved')
