from core.clock import Clock
from core.gameObject import GameObject

class Board(GameObject):

    def __init__(self, squareSize, boardPosition, boardSize):
        super().__init__()

        self.boardSize = boardSize
        self.board = [[None for _ in range(boardSize[0])] for _ in range(boardSize[1])]
        self.squareSize = squareSize
        self.boardPosition = boardPosition
        self.clock = Clock(1000)
        

    def insertObject(self, object, x, y):
        self.board[y][x] = object
        object.go(x, y, self.squareSize, self.boardPosition)

    def moveObject(self, x1, y1, x2, y2):
        self.board[y1][x1], self.board[y2][x2] = self.board[y2][x2], self.board[y1][x1]
    
    def update(self):
        if self.clock.getTicks() > 0:
            print("tick")
            for y, row in enumerate(self.board):
                for x, boardObject in enumerate(row):

                    if boardObject == None:
                        continue

                    possibleMove = None
                    
                    while(True):
                        
                        possibleMove = boardObject.move(x, y)
                        print(x, y, possibleMove)
                        if self.__checkMove(possibleMove[0], possibleMove[1]) == True:
                            break
                    
                    self.moveObject(x, y, possibleMove[0], possibleMove[1])
                    boardObject.go(x, y, self.squareSize, self.boardPosition)
    
    
    def __checkMove(self, x,y):
        if self.boardSize[0] > x > 0 and self.boardSize[1] > y > 0: 
            return True
        return False