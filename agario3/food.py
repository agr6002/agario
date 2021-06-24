import pygame

class Food:
    def __init__(self, posX, posY,  size, screen, screenx, screeny):
        #Sprint("Creating Food")
        self.posX = posX
        self.posY = posY
        self.color = (20, 50, 20)
        self.size = size
        self.screen = screen
        self.screenX = screenx
        self.screenY = screeny

    def move(self):
        #print("move Food")
        if(self.posX > 0 and self.posX < self.screenX and self.posY > 0 and self.posY < self.screenY):
            pygame.draw.circle(self.screen, self.color, (round(self.posX),
                round(self.posY)), self.size)
