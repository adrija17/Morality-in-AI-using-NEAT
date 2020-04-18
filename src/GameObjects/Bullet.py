import pygame

from GameObjects.Interface.GameObjectInterface import GameObject


class Bullet(GameObject):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # change the hitbox size depending on the Image size of the bullet
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def drawCharacter(self, canvas):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(canvas, (0, 0, 0), self.hitbox)

    def propagate(self, step):
        self.y -= step

    def checkCollission(self, gameObject):
        return self.hitbox.colliderect(gameObject.hitbox)
