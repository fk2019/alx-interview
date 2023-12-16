#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """island perimeter function"""
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 sides

                # Check adjacent cells (up, down, left, right)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Deduct 2 sides for adjacent land
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
