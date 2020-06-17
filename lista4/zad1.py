import random
import time


def exec_time(fun):
    """Decorator printing on stdout time of function run."""
    def wrapper():
        start_time = time.time_ns()
        ret = fun()
        end_time = time.time_ns()
        print(f"Run time: {(end_time - start_time) / 1e6}ms ")
        return ret
    return wrapper


@exec_time
def example_fun():
    """Example function."""
    x = 0
    for i in range(int(1e3)):
        for j in range(int(1e3)):
            x = (x + random.randint(0, 5)) / 2  # do some slow stuff
    return x


if __name__ == '__main__':
    print(example_fun())
