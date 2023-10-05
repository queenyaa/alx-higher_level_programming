#!/usr/bin/python3

"""

This module is to divide matrix

"""


def matrix_divided(matrix, div):

    """
    Divide all elements of a matrix by given number.

    Args:
        matrix (list of lists): the input matrix containing integers or floats
        div (int or float): the number to divide all elements of the matrix
            by (cannot be 0).

    Returns:
    list of lists: a new matrix with elements rounded to 2 decimal places

    Raises:
    TypeError: if 'matrix' is not a list of lists of integers of integers
        or floats, or if 'div' is not a number (integer or float).
    ZeroDivisionError: if 'div' is equal to 0
    ValueError: if the rows of 'matrix' is not the same size.
    """

    # Check if 'martix' is a list of lists of int or floats
    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    note_t = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(note_t)

    len_f = 0

    note_t = "Each row of the matrix must have the same size"

    for el in matrix:
        if not el or not isinstance(el, list):
            raise TypeError(note_t)

        if len_f != 0 and len(el) != len_f:
            raise TypeError(note_t)

        for nm in el:
            if not type(nm) in (int, float):
                raise TypeError(note_t)

        len_f = len(el)

    m = list(map(lambda y: list(map(lambda z: round(z / div, 2), y)), matrix))

    return (m)
