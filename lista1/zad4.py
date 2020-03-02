import math


def prime_factors(n):
    factors = []
    n = int(n)
    if n < 2:
        raise Exception("n is smaller than 2")

    for i in range(2, int(math.sqrt(n)) + 1):
        flag = False
        counter = 0
        while n % i == 0:
            flag = True
            counter += 1
            n /= i
        if flag:
            factors.append((i, counter))

    return factors


print(prime_factors(3991680))
