import pygame

from abc import ABC, abstractmethod


class GameObject(ABC):

    @abstractmethod
    def drawCharacter(self, canvas):
        pass

    @abstractmethod
    def propagate(self):
        pass
