import pygame

from abc import ABC, abstractmethod

# Interface to be used for all GameObjects


class GameObject(ABC):

    @abstractmethod
    def drawCharacter(self, canvas):
        pass

    @abstractmethod
    def propagate(self):
        pass
