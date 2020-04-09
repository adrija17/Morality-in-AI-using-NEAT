import pygame

from GameObjects.Interface.GameObjectInterface import GameObject


class Player(GameObject):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Modify the hitbox size depending on the Image size for player
        self.hitbox = (self.x, self.y,self.width, self.height)

    def drawCharacter(self, canvas):
        pygame.draw.rect(canvas,(0,255,0),self.hitbox)
        self.hitbox = (self.x, self.y, self.width, self.height)

    def propagate(self, canvas, step):
            self.x += step

