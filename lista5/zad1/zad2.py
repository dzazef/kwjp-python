import pandas as pd
import numpy as np


class Recommendation:

    def __init__(self, path_r, path_m):
        """Constructor
        :param path_r path to ratings.csv
        :param path_m path to movies.csv
        """
        self.path_r = path_r
        self.path_m = path_m
        self._prepare_data()
        self._fill_matrices()
        self._norm_matrix()

    def _prepare_data(self):
        """Reads data from file"""
        r0 = pd.read_csv(self.path_r)
        r1 = r0[r0.movieId < 10000]
        self.ratings = r1[['userId', 'movieId', 'rating']].to_numpy()
        m0 = pd.read_csv(self.path_m)
        m1 = m0[m0.movieId < 10000]
        m2 = m1.assign(movieId=m1.movieId - 1)
        self.movies = m2[['movieId', 'title']].to_numpy()
        self.n = int(r1.userId.iloc[-1])  # uid of last user
        self.m = int(max(self.ratings[:, 1]))  # uid of last movie

    def _fill_matrices(self):
        a = np.zeros(shape=(self.n, self.m))
        for row in self.ratings:
            uid = int(row[0])
            mid = int(row[1])
            a[uid - 1][mid - 1] = row[2]
        self.a0 = a

    def get_title(self, mid):
        t = self.movies[self.movies[:, 0] == mid]
        return t[0][1] if len(t) > 0 else "<no_title>"

    def _norm_matrix(self):
        norm = np.linalg.norm(self.a0, axis=0)
        norm = [x if x != 0.0 else 1.0 for x in norm]
        self.a1 = self.a0 / norm

    def _res_to_data_frame(self, p_np):
        p_pd = pd.DataFrame(dict(
            mid=np.arange(len(p_np)).ravel(),
            pred=p_np.ravel()
        ))
        p_pd = p_pd[p_pd.pred > 0.0]
        p_pd.insert(2, 'title', [self.get_title(x) for x in p_pd.mid])
        p_pd = p_pd.sort_values(by='pred', ascending=False)
        return p_pd

    def get_predictions(self, ratings):
        norm = np.linalg.norm(ratings)
        if norm == 0.0:  # if ratings are empty, predictions are empty
            return pd.DataFrame(dict(mid=[], pred=[], title=[]))
        rn = ratings / norm
        z = np.dot(self.a1, rn)
        zn = z / np.linalg.norm(z)
        p_np = np.dot(self.a1.T, zn)
        return self._res_to_data_frame(p_np)


if __name__ == '__main__':
    r = Recommendation(path_r='../assets/ml-latest-small/ratings.csv',
                       path_m='../assets/ml-latest-small/movies.csv')
    my_ratings = np.zeros((9018, 1))
    my_ratings[2570] = 5  # 2571 - Matrix
    my_ratings[31] = 4  # 32 - Twelve Monkeys
    my_ratings[259] = 5  # 260 - Star Wars IV
    my_ratings[1096] = 4  # 1097 - ET
    df = r.get_predictions(my_ratings)
    print(df[['pred', 'title']].head(10))
