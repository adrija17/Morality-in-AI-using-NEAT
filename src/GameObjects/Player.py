import pygame

from GameObjects.Interface.GameObjectInterface import GameObject


class Player(GameObject):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Modify the hitbox size depending on the Image size for player
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def drawCharacter(self, canvas):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(canvas, (0, 255, 0), self.hitbox)

    def propagate(self, step):
        self.x += step

    def checkCollission(self, gameObject):
        return self.hitbox.colliderect(gameObject.hitbox)
