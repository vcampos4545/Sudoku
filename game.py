from spot import Spot
import random
import pygame
from constants import *
from solver import solve, possible

class Game:
    def __init__(self):
        self.generate_board()
        self.lives = 3
        self.sel_spot = None

    def draw(self, WIN):
        WIN.fill(WHITE)
        self.draw_spots(WIN)
        self.draw_grid(WIN)
        self.draw_lives(WIN)
        pygame.display.update()

    def update(self):
        # Check has at least 1 life
        if self.lives < 1:
            print('Game Over')
            self.reset()
            self.lives = 3

        # Check for events
        for event in pygame.event.get():

            #Check for game quit
            if event.type == pygame.QUIT:
                pygame.quit()

            if pygame.mouse.get_pressed()[0]: # LEFT
                self.set_selected_spot()

            if event.type == pygame.KEYDOWN:
                #Space to Solve board
                if event.key == pygame.K_SPACE:
                    self.set_pygame_board(self.solved_board)
                #n to create a new board
                if event.key == pygame.K_n:
                    self.lives = 3
                    self.generate_board()
                #r to reset current board
                if event.key == pygame.K_r:
                    self.reset()

                # Update number of selected_spot
                if self.sel_spot and not self.sel_spot.given:
                    if event.key == pygame.K_1:
                        self.sel_spot.num = 1
                    if event.key == pygame.K_2:
                        self.sel_spot.num = 2
                    if event.key == pygame.K_3:
                        self.sel_spot.num = 3
                    if event.key == pygame.K_4:
                        self.sel_spot.num = 4
                    if event.key == pygame.K_5:
                        self.sel_spot.num = 5
                    if event.key == pygame.K_6:
                        self.sel_spot.num = 6
                    if event.key == pygame.K_7:
                        self.sel_spot.num = 7
                    if event.key == pygame.K_8:
                        self.sel_spot.num = 8
                    if event.key == pygame.K_9:
                        self.sel_spot.num = 9
                    #Set inputed spot to red depending on if it is the wrong number
                    #at the selected spot
                    i,j = self.sel_spot.i, self.sel_spot.j
                    if self.sel_spot.num != 0 and self.sel_spot.num != self.solved_board[i][j]:
                        self.sel_spot.fcolor = RED
                        self.lives -= 1

#========================================================================
    #Helpers
#========================================================================

    def generate_board(self):
        # TO DO: Generate a board by solving a board and removing numbers
        self.board = [[5,3,0,0,7,0,0,0,0],
                     [6,0,0,1,9,5,0,0,0],
                     [0,9,8,0,0,0,0,6,0],
                     [8,0,0,0,6,0,0,0,3],
                     [4,0,0,8,0,0,0,0,1],
                     [7,0,0,0,2,0,0,0,6],
                     [0,6,0,0,0,0,2,8,0],
                     [0,0,0,4,1,9,0,0,5],
                     [0,0,0,0,8,0,0,7,0]]

        # Make pygame board of rows and columns of spot objects from the generated
        # board matrix
        temp_board = []

        for row in range(len(self.board)):
            temp = []
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    temp.append(Spot(row, col, self.board[row][col], GAP, True))
                else:
                    temp.append(Spot(row, col, self.board[row][col], GAP))
            temp_board.append(temp)

        self.pygame_board = temp_board

        solve(self.board, self.pygame_board)
        solved = []
        for row in range(len(self.pygame_board)):
            temp = []
            for col in range(len(self.pygame_board[row])):
                temp.append(self.pygame_board[row][col].num)
            solved.append(temp)

        self.set_pygame_board(self.board)
        self.solved_board = solved

    def draw_spots(self, WIN):
        for row in self.pygame_board:
            for spot in row:
                if spot.num == 0:
                    spot.fcolor = BLACK
                elif not spot.given and spot.num == self.solved_board[spot.i][spot.j]:
                    spot.fcolor = GREEN
                spot.draw(WIN)

    def draw_grid(self, WIN):
        for i in range(9):
            if i % 3 == 0:
                pygame.draw.line(WIN, BLACK, (0, i*GAP), (WIDTH, i*GAP),3)
                pygame.draw.line(WIN, BLACK, (i*GAP, 0), (i*GAP, WIDTH),3)
            else:
                pygame.draw.line(WIN, BLACK, (0, i*GAP), (WIDTH, i*GAP))
                pygame.draw.line(WIN, BLACK, (i*GAP, 0), (i*GAP, WIDTH))
        pygame.draw.line(WIN, BLACK, (0, WIDTH), (WIDTH, WIDTH),3)

    def draw_lives(self, WIN):
        font = pygame.font.Font('freesansbold.ttf',30)
        display = font.render("Lives: "+str(self.lives),True,BLACK)
        textRect = display.get_rect()
        textRect.center = (60,WIDTH + 25)
        WIN.blit(display,textRect)

    def reset(self):
        self.lives = 3
        self.set_pygame_board(self.board)

    def set_pygame_board(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.pygame_board[i][j].num = board[i][j]

    def set_selected_spot(self):
        x, y = pygame.mouse.get_pos()

        row = y // GAP
        col = x // GAP

        new_spot = self.pygame_board[row][col]
        if self.sel_spot:
            self.sel_spot.selected = False

        self.sel_spot = new_spot
        self.sel_spot.selected = True
