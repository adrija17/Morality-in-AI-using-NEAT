import pygame
from pygame.locals import *
import random

from GameObjects.Player import Player
from GameObjects.Enemy import Enemy


class Game:
    def __init__(self):
        self.flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN

        # Screen vairbales
        self.screenHeight = 600
        self.screenWidth = 600
        self.screen = pygame.display.set_mode(
            (self.screenWidth, self.screenHeight), self.flags)
        self.background = pygame.Surface(
            self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

        # Game-Environment variables
        self.isRunning = False
        self.playerSpeed = 5
        self.probabilityOfGeneration = 0.02

        # Enemy Variables
        self.aliveEnemies = []
        self.enemyWidth = 20
        self.enemyHeight = 17
        self.enemySpeed = 3

    def __generateEnemies__(self):
        if len(self.aliveEnemies) < 3 or self.aliveEnemies[-1].y > (self.screenHeight + self.aliveEnemies[-1].height):
            if random.uniform(0, 1) < self.probabilityOfGeneration:
                self.aliveEnemies.insert(
                    0, Enemy(random.randrange(self.enemyWidth, self.screenWidth - self.enemyWidth, 1), -10, self.enemyWidth, self.enemyHeight))

    def __cleanEnemyIfDead__(self, enemy):
        if enemy.y > self.screenHeight + enemy.height:
            self.aliveEnemies.remove(enemy)

    def __handleEnemies__(self):
        self.__generateEnemies__()
        for enemy in self.aliveEnemies:
            enemy.propagate(self.enemySpeed)
            self.__cleanEnemyIfDead__(enemy)
            enemy.drawCharacter(self.screen)

    def runGame(self):
        pygame.init()
        pygame.display.set_caption('Shooting Game')

        player = Player(50, 560, 20, 20)
        self.isRunning = True

        while self.isRunning:
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.isRunning = False

            if keys[pygame.K_LEFT] and player.x > self.playerSpeed:
                player.propagate(-self.playerSpeed)
            elif keys[pygame.K_RIGHT] and player.x < self.screen.get_width() - player.width - self.playerSpeed:
                player.propagate(self.playerSpeed)

            self.screen.blit(self.background, (0, 0))
            player.drawCharacter(self.screen)
            self.__handleEnemies__()
            pygame.display.flip()

        pygame.quit()


game = Game()
game.runGame()
