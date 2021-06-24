import pygame
import math

class Player:
    def __init__(self, posX, posY, speed, size, app, screen):
      print("Creating Player")
      self.posX = posX
      self.posY = posY
      self.speed = speed
      self.size = size
      self.app = app
      self.screen = screen
      self.moveX = 0
      self.moveY = 0
      self.bounceX = False
      self.bounceY = False

    def move(self, timeChange):
        #print("Move Player")
        x, y = pygame.mouse.get_pos()
        self.angle = math.atan2(y - self.posY, x - self.posX)
        self.bounce()
        self.dx = self.speed * timeChange * math.cos(self.angle) + self.moveX
        self.dy = self.speed * timeChange * math.sin(self.angle) + self.moveY
        self.app.model.worldTop -= self.dy
        self.app.model.worldBottom -= self.dy
        self.app.model.worldLeft -= self.dx
        self.app.model.worldRight -= self.dx
        for e in self.app.model.enemies:
            e.posX -= self.dx
            e.posY -= self.dy
        for f in self.app.model.food:
            f.posX -= self.dx
            f.posY -= self.dy

        self.bounceUndo()
        pygame.draw.circle(self.screen, (0, 0, 255), (round(self.posX),
            round(self.posY)), self.size)

    def bounce(self):
        if (self.posX > self.app.model.worldRight - self.size):
            self.angle = math.pi - self.angle
            self.bounceX = True
            self.moveX = -self.size
        elif (self.posX < self.app.model.worldLeft + self.size):
            self.angle = math.pi - self.angle
            self.bounceX = True
            self.moveX = self.size

        if (self.posY > self.app.model.worldBottom - self.size):
            self.angle = -self.angle
            self.bounceY = True
            self.moveY = -self.size
        elif (self.posY < self.app.model.worldTop + self.size):
            self.angle = -self.angle
            self.bounceY = True
            self.moveY = self.size

    def bounceUndo(self):
        if (self.bounceX):
            self.moveX = 0
            self.angle = math.pi - self.angle
            self.bounceX = False

        if (self.bounceY):
            self.moveY = 0
            self.angle = -self.angle
            self.bounceY = False


#end
