import math


def primes(n):
    values = list(range(2, n + 1))
    c = 0
    n_sqrt = int(math.sqrt(n))
    while c < len(values) and values[c] <= n_sqrt:
        i = c + 1
        while i < len(values):
            if values[i] % values[c] == 0:
                values.pop(i)
                i -= 1
            i += 1
        c += 1
    return values


print(primes(53))
