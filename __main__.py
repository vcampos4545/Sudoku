import pygame
from constants import *
from game import Game

def main():
    # Initialize pygame window and board
    game = Game()
    WIN = pygame.display.set_mode((WIDTH, WIDTH + 40))
    pygame.display.set_caption('Sudoku')

    # Game Loop
    loop = True
    while loop:
        game.update()
        game.draw(WIN)

main()
