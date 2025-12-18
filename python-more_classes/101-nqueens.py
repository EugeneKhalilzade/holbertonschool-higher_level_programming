#!/usr/bin/python3
"""
N Queens problem solver
"""

import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)


def is_safe(queens, row, col):
    """
    Check if a queen can be placed at (row, col)
    """
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, queens, solutions):
    """
    Backtracking solution for N Queens
    """
    if row == n:
        solution = []
        for r, c in enumerate(queens):
            solution.append([r, c])
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append(col)
            solve_nqueens(n, row + 1, queens, solutions)
            queens.pop()


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(n, 0, [], solutions)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
