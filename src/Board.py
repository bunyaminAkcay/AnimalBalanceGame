from core.gameObject import GameObject
from core.clock import Clock

class Board(GameObject):

    def __init__(self, squareSize, boardPosition, boardSize):
        super().__init__()
        self.squareSize = squareSize
        self.boardPosition = boardPosition
        self.boardSize = boardSize
        self.board = [[None for _ in range(boardSize[0])] for _ in range(boardSize[1])]
        self.clock = Clock(1)


    def checkInBoard(self, x, y):
        print(x, " ", y)
        if self.boardSize[0] > x >= 0 and self.boardSize[1] > y >= 0:
            return True
        return False

    def update(self):
        if self.clock.getTicks() > 0:

            for y, row in enumerate(self.board):
                    for x, boardObject in enumerate(row):
                        if boardObject == None:
                            continue
                        boardObject.move()