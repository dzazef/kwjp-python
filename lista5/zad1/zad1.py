import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# noinspection PyMethodMayBeStatic


class RatingFinder:

    def __init__(self, path):
        self.path = path
        self.data = np.array([])
        self.usr = 0

    def prepare_data(self):
        """Reads data from file"""
        d0 = pd.read_csv(self.path)
        usr = d0[d0.movieId == 1][['userId']].to_numpy().ravel()
        self.usr = len(usr)
        d1 = d0[d0['userId'].isin(usr)]
        d1.insert(0, 'userIdNew',
                  d1.userId.replace(usr, np.arange(self.usr)))
        self.data = (d1[['userIdNew', 'movieId', 'rating']].to_numpy())

    def _fill_matrices(self, n, m):
        """Convert data to matrix and vector"""
        a = np.zeros(shape=(n, m))
        b = np.zeros(shape=n)
        for row in self.data:
            uid = int(row[0])
            mid = int(row[1])
            if mid < m + 2 and uid < n:
                if mid == 1:  # Toy Story
                    b[uid] = row[2]
                else:
                    a[uid][mid - 2] = row[2]
        return a, b

    def predict(self, row, x, exact=False) -> float:
        """Predict ranking of Toy Story movie base on other movies"""
        pred = np.dot(row, x)
        return (pred if not exact
                else max(0.0, min(5.0, round(pred * 2) / 2)))

    def error(self, row, x, real, exact=False) -> float:
        """Calculates error of ranking prediction"""
        pred = self.predict(row, x, exact)
        return pred - real

    def linear_regression(self, n, m):
        """Calculates the least-squares solution x to ax=b"""
        a, b = self._fill_matrices(n, m)
        x = np.linalg.lstsq(a, b, rcond=None)[0]
        return a, b, x

    def draw_plot_pred(self, users, real, pred, m, zad):
        """Draw plot for prediction"""
        plt.scatter(users, real, label='Real')
        plt.scatter(users, pred, label='Predicted', c='red')
        plt.xlabel('users')
        plt.ylabel('rating')
        plt.title(f'Toy Story rating, m = {m}')
        plt.legend()
        plt.savefig(fname=f'{zad}_{m}_pre')
        plt.clf()

    def draw_plots_err(self, users, errors, m, zad):
        """Draw plot for error"""
        plt.scatter(users, errors, label='Error')
        plt.title(f'Error of prediction for m = {m}')
        plt.legend()
        plt.savefig(fname=f'{zad}_{m}_err')
        plt.clf()

    def zad_a(self):
        for m in [10, 100, 1000, 10000]:
            a, b, x = self.linear_regression(self.usr, m)
            users = np.arange(self.usr)
            pred = [self.predict(a[uid], x) for uid in users]
            errors = [self.error(a[uid], x, b[uid]) for uid in users]
            self.draw_plot_pred(users, b, pred, m, zad='z1a')
            self.draw_plots_err(users, errors, m, zad='z1a')

    def zad_b(self):
        for m in [10, 100, 200, 500, 1000, 10000]:
            a_200, b_200, x = self.linear_regression(200, m)
            a_215, b_215 = self._fill_matrices(self.usr, m)
            users = np.arange(self.usr - 200)
            real = [b_215[uid + 200] for uid in users]
            pred = [self.predict(a_215[uid + 200], x, exact=True)
                    for uid in users]
            errors = [self.error(a_215[uid + 200], x, b_215[uid + 200],
                                 exact=True) for uid in users]
            self.draw_plot_pred(users, real, pred, m, zad='z1b')
            self.draw_plots_err(users, errors, m, zad='z1b')


if __name__ == '__main__':
    rf = RatingFinder('../assets/ml-latest-small/ratings.csv')
    rf.prepare_data()
    rf.zad_a()
    rf.zad_b()
