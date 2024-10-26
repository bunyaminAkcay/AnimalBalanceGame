import random

from boardObject import BoardObject

class Animal(BoardObject):

    def move(self):
        
        possibleWays = [ (1, 0), (-1,0), (0, 1), (0,-1)]
        possibleWay = None
        while(len(possibleWays) != 0):

            possibleWayIndex = random.randint(0, len(possibleWays) -1)

            isPossible = self.checkMove(possibleWays[possibleWayIndex][0] + self.boardX, possibleWays[possibleWayIndex][1] + self.boardY)

            if(isPossible == False):
                possibleWays.remove(possibleWays[possibleWayIndex])
            else:
                possibleWay = possibleWays[possibleWayIndex]
                break
        
        if len(possibleWays) == 0:
            possibleWay = (0, 0)
        
        self.go(self.boardX + possibleWay[0], self.boardY + possibleWay[1])

    def checkMove(self, x, y):
        inBoard = self.boardObject.checkInBoard(x, y)
        isWall = False
        if inBoard and self.boardObject.board[y][x] != None and self.boardObject.board[y][x].getTag()  == "Wall":
            isWall = True 
        return inBoard and (not isWall)