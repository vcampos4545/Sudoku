import pygame
from constants import *

class Spot:
    def __init__(self, i, j, num = None):
        self.i = i
        self.j = j
        self.w = WIDTH//9
        self.y = i * self.w
        self.x = j * self.w
        self.num = num

    def draw(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, self.w, self.w))
        if self.num != None:
            for i in range(self.num):
                pygame.draw.rect(win, BLACK, (self.x + 5*i, self.y, 3, 20))
