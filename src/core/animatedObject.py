from .positionalObject import PositionalObject
import pygame

class AnimatedObject(PositionalObject):

    def __init__(self, x, y, width, height, layer : int, animationList, backgroundColor = (0,0,0,0), visibility = True):
        super().__init__(x, y, width, height, layer, backgroundColor, visibility)
        
        self.animationList = animationList
        self.currentAnimationIndex = 0
        self.__scaledImage = pygame.transform.scale(self.animationList[self.currentAnimationIndex].getCurrentImage(), (width, height))
        self._surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self._surface.fill(backgroundColor)
        self._surface.blit(self.__scaledImage, (0,0))

    def _updateScale(self, zoom):
        self.__scaledImage = pygame.transform.scale(self.animationList[self.currentAnimationIndex].getCurrentImage(), (int(self.width * zoom), int(self.height * zoom)))
        self._surface.fill(self._backgroundColor)
        self._surface.blit(self.__scaledImage, (0, 0))
        self._surface = pygame.transform.scale(self._surface, (int(self.width * zoom), int(self.height * zoom)) )
    


    def update(self):
        if self.animationList[self.currentAnimationIndex].clock.checkTickable() == True:
            scaledImageSize = self.__scaledImage.get_size()
            self.__scaledImage = pygame.transform.scale(self.animationList[self.currentAnimationIndex].getCurrentImage(), (scaledImageSize))
            self._surface.fill(self._backgroundColor)
            self._surface.blit(self.__scaledImage, (0, 0))
            self._surface = pygame.transform.scale(self._surface, (scaledImageSize) )