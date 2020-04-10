import pygame

from GameObjects.Interface.GameObjectInterface import GameObject


class Enemy(GameObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Change the dims of hitbox depending on Image size
        self.hitbox = (self.x, self.y, 20, 20)

    def drawCharacter(self, canvas):
        self.hitbox = (self.x, self.y, 20, 20)
        pygame.draw.rect(canvas, (0, 0, 0), self.hitbox)

    def propagate(self, speed):
        self.y += speed
