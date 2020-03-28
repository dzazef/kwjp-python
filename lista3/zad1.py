

def transpose_matrix(matrix):
    """Returns transponse of given matrix"""
    return [' '.join([row[i] for row in [x.split(' ') for x in matrix]])
            for i in range(len(matrix))]


print(transpose_matrix(["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]))
