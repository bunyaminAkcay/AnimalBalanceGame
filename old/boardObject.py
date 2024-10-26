from core.spriteObject import SpriteObject

class BoardObject(SpriteObject):

    def go(self, x, y, squareSize, boardPosition):
        self.x = squareSize * x + boardPosition[0]
        self.y = squareSize * y + boardPosition[1]
        print("position : ",self.x, self.y)
    

    def move(self, x, y):
        pass