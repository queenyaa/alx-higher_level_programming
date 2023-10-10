#!/usr/bin/python3

"""
function to generate Pascal's triangle of n rows
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle with 'n' rows

    Args:
        n (int): number of rows to generate

    Returns:
        list of lists: pascal's triangle representation
    """
    if n <= 0:
        return []

    triangle =[[1]]

    for x in range(1, n):
        row = [1]  # initialize each row with 1
        prev_row = triangle[x -1]

        for y in range(1, x):
            row.append(prev_row[y - 1] + prev_row[y])

        row.append(1)  # add the last 1 to the row
        triangle.append(row)


    return triangle

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)
