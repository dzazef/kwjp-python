import math


class Graph:
    def __init__(self, x_dim=80, y_dim=24, scale_y=1.2):
        assert isinstance(x_dim, int) and isinstance(y_dim, int)
        assert isinstance(scale_y, int) or isinstance(scale_y, float)
        assert x_dim > 10 and y_dim > 10 and scale_y > 1
        self.x_dim = x_dim + (x_dim + 1) % 2
        self.y_dim = y_dim + (y_dim + 1) % 2
        self.x_mid = int(self.x_dim / 2)
        self.y_mid = int(self.y_dim / 2)
        self.scale_y = scale_y

    def __get_empty_matrix(self):
        # noinspection PyUnusedLocal
        _graph = [[" " for a in range(self.y_dim)] for a in range(self.x_dim)]
        for i in range(self.x_dim):
            _graph[i][self.y_mid] = "-"
        for i in range(self.y_dim):
            _graph[self.x_mid][i] = "|"
        self.graph = _graph

    def __calc(self, f, f_min, f_max):
        results = []
        max_abs = 0
        step = (f_max - f_min) / (self.x_dim - 1)
        for x in range(self.x_dim):
            f_x = f(f_min + step * x)
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
        scale = self.y_mid / (max_abs * self.scale_y)
        for x in range(self.x_dim):
            c_res = results[x]
            if c_res is not None:
                scaled = int(scale * c_res)
                y = self.y_mid - scaled
                try:
                    self.graph[x][y] = "\033[0;31m*\033[0m"
                except IndexError:
                    pass

    def draw(self, f, f_min, f_max):
        self.__get_empty_matrix()
        results, max_abs = self.__calc(f, f_min, f_max)
        self.__mod_graph_from_res(results, max_abs)
        self.__print_graph()


dict_f = {"cos(x)": lambda x: math.cos(x),
          "sin(x)": lambda x: math.sin(x),
          "x": lambda x: x,
          "2x": lambda x: 2 * x
          }

graph = Graph()
f, a, b = 0, 0, 0
try:
    f = dict_f[input("f(x) = ")]
except KeyError:
    print("incorrect f(x)")
    exit(1)
try:
    a = float(input("a = "))
except ValueError:
    print("incorrect a")
    exit(1)
try:
    b = float(input("b = "))
except ValueError:
    print("incorrect b")
    exit(1)
assert b > a
graph.draw(f, a, b)
