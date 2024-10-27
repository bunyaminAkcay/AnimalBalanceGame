from core.spriteObject import SpriteObject
import os
import pygame


class Bar(SpriteObject):

    def __init__(self, x, y, width, height, layer, board, targetTag, scene,  visibility=True):
        base_path = os.path.dirname(__file__)
        bar_image_path = os.path.join(base_path, "..", "sprites", "Bar.png")
            
        barImage = pygame.image.load(bar_image_path)

        super().__init__(x, y, width, height, layer, None, (255,0,0,255), visibility)
        self.board = board
        self.targetTag = targetTag
        self.maxBarSize = height
        self.scene = scene
        self.allAnimalTags = ["Animal.Mouse", "Animal.Cat", "Animal.Dog", "Animal.Frog", "Animal.Snake", "Animal.Eagle"]
        self.ratio = 0.5
        
        self.backgroundSprite = SpriteObject(x, y, width, height, -25, barImage)
        self.scene.addGameObject(self.backgroundSprite)

        tagList = targetTag.split(".")

        self.animalSprite = SpriteObject(x -12, y + height -40, 64, 64, -30, Bar.getImage(tagList[1] + ".png"))
        self.scene.addGameObject(self.animalSprite)

    @staticmethod
    def getImage(filename):
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "..", "sprites", filename)
        return pygame.image.load(image_path)

    def init(self):
        self.initialX = self.x
        self.initialY = self.y
    

    def update(self):
        if self.board.stop:
            return
        # boarddaki o tagdaki hayvanları sayself
        # board daki tüm hayvanları say
        # oranı bul
        # x, y, w, h değiştir
        targetTagCount = 0
        totalAnimalCount = 0

        boardSize = self.board.boardSize
        for j in range(boardSize[1]):
            for i in range(boardSize[0]):
                    if self.board.board[j][i] == None:
                        continue
                    t = self.board.board[j][i].getTag()
                    if self.targetTag == t:
                        targetTagCount +=1
                        totalAnimalCount +=1
                    elif t in self.allAnimalTags:
                        totalAnimalCount +=1
                        
        
        self.ratio = targetTagCount/(totalAnimalCount + 0.0001)
        self.changeHeightByRatio(self.ratio)
        
    
    def changeHeightByRatio(self, ratio):
        self.height = self.maxBarSize * ratio   

        self.y = self.initialY + self.maxBarSize - self.height
        self._updateScale(1)

    #get close %5 ratio to ratio and give a ceza point
    def reduceToBalance( self, wantedRatio, barCount):
        adjustment = 0.01  # Smaller adjustment step to move gradually toward the target ratio
        
        if self.ratio - wantedRatio >= adjustment:
            self.ratio -= adjustment
            penalty = adjustment * 1000
        elif wantedRatio - self.ratio >= adjustment:
            self.ratio += adjustment
            penalty = adjustment * 1000
        else:
            # Set ratio exactly to target once within range
            self.ratio = wantedRatio
            penalty = abs(self.ratio - wantedRatio) * 1000
            self.changeHeightByRatio(self.ratio)
            return True, penalty
        
        penalty *= barCount
        # Update height based on the adjusted ratio
        self.changeHeightByRatio(self.ratio)
        return False, penalty
