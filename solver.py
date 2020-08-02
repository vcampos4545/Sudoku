import numpy as np
from spot import Spot


def solve(grid):
    """
    Returns a solved grid using backtracking and recursion
    """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                for n in range(1,10):
                    if possible(grid, row, col, n):
                        grid[row][col] = n
                        solve(grid)
                        grid[row][col] = 0

                return

    print('Solved board:\n',np.matrix(grid))

#Helpers
def possible(grid, i, j, n):
    """
    Returns a boolean indicating whether an integer, n, can be placed
    at grid position (i,j)
    """
    if grid[i][j] == 0:
        #Check Row of grid
        for index in range(len(grid[i])):
            if grid[i][index] != 0 and grid[i][index] == n:
                return False
        #Check Column of grid
        for index in range(len(grid)):
            if grid[index][j] != 0 and grid[index][j] == n:
                return False
        #Check Square of grid
        di = i%3
        dj = j%3
        for row in range(3):
            for col in range(3):
                if grid[i+row-di][j+col-dj] == n:
                    return False

        return True

    return False
