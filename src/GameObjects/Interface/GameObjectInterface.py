import pygame

from abc import ABC, abstractmethod

# Abstract class to be implemented by all GameObjects


class GameObject(ABC):

    @abstractmethod
    def drawCharacter(self, canvas):
        pass

    @abstractmethod
    def propagate(self):
        pass

    @abstractmethod
    def checkCollission(self, gameObject):
        pass
