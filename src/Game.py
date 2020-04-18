import pygame
from pygame.locals import *
import random

from GameObjects.Player import Player
from GameObjects.Enemy import Enemy
from GameObjects.Bullet import Bullet


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

        # Bullet Variables
        self.aliveBullets = []
        self.bulletWidth = 5
        self.bulletHeight = 5
        self.bulletSpeed = 7

        # Player variables
        self.player = None
        self.playerWidth = 20
        self.playerHeight = 17

    # ----------------------------------------- Enemy Utility Methods -------------------------------------------------------------------------------

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

    # ----------------------------------------- Bullet utility methods ---------------------------------------------------------------------------------

    def __fireBullet__(self):
        if len(self.aliveBullets) == 0 or (self.aliveBullets[0].y < self.player.y - 50):
            bullet = Bullet(self.player.x + self.player.width/2, self.player.y -
                            self.player.height, self.bulletWidth, self.bulletHeight)
            self.aliveBullets.insert(0, bullet)

    def __handleBullets__(self):
        for bullet in self.aliveBullets:
            bullet.propagate(self.bulletSpeed)
            self.__cleanBulletIfDead__(bullet)
            bullet.drawCharacter(self.screen)

    def __cleanBulletIfDead__(self, bullet):
        if bullet.y < -self.bulletHeight:
            self.aliveBullets.remove(bullet)

    def runGame(self):
        pygame.init()
        pygame.display.set_caption('Shooting Game')

        self.player = Player(50, 560, self.playerWidth, self.playerHeight)
        self.isRunning = True

        while self.isRunning:
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.isRunning = False

            if keys[pygame.K_LEFT] and self.player.x > self.playerSpeed:
                self.player.propagate(-self.playerSpeed)
            elif keys[pygame.K_RIGHT] and self.player.x < self.screen.get_width() - self.player.width - self.playerSpeed:
                self.player.propagate(self.playerSpeed)

            if keys[pygame.K_SPACE]:
                self.__fireBullet__()

            self.screen.blit(self.background, (0, 0))
            self.player.drawCharacter(self.screen)
            self.__handleEnemies__()
            self.__handleBullets__()
            pygame.display.flip()

        pygame.quit()


game = Game()
game.runGame()
