import pygame

class View:
    def __init__(self, app):
        print("Creating View")
        self.app = app
        self.model = self.app.model

    def initialize(self):
        print("Initialize View")
        # Set size of pygame window.
        #screen = pygame.display.set_mode(size=(0, 0), flags=pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode(size=(self.model.screenX,
            self.model.screenY))
        # Create empty pygame surface.
        self.background = pygame.Surface(self.screen.get_size())
        # Fill the background white color.
        self.background.fill((255, 100, 100))
        # Convert Surface object to make blitting faster.
        self.background = self.background.convert()
        # Copy background to screen (position (0, 0) is upper left corner).
        self.screen.blit(self.background, (0, 0))

    def run(self):
        # print("Running View")
        self.screen.fill((255, 100, 100))
        f = -1
        for a in self.model.food:
            f += 1
            self.model.food[f].move()
        e = -1
        for i in self.model.enemies:
            e += 1
            self.model.enemies[e].move(self.model.timeChange)
        self.model.player.move(self.model.timeChange)
        pygame.display.update()

        if(self.model.worldTop >= 0):
            pygame.draw.line(self.screen, (0, 0, 255), (self.model.worldLeft, self.model.worldTop), (self.model.worldRight, self.model.worldTop))
        if(self.model.worldBottom <= self.model.screenY):
            pygame.draw.line(self.screen, (0, 0, 255), (self.model.worldLeft, self.model.worldBottom), (self.model.worldRight, self.model.worldBottom))
        if(self.model.worldLeft >= 0):
            pygame.draw.line(self.screen, (0, 0, 255), (self.model.worldLeft, self.model.worldTop), (self.model.worldLeft, self.model.worldBottom))
        if(self.model.worldRight <= self.model.screenX):
            pygame.draw.line(self.screen, (0, 0, 255), (self.model.worldRight, self.model.worldTop), (self.model.worldRight, self.model.worldBottom))

    def finialize(self):
        print("Finialize View")
