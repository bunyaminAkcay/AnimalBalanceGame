from .positionalObject import PositionalObject
import pygame

class SpriteObject(PositionalObject):

    def __init__(self, x, y, width, height, layer : int, image = None, backgroundColor = (0,0,0,0), visibility = True):
        super().__init__(x, y, width, height, layer, backgroundColor, visibility)
        self.__image = image
        if image != None:
            self.__scaledImage = pygame.transform.scale(image, (width, height))
        self._surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self._surface.fill(backgroundColor)
        if image != None:
            self._surface.blit(self.__scaledImage, (0,0))

    def _updateScale(self, zoom):
        if self.__image != None:
            self.__scaledImage = pygame.transform.scale(self.__image, (int(self.width * zoom), int(self.height * zoom)))
            self._surface.fill(self._backgroundColor)
            self._surface.blit(self.__scaledImage, (0, 0))
        self._surface = pygame.transform.scale(self._surface, (int(self.width * zoom), int(self.height * zoom)) )