from animation import Animation
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pylab as plt


if __name__ == '__main__':

    ACTIVATION = 'tanh'

    # Zadanie próbowałem dla różnych warstw sieci, jednak 1-5-1 daje
    # wystarczające wyniki. tanh działa znacznie lepiej niż sigmoid
    # lub relu. Błąd w danym kroku wyświetlany jest w konsoli.

    # Dane z wykładu, ale przez małą dziedzinę nie wiele widać
    # x = np.linspace(0, 2, 21)
    # y = np.sin(x)
    # xp = np.linspace(0, 2, 161)

    # Ciekawsze dane
    x = np.arange(0, np.pi * 2, 0.1)
    y = np.sin(x)
    xp = x

    model = Sequential()
    model.add(Dense(1, input_shape=(1,), activation=ACTIVATION))
    model.add(Dense(5, activation=ACTIVATION))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['mean_squared_error'])

    snapshot = []
    epochs = 40000
    step = 500
    for i in range(0, epochs, step):
        model.fit(x, y, epochs=step, batch_size=16, verbose=0)
        yp = model.predict(xp)
        snapshot.append(yp)
        # plt.plot(xp, yp)
        # plt.show()
        ev = model.evaluate(x, y, verbose=0)
        print(f'step {i + step} error: {ev[1] * 100:.2f}%')
    print('Animacja...')
    anim = Animation(f"sin_1_5_1_{ACTIVATION}", np.reshape(xp, (-1, 1)), snapshot,
                     epochs, step, xlim=(0, np.pi*2), ylim=(-1.2, 1.2))
    anim.draw()