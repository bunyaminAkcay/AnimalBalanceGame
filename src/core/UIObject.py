import pygame
from .drawableGameObject import DrawableGameObject

class UIObject(DrawableGameObject):
    def __init__(self, x ,y, width, height, layer, visibility):
        super().__init__(layer, visibility)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self._isUI = True
    
    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def getScreenRect(self):
        return self.getRect()