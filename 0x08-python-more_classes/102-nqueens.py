#!/usr/bin/python3

"""This module solves the N Queen problem"""
import sys


def is_safe(board, row, col, n):
    """
    This function solves the N Queen proble and
    prints all possible solutions
    """

    # Check if there is a queen in the same column
    for x in range(row):
        if board[x][col] == 'Q':
            return False

    # Check upper-left diagonal
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 'Q':
            return False

    # Check upper-right diagonal
    for x, y in zip(range(row, -1, -1), range(col, n)):
        if board[x][y] == 'Q':
            return False

    return True


def solve_nqueens(n):
    def backtrack(row):
        if row == n:
            solutions.append([''.join(row) for row in board])
            return

        for col in range(n):
                if is_safe(board, row, col, n):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(n)] for _ in range(n)]
    solution = []

    backtrack(0)

    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
