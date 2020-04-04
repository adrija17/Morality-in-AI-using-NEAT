import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        self.flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN
        self.screen = pygame.display.set_mode((600, 600), self.flags)
        self.background = pygame.Surface(
            self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))
        self.isRunning = False

    def runGame(self):
        pygame.init()
        pygame.display.set_caption('Basic Pygame program')
        self.isRunning = True
        while self.isRunning:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN:
                    self.isRunning = False
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()
        pygame.quit()


game = Game()
game.runGame()
