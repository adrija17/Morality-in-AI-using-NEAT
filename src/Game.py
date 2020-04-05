import pygame
from pygame.locals import *
from GameObjects.Player import Player

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
        clock = pygame.time.Clock()
        pygame.display.set_caption('Basic Pygame program')
        self.isRunning = True
        while self.isRunning:
            dt = clock.tick(clock.get_fps())/1000
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.isRunning = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.isRunning = False
            man.propagate(self.screen,(120*dt))           
            self.screen.blit(self.background, (0, 0))
            pygame.draw.aaline(self.screen, (0,0,0), (0,line_height), (600,line_height))
            man.drawCharacter(self.screen)
            pygame.display.flip()
        pygame.quit()

line_height = 450
man = Player(50,line_height-20,20,20)
game = Game()
game.runGame()

