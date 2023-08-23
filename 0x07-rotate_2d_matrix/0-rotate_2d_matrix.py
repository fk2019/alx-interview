#!/usr/bin/python3
"""Rotate a 2d matrix clockwise
"""


def rotate_2d_matrix(matrix):
    """Rotates elements of matrix 90 deg"""
    if type(matrix) is not list:
        exit(1)
    if len(matrix) <= 0:
        exit(1)
    # check if all elements of matrix are lists
    if not all(map(lambda x: type(x) == list, matrix)):
        exit(1)
    rows = len(matrix)
    columns = len(matrix[0])
    # verify if matrix lists have length equal to columns
    if not all(map(lambda x: len(x) == columns, matrix)):
        exit(1)
    col, row = 0, rows - 1
    for i in range(columns * rows):
        if i % rows == 0:
            matrix.append([])
        if row == -1:
            row = rows - 1
            col += 1
        matrix[-1].append(matrix[row][col])
        if col == columns - 1 and row >= -1:
            matrix.pop(row)
        row -= 1
