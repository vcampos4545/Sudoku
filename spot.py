import pygame
pygame.font.init()
from constants import *

class Spot:
    def __init__(self, i, j, num, width):
        self.i = i
        self.j = j
        self.w = width
        self.y = i * self.w
        self.x = j * self.w
        self.num = num
        self.selected = False

    def draw(self, win):
        if self.selected:
            pygame.draw.rect(win, LIGHT_GREY, (self.x, self.y, self.w, self.w))
        else:
            pygame.draw.rect(win, WHITE, (self.x, self.y, self.w, self.w))

        if self.num != 0:
            font = pygame.font.Font('freesansbold.ttf',50)
            display = font.render(str(self.num),True,BLACK)
            textRect = display.get_rect()
            textRect.center = (self.x + self.w//2,self.y + self.w//2)
            win.blit(display,textRect)

    def set_color(self, color):
        self.color = color
