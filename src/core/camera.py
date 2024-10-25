from .gameObject import GameObject

class Camera(GameObject):

    def __init__(self, x, y, zoom=1):
        super().__init__()
        self.centerX = x
        self.centerY = y
        self._zoom = float(zoom)
        self._zoomed = False
    
    def zoom(self, zoomMultiplier):
        self._zoom = zoomMultiplier * self._zoom
        self._zoomed = True