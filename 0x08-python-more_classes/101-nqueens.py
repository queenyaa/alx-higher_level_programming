#!/usr/bin/python3

""" functions that solve N-queens puzzle """
import sys


def in_board(n):
    # initialize an m x m size chessboard with 0's
    bod = []
    [bod.append([]) for x in range(n)]
    [row.append(' ') for x in range(n) for row in bod]
    return (bod)


def dcp_board(bod):
    # Return a deepcopy
    if isinstance(bod, list):
        return list(map(dcp_board, bod))
    return (bod)


def g_solu(bod):
    # Return list of lists of solved board

    solution = []
    for y in range(len(bod)):
        for z in range(len(bod)):
            if bod[y][z] == "Q":
                solution.append([y, z])
                break
    return (solution)


def x_out(bod, row, col):

    for z in range(col + 1, len(bod)):
        bod[row][z] = "x"

    for z in range(col - 1, -1, -1):
        bod[row][z] = "x"

    for y in range(row + 1, len(bod)):
        bod[y][col] = "x"

    for y in range(row - 1, -1, -1):
        bod[y][col] = "x"

    z = col + 1
    for y in range(row + 1, len(bod)):
        if z >= len(bod):
            break
        bod[y][z] = "x"
        z += 1

    z = col - 1
    for y in range(row - 1, -1, -1):
        if z < 0:
            break
        bod[y][z]
        z -= 1

    z = col + 1
    for y in range(row - 1, -1, -1):
        if z >= len(bod):
            break
        bod[y][z] = "x"
        z += 1

    z = col - 1
    for y in range(row + 1, len(bod)):
        if z < 0:
            break
        bod[y][z] = "x"
        z -= 1


def rec_solve(bod, row, queens, solutions):

    if queens == len(bod):
        solutions.append(g_solu(bod))
        return (solutions)

    for z in range(len(bod)):
        if bod[row][z] == " ":
            tmp_bod = dcp_board(bod)
            tmp_bod[row][z] = "Q"
            x_out(tmp_bod, row, z)
            solutions = rec_solve(tmp_bod, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    bod = in_board(int(sys.argv[1]))
    solutions = rec_solve(bod, 0, 0, [])
    for solu in solutions:
        print(solu)
