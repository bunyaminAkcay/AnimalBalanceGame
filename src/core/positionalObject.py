from .drawableGameObject import DrawableGameObject
from .game import Game
import pygame

class PositionalObject(DrawableGameObject):
    
    def __init__(self, x, y, width, height, layer : int, backgroundColor = (0,0,0,0), visibility = True):
        super().__init__(layer, visibility)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self._backgroundColor = backgroundColor
        self._surface = None

    def _getSurface(self):
        return self._surface

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def _updateScale(self, zoom):
        pass

    def getScreenRect(self):
        camera = Game.getScene().mainCamera
        cameraCenterX = camera.centerX
        cameraCenterY = camera.centerY
        screenSize = Game.getScreenSize()
        relativeX = (self.x - cameraCenterX) * camera._zoom + screenSize[0]//2
        relativeY = (self.y - cameraCenterY) * camera._zoom + screenSize[1]//2
        
        return pygame.Rect(relativeX, relativeY, self._surface.get_rect().width, self._surface.get_rect().height)