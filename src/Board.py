from core.gameObject import GameObject
from core.clock import Clock

class Board(GameObject):

    def __init__(self, squareSize, boardPosition, boardSize, scene):
        super().__init__()
        self.squareSize = squareSize
        self.boardPosition = boardPosition
        self.boardSize = boardSize
        self.board = [[None for _ in range(boardSize[0])] for _ in range(boardSize[1])]
        self.clock = Clock(1000)
        self.scene = scene
        self.userWallLocations = []
        self.userWallCount = 10

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
    
    #if user wall added return true otherwise return false
    def addUserWall(self, x ,y):
        from userWall import UserWall
        if self.boardObject.board[y][x] != None:
            return False
        if len(self.userWallLocations) < self.userWallCount:        
            userWall = UserWall(x, y, self.boardObject, 0, None, (0, 0, 255, 255))
            self.scene.addGameObject(userWall)
            self.board[y][x] = userWall
            self.userWallLocations.append((x, y))
        else:
            firstWallIndex = self.userWallLocations[0]

            oldWall = self.board[firstWallIndex[0]][firstWallIndex[1]] 
            self.scene.removeGameObject(oldWall)

            self.userWallLocations.pop(0)

            userWall = UserWall(x, y, self.boardObject, 0, None, (0, 0, 255, 255))
            self.scene.addGameObject(userWall)
            self.board[y][x] = userWall
            self.userWallLocations.append((x, y))
        return True