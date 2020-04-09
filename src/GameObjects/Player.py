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

    def propagate(self, canvas, step, keys):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > step:
            self.x -= step
        elif keys[pygame.K_RIGHT] and self.x < canvas.get_width() - self.width - step:
            self.x += step

