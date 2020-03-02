def pascal(n):
    rows = [[1]]
    row = [1]
    k = [0]
    for x in range(max(n - 1, 0)):
        row = [l + r for (l, r) in zip(row + k, k + row)]
        rows.append(row)
    return rows


def print_pascal(rows):
    n = len(rows) - 1
    max_val = len(str(rows[n-1][int(n/2)]))
    for row in rows:
        print(((max_val + 1) * " ") * n, end='')
        for elem in row:
            print(" " + (str(elem) + (" " * (max_val - len(str(elem))))) + (max_val * " ") + " ", end='')
        print(((max_val + 1) * " ") * n)
        n -= 1
    pass


print_pascal(pascal(9))
