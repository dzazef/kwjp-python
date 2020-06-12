from animation import Animation
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import numpy as np
import matplotlib.pylab as plt


if __name__ == '__main__':

    ACTIVATION = 'relu'

    # Sieć lepiej aproksymowała funkcję gdy nie miała na wejściu 1 neurona
    # Sieć działa dobrze jedynie dla ReLU.
    # Po dodaniu jeszcze jednej warstwy błąd zmniejszył się o połowę.

    x = np.linspace(-50, 50, 26)
    y = x ** 2
    plt.scatter(x, y)
    xp = np.linspace(-50, 50, 101)

    model = Sequential()
    model.add(Dense(10, input_shape=(1,), activation=ACTIVATION))
    model.add(Dense(10, activation=ACTIVATION))
    model.add(Dense(10, activation=ACTIVATION))
    model.add(Dense(1))
    model.compile(optimizer=Adam(), loss='mse')

    snapshot = []
    epochs = 80000
    step = 500
    for i in range(0, epochs, step):
        model.fit(x, y, epochs=step, batch_size=100, verbose=0)
        yp = model.predict(xp)
        snapshot.append(yp)
        # plt.plot(xp, yp)
        # plt.show()
        ev = model.evaluate(x, y, verbose=0)
        print(f'step {i + step} error: {ev * 100:.2f}%')
    print('Animacja...')
    anim = Animation(f"x2_1_5_1_{ACTIVATION}", np.reshape(xp, (-1, 1)), snapshot,
                     epochs, step, xlim=(-50, 50), ylim=(-1, 2500))
    anim.draw()