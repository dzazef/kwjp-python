import math


class Graph:
    def __init__(self, x_dim=80, y_dim=24, scale_x=3):
        assert isinstance(x_dim, int) and isinstance(y_dim, int)
        assert isinstance(scale_x, int) or isinstance(scale_x, float)
        assert x_dim > 10 and y_dim > 10
        self.x_dim = x_dim + (x_dim + 1) % 2
        self.y_dim = y_dim + (y_dim + 1) % 2
        self.x_mid = int(self.x_dim / 2)
        self.y_mid = int(self.y_dim / 2)
        self.scale_x = scale_x

    def __get_empty_matrix(self):
        # noinspection PyUnusedLocal
        _graph = [[" " for a in range(self.y_dim)] for a in range(self.x_dim)]
        for i in range(self.x_dim):
            _graph[i][self.y_mid] = "-"
        for i in range(self.y_dim):
            _graph[self.x_mid][i] = "|"
        self.graph = _graph

    def __calc(self, f):
        results = []
        max_abs = 0
        scale = self.y_dim / (self.x_dim * self.scale_x)
        for x in range(-self.x_mid, self.x_mid + 1):
            f_x = f(x * scale)
            results.append(f_x)
            if abs(f_x) > max_abs:
                max_abs = f_x

        results[self.x_mid] = None
        return results, max_abs

    def __print_graph(self):
        for y in range(self.y_dim):
            for x in range(self.x_dim):
                print(self.graph[x][y], end='')
            print()

    def __mod_graph_from_res(self, results, max_abs):
        scale = self.y_mid / max_abs
        for x in range(self.x_dim):
            c_res = results[x]
            if c_res is not None:
                scaled = int(scale * c_res)
                y = self.y_mid - scaled
                self.graph[x][y] = "\033[0;31m*\033[0m"

    def draw(self, f):
        self.__get_empty_matrix()
        results, max_abs = self.__calc(f)
        self.__mod_graph_from_res(results, max_abs)
        self.__print_graph()


graph = Graph()
graph.draw(lambda x: x)
