#!/usr/bin/python3
"""Defines a function to calculate the perimeter of an island."""

def island_perimeter(grid):
    """Calculate the perimeter of an island.

    The function calculates the perimeter of an island defined by a grid.
    In the grid, water is represented by 0 and land by 1.

    Args:
        grid (list): A list of lists of integers representing the island.

    Returns:
        int: The perimeter of the island.
    """
    num_columns = len(grid[0])
    num_rows = len(grid)
    num_edges = 0
    num_land_cells = 0

    for x in range(num_rows):
        for y in range(num_columns):
            if grid[x][y] == 1:
                num_land_cells += 1
                if (y > 0 and grid[x][y - 1] == 1):
                    num_edges += 1
                if (x > 0 and grid[x - 1][y] == 1):
                    num_edges += 1
    return num_land_cells * 4 - num_edges * 2
