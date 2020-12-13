from constants import BLACK
import pygame

class Button:
    def __init__(self, x, y, w, h, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text

    def contains(self, pos):
        if pos[0] >= self.x and pos[0] < self.x+self.w:
            if pos[1] >= self.y and pos[1] < self.y+self.h:
                return True
        return False
    
    def action(self):
        return self.text
    
    def draw(self, WIN):
        pygame.draw.rect(WIN, BLACK, (self.x, self.y, self.w, self.h),1)

        font = pygame.font.Font('freesansbold.ttf',15)
        display = font.render(self.text,True,BLACK)
        textRect = display.get_rect()
        textRect.center = (self.x + self.w//2, self.y + self.h//2)
        WIN.blit(display,textRect)
