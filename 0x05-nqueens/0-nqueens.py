#!/usr/bin/python3
"""NQueens class solves for all possible positions for queens
in an n * n board
"""
import sys


class NQueens():
    """NQueens class"""
    def solveNQueens(self, n):
        """solve for NQueens"""
        column = set()
        posDiag = set()  # constant for row + col
        negDiag = set()  # constant for row - col

        res = []
        board = [-1] * n

        def backtrack(row):
            """backtrack the board"""
            if row == n:
                res.append(board[:])
                return
            for col in range(n):
                pos = row + col
                neg = row - col
                if col in column or pos in posDiag or neg in negDiag:
                    continue
                column.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                board[row] = col
                backtrack(row + 1)
                column.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
                board[row] = -1
        backtrack(0)
        b = [[[row, col] for row, col in enumerate(sol)] for sol in res]
        return b


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('usage: nqueens N')
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)
    nq = NQueens()
    sol = nq.solveNQueens(n)
    for i in sol:
        print(i)
