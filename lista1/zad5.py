def fraczero(n):
    n = int(n)
    if n < 0:
        raise Exception("n should be >= 0")

    zeros = 0
    factorial = 1
    if n == 1 or n == 0:
        return zeros
    for i in range(2, n + 1):
        factorial *= i
        if i % 5 == 0:
            zeros += 1
    return zeros


print(fraczero(10))
