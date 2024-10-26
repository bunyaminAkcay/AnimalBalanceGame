from core.spriteObject import SpriteObject
from Board import Board

class BoardObject(SpriteObject):

    def __init__(self, boardX, boardY, boardObject : Board, layer, image = None, backgroundColor = (0, 0, 0, 0), visibility = True):
        x = boardObject.boardPosition[0] + boardObject.squareSize * boardX
        y = boardObject.boardPosition[1] + boardObject.squareSize * boardY
        width = boardObject.squareSize
        height = boardObject.squareSize
        self.boardObject = boardObject
        self.boardObject.board[boardY][boardX] = self
        self.boardX = boardX
        self.boardY = boardY
        super().__init__(x, y, width, height, layer, image, backgroundColor, visibility)
    

    def go(self, boardX, boardY):
        self.boardX = boardX
        self.boardY = boardY

        x = self.boardObject.boardPosition[0] + self.boardObject.squareSize * boardX
        y = self.boardObject.boardPosition[1] + self.boardObject.squareSize * boardY

        self.x = x
        self.y = y
    
    def move():
        pass

    def checkMove(self, x, y):
        return self.boardObject.checkInBoard(x, y)
    
    