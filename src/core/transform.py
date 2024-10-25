class Transform:

    @staticmethod
    def getPixelPositionFromPosition(screenW, screenH, x, y, w, h, cameraCenterX, cameraCenterY, zoom):
        relativeX = (x - cameraCenterX) * zoom + screenW//2
        relativeY = (y - cameraCenterY) * zoom + screenH//2
        isInWindow = False
        
        if  ((relativeX     <= screenW and relativeX     >= 0-w) and (relativeY     <= screenH and relativeY     >= 0-h)):
            isInWindow = True
        
        return isInWindow, (relativeX, relativeY)