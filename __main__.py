import pygame
import random
from constants import *
from solver import solve
import numpy as np
from spot import Spot

def generate_board():
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
            if board[row][col] != 0:
                temp.append(Spot(row, col, board[row][col]))
            else:
                temp.append(Spot(row, col))

        pygame_board.append(temp)

    return pygame_board

def main():
    loop = True

    board = generate_board()

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        WIN.fill(WHITE)
        gap = WIDTH//9
        for row in board:
            for spot in row:
                spot.draw(WIN)
        for i in range(len(board)):
            if i % 3 == 0:
                pygame.draw.line(WIN, BLACK, (0, i*gap), (WIDTH, i*gap),3)
                pygame.draw.line(WIN, BLACK, (i*gap, 0), (i*gap, WIDTH),3)
            else:
                pygame.draw.line(WIN, BLACK, (0, i*gap), (WIDTH, i*gap))
                pygame.draw.line(WIN, BLACK, (i*gap, 0), (i*gap, WIDTH))
        pygame.display.update()

main()
