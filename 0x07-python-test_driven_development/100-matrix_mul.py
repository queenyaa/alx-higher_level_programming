#!/usr/bin/python3

"""
This module multiplies two matrices

"""


def matrix_mul(m_a, m_b):

    """
    The functino multiplies two matrices

    Args:
        m_a (list of lists): the 1st matrix
        m_b (list of lists): the 2nd matrix

    Returns:
    list of lists: the result of multiplying m_a by m_b.

    Raises:
    TypeError: if m_a or m_b is not a list, not a list of lists,
        empty, or contains non-integer/float elements
    ValueError: if m_a and m_b cannot be multiplied due to incompatible
        dimensions
    """

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Check if m_a and m_b contain only integers or floats
    if not all(isinstance(num, (int, float))
            for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float))
            for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    # Check if m_a and m_b have compatible dimensions for multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # initialize the result matrix with zeros
    res = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # perform matrix multiplication
    for x in range(len(m_a)):
        for y in range(len(m_b[0])):
            for z in range(len(m_b)):
                res[x][y] += m_a[x][z] * m_b[z][y]

    return (res)
