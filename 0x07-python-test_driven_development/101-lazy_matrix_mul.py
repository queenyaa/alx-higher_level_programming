#!/usr/bin/python3

""" Function to multiply matrices with NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices m_a and m_b using NumPy
    Args:
    m_a (list of lists): 1st matrix
    m_b (list of lists): 2nd matrix
    """

    # convert input matrices to NumPy arrays
    m_a = np.array(m_a)
    m_b - np.array(m_b)

    # Perform matrix multiplication using NumPy's dot function
    res = np.dot(m_a, m_b)

    return res
