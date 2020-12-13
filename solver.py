import numpy as np

def solve(board, pygame_board):
    """
    Returns a solved grid using backtracking and recursion
    """
    # TO DO: Fix solve and somehow get solved board in variable
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                for n in range(1,10):
                    if possible(board, row, col, n):
                        board[row][col] = n
                        solve(board, pygame_board)
                        board[row][col] = 0

                return

    for i in range(len(board)):
        for j in range(len(board[i])):
            pygame_board[i][j].num = board[i][j]
    print('A solution')

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
