from .gameObject import GameObject

class DrawableGameObject(GameObject):

    def __init__(self, layer, visibility):
        super().__init__()
        self._layer = layer
        self._drawable = True
        self.visibility = visibility
        self._isUI = False
    
    def _updateScale(self, zoom):
        pass

    def getRect(self):
        pass

    def getScreenRect(self):
        pass