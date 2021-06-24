import pygame

class Controller:
    def __init__(self, app):
        print("Creating Controller")
        self.app = app

    def initialize(self):
        print("Initialize Controller")

    def run(self):
        #print("Running Controller")
        for event in pygame.event.get():
            # User presses QUIT-button.
            if event.type == pygame.QUIT:
                self.app.mainloop = False
            elif event.type == pygame.KEYDOWN:
                # User presses ESCAPE-Key
                if event.key == pygame.K_ESCAPE:
                    self.app.mainloop = False
                elif event.key == pygame.K_q:
                    self.app.mainloop = False


    def finialize(self):
        print("Finialize Controller")
