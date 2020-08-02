import pygame
import random
from constants import *
from solver import solve
import numpy as np
from spot import Spot

def generate_board(gap):
    # TO DO: Generate a board by solving a board and removing numbers
    board = [[5,3,0,0,7,0,0,0,0],
             [6,0,0,1,9,5,0,0,0],
             [0,9,8,0,0,0,0,6,0],
             [8,0,0,0,6,0,0,0,3],
             [4,0,0,8,0,3,0,0,1],
             [7,0,0,0,2,0,0,0,6],
             [0,6,0,0,0,0,2,8,0],
             [0,0,0,4,1,9,0,0,5],
             [0,0,0,0,8,0,0,7,9]]

    pygame_board = []

    for row in range(len(board)):
        temp = []
        for col in range(len(board[row])):
            temp.append(Spot(row, col, board[row][col], gap))
        pygame_board.append(temp)

    return pygame_board, board

def draw_grid(WIN, gap):
    for i in range(9):
        if i % 3 == 0:
            pygame.draw.line(WIN, BLACK, (0, i*gap), (WIDTH, i*gap),3)
            pygame.draw.line(WIN, BLACK, (i*gap, 0), (i*gap, WIDTH),3)
        else:
            pygame.draw.line(WIN, BLACK, (0, i*gap), (WIDTH, i*gap))
            pygame.draw.line(WIN, BLACK, (i*gap, 0), (i*gap, WIDTH))

def get_clicked_pos(gap):
    x, y = pygame.mouse.get_pos()

    row = y // gap
    col = x // gap

    return row, col

def main():
    # Initialize pygame window and board
    WIN = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption('Sudoku')
    gap = WIDTH//9
    pygame_board, board = generate_board(gap)

    # Game Loop
    loop = True
    selected_spot = None
    while loop:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if pygame.mouse.get_pressed()[0]: # LEFT

                row, col = get_clicked_pos(gap)
                spot = pygame_board[row][col]
                if selected_spot:
                    selected_spot.selected = False
                selected_spot = spot
                selected_spot.selected = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('Solving board')
                    solve(board)
                    print('solved_board')
                    print(np.matrix(board))

        WIN.fill(WHITE)
        for row in pygame_board:
            for spot in row:
                spot.draw(WIN)
        draw_grid(WIN, gap)
        pygame.display.update()

main()
