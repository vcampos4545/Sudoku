import pygame
pygame.init()
pygame.font.init()
from constants import *

class Spot:
    def __init__(self, i, j, num, width, given=False):
        self.i = i
        self.j = j
        self.w = width
        self.y = i * self.w
        self.x = j * self.w
        self.num = num
        self.selected = False
        self.fcolor = BLACK
        self.given = given
        self.highlight = False
        self.notes = []

    def draw(self, win):
        #Draw rect with right color
        if self.selected:
            pygame.draw.rect(win, LIGHT_GREY, (self.x, self.y, self.w, self.w))
        elif self.highlight:
            pygame.draw.rect(win, YELLOW, (self.x, self.y, self.w, self.w))
        else:
            pygame.draw.rect(win, WHITE, (self.x, self.y, self.w, self.w))

        #Draw num if not 0
        if self.num != 0:
            font = pygame.font.Font('freesansbold.ttf',50)
            display = font.render(str(self.num),True,self.fcolor)
            textRect = display.get_rect()
            textRect.center = (self.x + self.w//2,self.y + self.w//2)
            win.blit(display,textRect)
        
        #Update notes:
        for i in range(1,9):
            count = self.notes.count(i)
            if count > 1:
                for _ in range(count):
                    self.notes.remove(i)
        #Draw notes
        for num in self.notes:
            font = pygame.font.Font('freesansbold.ttf',10)
            display = font.render(str(num),True,GREY)
            textRect = display.get_rect()
            textRect.center = (self.x + (self.w//9)*num,self.y + 10)
            win.blit(display,textRect)
