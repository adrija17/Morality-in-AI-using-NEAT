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
        self.speed = 5

    def runGame(self):
        pygame.init()
        pygame.display.set_caption('Basic Pygame program')

        player = Player(50, 560, 20, 20)
        self.isRunning = True

        while self.isRunning:
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.isRunning = False

            if keys[pygame.K_LEFT] and player.x > self.speed:
                player.propagate(self.screen, -self.speed)
            elif keys[pygame.K_RIGHT] and player.x < self.screen.get_width() - player.width - self.speed:
                player.propagate(self.screen, self.speed)

            self.screen.blit(self.background, (0, 0))
            player.drawCharacter(self.screen)
            pygame.display.flip()

        pygame.quit()


game = Game()
game.runGame()
