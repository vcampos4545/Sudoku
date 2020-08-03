import pygame
import random
from constants import *
from solver import solve, possible
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

    # Make pygame board of rows and columns of spot objects from the generated
    # board matrix
    pygame_board = []

    for row in range(len(board)):
        temp = []
        for col in range(len(board[row])):
            if board[row][col] != 0:
                temp.append(Spot(row, col, board[row][col], gap, True))
            else:
                temp.append(Spot(row, col, board[row][col], gap))
        pygame_board.append(temp)

    return pygame_board, board

def draw_lives(WIN, lives):
    font = pygame.font.Font('freesansbold.ttf',40)
    display = font.render("Lives: "+str(lives),True,BLACK)
    textRect = display.get_rect()
    textRect.center = (80,WIDTH + 20)
    WIN.blit(display,textRect)

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
    WIN = pygame.display.set_mode((WIDTH, WIDTH + 40))
    pygame.display.set_caption('Sudoku')
    gap = WIDTH//9
    pygame_board, board = generate_board(gap)

    # Game Loop
    loop = True
    selected_spot = None
    lives = 3
    while loop:
        if lives < 1:
            pygame_board, board = generate_board(gap)
            lives = 3
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
                if not selected_spot.given:
                    if event.key == pygame.K_1:
                        selected_spot.num = 1
                        if possible(board, selected_spot.i, selected_spot.j, 1):
                            selected_spot.fcolor = GREEN
                        else:
                            selected_spot.fcolor = RED
                            lives -= 1
                        board[selected_spot.i][selected_spot.j] = 1
                    if event.key == pygame.K_2:
                        selected_spot.num = 2
                        if possible(board, selected_spot.i, selected_spot.j, 2):
                            selected_spot.fcolor = GREEN
                        else:
                            selected_spot.fcolor = RED
                            lives -= 1
                        board[selected_spot.i][selected_spot.j] = 2
                    if event.key == pygame.K_3:
                        selected_spot.num = 3
                        if possible(board, selected_spot.i, selected_spot.j, 3):
                            selected_spot.fcolor = GREEN
                        else:
                            selected_spot.fcolor = RED
                            lives -= 1
                        board[selected_spot.i][selected_spot.j] = 3
                    if event.key == pygame.K_4:
                        selected_spot.num = 4
                        if possible(board, selected_spot.i, selected_spot.j, 4):
                            selected_spot.fcolor = GREEN
                        else:
                            selected_spot.fcolor = RED
                            lives -= 1
                        board[selected_spot.i][selected_spot.j] = 4
                    if event.key == pygame.K_5:
                        selected_spot.num = 5
                        if possible(board, selected_spot.i, selected_spot.j, 5):
                            selected_spot.fcolor = GREEN
                        else:
                            selected_spot.fcolor = RED
                            lives -= 1
                        board[selected_spot.i][selected_spot.j] = 5
                    if event.key == pygame.K_6:
                        selected_spot.num = 6
                        if possible(board, selected_spot.i, selected_spot.j, 6):
                            selected_spot.fcolor = GREEN
                        else:
                            selected_spot.fcolor = RED
                            lives -= 1
                        board[selected_spot.i][selected_spot.j] = 6
                    if event.key == pygame.K_7:
                        selected_spot.num = 7
                        if possible(board, selected_spot.i, selected_spot.j, 7):
                            selected_spot.fcolor = GREEN
                        else:
                            selected_spot.fcolor = RED
                            lives -= 1
                        board[selected_spot.i][selected_spot.j] = 7
                    if event.key == pygame.K_8:
                        selected_spot.num = 8
                        if possible(board, selected_spot.i, selected_spot.j, 8):
                            selected_spot.fcolor = GREEN
                        else:
                            selected_spot.fcolor = RED
                            lives -= 1
                        board[selected_spot.i][selected_spot.j] = 8
                    if event.key == pygame.K_9:
                        selected_spot.num = 9
                        if possible(board, selected_spot.i, selected_spot.j, 9):
                            selected_spot.fcolor = GREEN
                        else:
                            selected_spot.fcolor = RED
                            lives -= 1
                        board[selected_spot.i][selected_spot.j] = 9


        WIN.fill(WHITE)
        for row in pygame_board:
            for spot in row:
                spot.draw(WIN)
        draw_grid(WIN, gap)
        #TODO Create lives variable
        draw_lives(WIN, lives)
        pygame.display.update()

main()
