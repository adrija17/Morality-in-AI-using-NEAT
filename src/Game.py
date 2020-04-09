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
        player = Player(50,450,20,20)
        pygame.display.set_caption('Basic Pygame program')
        self.isRunning = True
        while self.isRunning:
            keys = pygame.key.get_pressed()
            dt = clock.tick(40)
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.isRunning = False
                    
            if len(keys)!= 0:
                player.propagate(self.screen,5,keys)          
            self.screen.blit(self.background, (0, 0))
            player.drawCharacter(self.screen)
            pygame.display.flip()
                 
        pygame.quit()

     
game = Game()
game.runGame()


