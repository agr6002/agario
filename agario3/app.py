"""import pygame"""
import pygame
from model import Model
from view import View
from controller import Controller
class App:
    """class App"""
    def __init__(self):
        """def __init__"""
        print("creating App")
        self.model = Model(self)
        self.view = View(self)
        self.controller = Controller(self)
        self.mainloop = True
        # Desired framerate in frames per second. Try out other values.
        # Initialize Pygame.
        pygame.init()

        self.start()

    def start(self):
        self.initialize()
        self.run()
        self.finialize()

    def initialize(self):
        print("Initialize App")
        self.view.initialize()
        self.model.initialize()
        self.controller.initialize()

    def run(self):
        print("Running App")
        while self.mainloop:
            # Do not go faster than this framerate.
            self.model.run()
            self.view.run()
            self.controller.run()
            #Update Pygame display.
            pygame.display.flip()

    def finialize(self):
        print("Finialize App")
        self.model.finialize()
        self.view.finialize()
        self.controller.finialize()
        # Finish Pygame.
        pygame.quit()
        # At the very last:
        print("This game was played for {0:.2f} seconds".format(self.model.playtime))
