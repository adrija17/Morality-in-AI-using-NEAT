import pygame

from Interface.GameObjectInterface import GameObject


class Enemy(GameObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Change the dims of hitbox depending on Image size
        self.hitbox = (self.x, self.y, 20, 20)

    def drawCharacter(self, canvas):
        pass

    def propagate(self, speed):
        pass
