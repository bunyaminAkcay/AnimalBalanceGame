import random

from boardObject import BoardObject

class Animal(BoardObject):

    def __init__(self, boardX, boardY, boardObject, layer, image=None, backgroundColor=..., visibility=True):
        super().__init__(boardX, boardY, boardObject, layer, image, backgroundColor, visibility)
        self.targetAnimalTag = ""
        self.enemyAnimalTag = ""
        self.birthChance = 0

    def move(self):
        initialPosition = (self.boardX, self.boardY)

        possibleWays = [ (1, 0), (-1,0), (0, 1), (0,-1)]
        possibleWay = None

        yemLocation = None
        for way in possibleWays:
            if self.checkYem(initialPosition[0] + way[0], initialPosition[1] + way[1]):
                yemLocation = (initialPosition[0] + way[0], initialPosition[1] + way[1])
                break
        

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
        
        isTarget = self.checkTarget(self.boardX + possibleWay[0], self.boardY + possibleWay[1])

        #target mı?
        #targetsa targetı yok et
        #kavga animasyonu

        if isTarget:
            targetAnimal = self.boardObject.board[self.boardY + possibleWay[1]][self.boardX + possibleWay[0]]

            targetAnimal.x = -100
            self.boardObject.board[self.boardY + possibleWay[1]][self.boardX + possibleWay[0]] = None

        if(yemLocation != None):
            self.boardObject.board[yemLocation[1]][yemLocation[0]].x = -100
            self.boardObject.board[yemLocation[1]][yemLocation[0]] = None
            self.go(yemLocation[0], yemLocation[1])
        else:
            self.go(self.boardX + possibleWay[0], self.boardY + possibleWay[1])

        randomNumber = random.random()
        if possibleWay != (0, 0) and randomNumber > (1-self.birthChance):
            self.createNewAnimal(initialPosition)



    def createNewAnimal(self, position):
        newMouse = self.__class__(position[0], position[1], self.boardObject, self._layer)
        newMouse.init()
        self.boardObject.scene.addGameObject(newMouse)
        self.boardObject.board[position[1]][position[0]] = newMouse
        
        
    def checkMove(self, x, y):
        inBoard = self.boardObject.checkInBoard(x, y)
        isWall = False
        if inBoard and self.boardObject.board[y][x] != None and self.boardObject.board[y][x].getTag() in ["Wall", "UserWall", "Kafes"]:
            isWall = True

        if self.checkTarget(x,y):
            return True

        isAnimal = False
        
        tagList = []
        if inBoard and self.boardObject.board[y][x] != None:
            tagList = self.boardObject.board[y][x].getTag().split(".")

        if inBoard and len(tagList) > 0 and tagList[0] == "Animal":
            isAnimal = True

        return inBoard and (not isWall) and (not isAnimal)
    
    def checkTarget(self, x, y):
    
        inBoard = self.boardObject.checkInBoard(x, y)
        if inBoard and self.boardObject.board[y][x] != None and self.boardObject.board[y][x].getTag() == self.targetAnimalTag:
            return True
        return False
    
    def checkYem(self, x, y):
        inBoard = self.boardObject.checkInBoard(x, y)
        if inBoard and self.boardObject.board[y][x] != None and self.boardObject.board[y][x].getTag() == "Yem":
            return True
        return False