import pygame

from Interface.GameObjectInterface import GameObject

class Bullet(GameObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # change the hitbox size depending on the Image size of the bullet
        self.hitbox = (self.x, self.y, 20, 20)

    def drawCharacter(self, canvas):
        pass

    def propagate(self, step):
        pass

    