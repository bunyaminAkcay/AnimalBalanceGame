
import pygame
from .UIObject import UIObject

class UIbox(UIObject):
    def __init__(self, layer, x ,y, w, h, image):
        super().__init__(layer, x ,y)
        
        self.__image = image
        if image != None:
            self.__scaledImage = pygame.transform.scale(image, (w, h))
        self.__surface = pygame.Surface((w, h), pygame.SRCALPHA)
        if image != None:
            self.__surface.blit(self.__scaledImage, (0,0))

    def _getSurface(self):
        return self.__surface