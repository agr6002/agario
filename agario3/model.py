import pygame
import random
import math
#from playsound import playsound
from player import Player
from enemy import Enemy
from food import Food

class Model:
    def __init__(self, app):
      print("Creating Model")
      self.app = app
      self.clock = pygame.time.Clock()
      self.FPS = 30
      self.timeChange = 0.0
      self.screenX = 1024
      self.screenY = 700
      self.worldTop = -700
      self.worldBottom = 1400
      self.worldRight = 2048
      self.worldLeft = -1024
      self.sizePlayer = 20
      self.spriteSpeed = 0.2
      self.sizeEnemies = 20
      self.numEnemies = 10
      self.enemies = []
      self.colors = [(250, 200, 0), (255, 0,0), (25, 200, 200), (0, 0, 0), (250, 125, 0),
        (200, 200, 200), (100, 50, 0), (0, 50, 250), (50, 50, 50), (100, 0, 200)]
      #              yellow         red       teal            white        orange
      self.sizeFood = 5
      self.numFood = 900
      self.food = []

    def initialize(self):
        print("Initialize Model")
        self.player = Player(self.screenX / 2, self.screenY / 2, self.spriteSpeed,
            self.sizePlayer, self.app, self.app.view.screen)
        for e in range(self.numEnemies):
            #print(speed)
            angle = random.uniform(0, 2 * math.pi)
            #print(angle)
            self.enemies.append(
                Enemy(
                    random.randrange(self.sizeEnemies, self.screenX - self.sizeEnemies),
                    random.randrange(self.sizeEnemies, self.screenY - self.sizeEnemies),
                    self.spriteSpeed, angle, self.colors[e],
                    self.sizeEnemies, self.app, self.app.view.screen
                )
            )

        for f in range(self.numFood):
            self.food.append(Food(
                random.randrange(self.worldLeft + self.sizeFood, self.worldRight - self.sizeFood),
                random.randrange(self.worldTop + self.sizeFood, self.worldBottom - self.sizeFood),
                self.sizeFood, self.app.view.screen, self.screenX, self.screenY))

    def run(self):
        #print("Running Model")
        self.timeChange = self.clock.tick(self.FPS)
        #self.playtime += milliseconds / 1000.0
        self.playerEat()
        self.enemiesEat()
        #self.enemiesEachOther()
        #self.enemiesEatPlayer()
        #self.playerEatEnemies()

    def finialize(self):
        print("Finialize Model")

    def negPos(self, num):
        float = random.random()
        if (float > 0.5):
            #print(num)
            return  num
        else:
            return -num

    def playerEat(self):
        #print("here")
        f = -1
        for a in range(len(self.food)):
            f += 1
            d=math.sqrt(
                (self.player.posX - self.food[f].posX) ** 2 +
                (self.player.posY - self.food[f].posY)**2
            )

            #print("----")
            #print(d)
            #print(self.player.size + self.food[f].size)
            if d > self.player.size + self.food[f].size:
                continue
            self.food.pop(f)
            self.player.size += 1
            self.player.speed *= 0.995
#            playsound('click.mp3')

            f -= 1
            #print("eat")

    def enemiesEat(self):
        e = -1
        for i in range(len(self.enemies)):
            e += 1
            f = -1
            for a in range(len(self.food)):
                f += 1
                d=math.sqrt((self.enemies[e].posX - self.food[f].posX) ** 2 + (self.enemies[e].posY - self.food[f].posY)**2)

                if d > self.enemies[e].size + self.food[f].size:
                    continue
                self.food.pop(f)
                self.enemies[e].size += 1
                self.enemies[e].speed *= 0.995
#                playsound('audio.mp3')
                f -= 1

    def enemiesEachOther(self):
        e = -1
        for i in range(len(self.enemies)):
            e += 1
            ee = -1
            for n in range(len(self.enemies)):
                ee += 1
                d=math.sqrt((self.enemies[e].posX - self.enemies[ee].posX) ** 2 + (self.enemies[e].posY - self.enemies[ee].posY)**2)

                if d > self.enemies[e].size + self.enemies[ee].size:
                    continue
                self.enemies[e].size += self.enemies[ee].size
                self.enemies[e].velX -= (self.enemies[ee].size - 20) / 5 * 0.005
                self.enemies[e].velY -= (self.enemies[ee].size - 20) / 5 * 0.005
                self.enemies.pop(ee)
                ee -= 1

    def enemiesEatPlayer(self):
        e = -1
        for i in range(len(self.enemies)):
            e += 1
            d=math.sqrt((self.enemies[e].posX - self.player.posX) ** 2 + (self.enemies[e].posY - self.player.posY)**2)

            if d > self.enemies[e].size + self.player.size:
                continue
            print("Game Over")
            self.app.mainloop = False
            # self.enemies[e].size += self.player.size
            # self.enemies[e].velX -= (self.enemies[e].size - 20) / 5 * 0.005
            # self.enemies[e].velY -= (self.enemies[e].size - 20) / 5 * 0.005
            # self.enemies.pop(e2)

    def playerEatEnemies(self):
        e = -1
        for e in range(len(self.enemies)):
            e += 1
            d=math.sqrt((self.player.posX - self.enemies[e].posX) ** 2 + (self.player.posY - self.enemies[e].posY)**2)

            if d > self.player.size + self.enemies[e].size:
                continue
            self.player.size += self.enemies[e].size
            self.player.velX -= (self.enemies[e].size - 20) / 5 * 0.005
            self.player.velY -= (self.enemies[e].size - 20) / 5 * 0.005
            self.enemies.pop(e)
            e -= 1
