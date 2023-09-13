#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    matrix_1 = []
    for row in matrix:
        n_row = []
        for n in row:
            n_row.append(n ** 2)
        matrix_1.append(n_row)

    return (matrix_1)
