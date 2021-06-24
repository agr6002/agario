import pygame
import math

class Enemy:
    def __init__(self, posX, posY, speed, angle, color, size, app, screen):
        #print("Creating Enemy")
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.angle = angle
        self.color = color
        self.size = size
        self.app = app
        self.model = self.app.model
        self.screen = screen

    def move(self, timeChange):
        #print("move Enemy")
        #print(self.speed)
        #print(timeChange)
        d=math.sqrt(
            (self.posX - self.model.screenX / 2) ** 2 +
            (self.posY - self.model.screenY / 2)**2
        )
        if d < 300:
            if self.size > self.model.player.size:
                self.angle = math.atan2(
                     self.model.screenY / 2 - self.posY,
                     self.model.screenX / 2 - self.posX
                 )
            else:
                self.angle = math.atan2(
                     self.model.screenY / 2 - self.posY,
                     self.model.screenX / 2 - self.posX
                 ) + math.pi

        for e in range(len(self.model.enemies)):
            dE=math.sqrt(
                (self.posX - self.model.enemies[e].posX) ** 2 +
                (self.posY - self.model.enemies[e].posY)**2
            )
            if dE < 300:
                if self.size > self.model.enemies[e].size:
                    self.angle = math.atan2(
                         self.model.enemies[e].posY- self.posY,
                         self.model.enemies[e].posX - self.posX
                     )
                else:
                    self.angle = math.atan2(
                         self.model.enemies[e].posY - self.posY,
                         self.model.enemies[e].posX - self.posX
                     ) + math.pi

        self.posX += self.speed * timeChange * math.cos(self.angle)
        self.posY += self.speed * timeChange * math.sin(self.angle)

        pygame.draw.circle(self.screen, self.color, (round(self.posX),
            round(self.posY)), self.size)

        self.bounce()

    def bounce(self):
        if (self.posX > self.model.worldRight - self.size):
            self.posX = self.model.worldRight - self.size
            self.angle = math.pi - self.angle
        elif (self.posX < self.model.worldLeft + self.size):
            self.posX = self.model.worldLeft + self.size
            self.angle = math.pi - self.angle

        if (self.posY > self.model.worldBottom - self.size):
            self.posY = self.model.worldBottom- self.size
            self.angle = -self.angle
        elif (self.posY < self.model.worldTop + self.size):
            self.posY = self.model.worldTop + self.size
            self.angle = -self.angle
