#!/usr/bin/python3
"""
N Queens problem solver
"""

import sys


def is_safe(queens, row, col):
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, queens, solutions):
    if row == n:
        solutions.append([[r, c] for r, c in enumerate(queens)])
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append(col)
            solve_nqueens(n, row + 1, queens, solutions)
            queens.pop()


def main():
    # 1️⃣ Argument count check
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # 2️⃣ Integer check
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # 3️⃣ Minimum value check
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(n, 0, [], solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
