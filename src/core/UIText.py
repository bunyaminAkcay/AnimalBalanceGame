import pygame
from .UIObject import UIObject

class UIText(UIObject):

    font = [None]

    def __init__(self, textString, x ,y, fontSize, layer, fontColor, fontBackground = None, visibility = True):
        if not pygame.font.get_init():
            pygame.font.init()
        
        self.fontBackground = fontBackground
        self.fontColor = fontColor

        self.__font = pygame.font.Font(UIText.font[0], fontSize)
        if fontBackground == None:
            self.__text = self.__font.render(textString, True, fontColor)
        else:
            self.__text = self.__font.render(textString, True, fontColor, fontBackground)

        self.__textRect = self.__text.get_rect()
        super().__init__(x ,y, self.__textRect.width, self.__textRect.height, layer, visibility)

    def _getSurface(self):
        return self.__text
    
    @staticmethod
    def setFont(fontPath):
        UIText.font[0] = fontPath

    def setText(self, textString):
        if self.fontBackground == None:
            self.__text = self.__font.render(textString, True, self.fontColor)
        else:
            self.__text = self.__font.render(textString, True, self.fontColor, self.fontBackground)

        self.__textRect = self.__text.get_rect()