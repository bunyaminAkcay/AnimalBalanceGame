from core.gameObject import GameObject
from core.clock import Clock
from core.game import Game
import pygame


class Board(GameObject): 

    def __init__(self, squareSize, boardPosition, boardSize, scene, skillItems):
        super().__init__()
        self.squareSize = squareSize
        self.boardPosition = boardPosition
        self.boardSize = boardSize
        self.board = [[None for _ in range(boardSize[0])] for _ in range(boardSize[1])]
        self.clock = Clock(100)
        self.scene = scene
        self.userWalls = []
        self.userWallCount = 10
        self.skillItems = skillItems
        self.holder = [None for _ in range(1)]


    def checkInBoard(self, x, y):
        if self.boardSize[0] > x >= 0 and self.boardSize[1] > y >= 0:
            return True
        return False


    def getCoordsFromMousePosition(self, mouse_pos):
        relativeMousePos = (mouse_pos[0] - self.boardPosition[0], mouse_pos[1] - self.boardPosition[1])
        coords = (relativeMousePos[0]//self.squareSize, relativeMousePos[1]//self.squareSize)
        return (self.checkInBoard(coords[0], coords[1])), coords

    def update(self):
        
        mouse_pos = pygame.mouse.get_pos()

        if self.skillItems.getSkillId() == 0:
            if self.holder[0] != None:
                self.holder[0].visibility = True
                self.holder[0].x = mouse_pos[0]
                self.holder[0].y = mouse_pos[1]
        else:
            if self.holder[0] != None:
                self.holder[0].visibility = False

                      
        if Game.mouseClicked[0]:
            Game.mouseClicked[0] = False
            # Get mouse position
            
            isInBoard, coord = self.getCoordsFromMousePosition(mouse_pos)
            
            #hand
            if isInBoard:
                if self.skillItems.getSkillId() == 0:
                    if self.holder[0] == None:
                        
                        gameObject = self.board[coord[1]][coord[0]]
                        if gameObject != None:
                            tagList = gameObject.getTag().split(".")
                            if len(tagList) > 0 and tagList[0] == "Animal":
                                #clicked an animal
                                temp = self.board[coord[1]][coord[0]]
                                self.board[coord[1]][coord[0]] = self.holder[0]
                                self.holder[0] = temp

                    elif self.holder[0] != None:
                        if isInBoard and self.board[coord[1]][coord[0]] == None:
                            self.board[coord[1]][coord[0]] = self.holder[0]
                            self.holder[0] = None
                            self.board[coord[1]][coord[0]].go(coord[0], coord[1])
                            
                elif self.skillItems.getSkillId() == 1:
                    if(isInBoard):
                        self.addUserWall(coord[0], coord[1])
        

        if self.clock.getTicks() > 0:
            

            for y, row in enumerate(self.board):
                    for x, boardObject in enumerate(row):
                        if boardObject == None:
                            continue
                        boardObject.move()


    #if user wall added return true otherwise return false
    
    def addUserWall(self, x ,y):
        from userWall import UserWall
        if self.board[y][x] != None:
            return False       
        userWall = UserWall(x, y, self, 0)
        self.scene.addGameObject(userWall)
        self.board[y][x] = userWall
        self.userWalls.append(userWall)

        for wall in self.userWalls:
            wall.reduceLifeTime()

        #check user walls
        for i, go in enumerate(self.userWalls):
            if go.lifetime < 0:
                #remove wall
                
                self.board[go.boardY][go.boardX].x = -100
                self.board[go.boardY][go.boardX] = None
                self.userWalls[i] = None
        
        self.userWalls = [x for x in self.userWalls if x is not None]

        return True
        