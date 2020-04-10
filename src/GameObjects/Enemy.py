import pygame

from GameObjects.Interface.GameObjectInterface import GameObject


class Enemy(GameObject):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.image = pygame.image.load(
            "GameObjects/SpriteImages/EnemySpaceship.png")

    def drawCharacter(self, canvas):
        self.hitbox = (self.x, self.y, self.width, self.height)
        canvas.blit(self.image, (self.x, self.y))

    def propagate(self, speed):
        self.y += speed
