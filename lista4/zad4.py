import math
from inspect import getfullargspec


class FunDict:
    """Class containing dictionary of overloaded functions"""
    fun_dict = {}


class Fun:
    """Class wrapping overloaded functions"""
    def __init__(self, fun):
        """Init object with function"""
        assert callable(fun)
        self.fun = fun

    def __call__(self, *args, **kwargs):
        """Find right function and call it"""
        fun_obj = Fun(self.fun)
        fun_dict = FunDict.fun_dict
        _fun = fun_dict.get(fun_obj.key(args=args))
        return _fun(*args, **kwargs)

    def key(self, args=None):
        """Get unique key for overloaded function"""
        if args is None:
            args = getfullargspec(self.fun).args
        return f"{self.fun.__name__}_{len(args)}"


def overload(fun):
    """Decorator for function overloading"""
    fun_obj = Fun(fun)
    fun_dict = FunDict.fun_dict
    fun_dict[fun_obj.key()] = fun
    return fun_obj


@overload
def norm(x, y):
    """Euclidean norm"""
    return math.sqrt(x * x + y * y)


@overload
def norm(x, y, z):
    """Taxicab norm"""
    return abs(x) + abs(y) + abs(z)


if __name__ == '__main__':
    print(norm(1, 1))
    print(norm(1, 1, 1))
