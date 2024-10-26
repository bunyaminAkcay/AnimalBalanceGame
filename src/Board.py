from core.gameObject import GameObject
from core.clock import Clock
import pygame
from wall import Wall

class Board(GameObject):
 class MouseEventHandler:

    def __init__(self, squareSize, boardPosition, boardSize, scene, skillItems):
        super().__init__()
        self.squareSize = squareSize
        self.boardPosition = boardPosition
        self.boardSize = boardSize
        self.board = [[None for _ in range(boardSize[0])] for _ in range(boardSize[1])]
        self.clock = Clock(1000)
        self.scene = scene
        self.userWallLocations = []
        self.userWallCount = 10
        self.skillItems = skillItems
        self.holder = None

    def checkInBoard(self, x, y):
        if self.boardSize[0] > x >= 0 and self.boardSize[1] > y >= 0:
            return True
        return False

    def update(self):
        #skill 0: hand


        #if self.skillItems.getSkillId() == 0:

# Mouse event handler sınıfı
        def _init_(self):
            self.dragging = None
            self.offset_x = 0
            self.offset_y = 0

        def handle_event(self, event, game_objects):
            if event.type == pygame.MOUSEBUTTONDOWN:
                for obj in game_objects:
                    if isinstance(obj, Wall) and obj.rect.collidepoint(event.pos):
                    # Wall nesnesi sürüklenmeye başlar
                        self.dragging = obj
                        mouse_x, mouse_y = event.pos
                        self.offset_x = obj.rect.x - mouse_x
                        self.offset_y = obj.rect.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
            # Fare bırakıldığında sürüklemeyi durdur
                self.dragging = None

            elif event.type == pygame.MOUSEMOTION:
            # Sürükleme işlemi
                if self.dragging:
                    mouse_x, mouse_y = event.pos
                    self.dragging.rect.x = mouse_x + self.offset_x
                    self.dragging.rect.y = mouse_y + self.offset_y
                    self.dragging.update_position()

            

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