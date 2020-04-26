import pygame

from GameObjects.Interface.GameObjectInterface import GameObject


class Player(GameObject):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(
            "GameObjects/SpriteImages/PlayerSpaceship.png")

        # Modify the hitbox size depending on the Image size for player
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def drawCharacter(self, canvas):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        canvas.blit(self.image, (self.x, self.y))

    def propagate(self, step):
        self.x += step

    def checkCollission(self, gameObject):
        return self.hitbox.colliderect(gameObject.hitbox)
