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
        self.allAnimalTags = ["Animal.Mouse", "Animal.Cat", "Animal.Dog"]
        
        backgroundSprite = SpriteObject(x, y, width, height, -1, barImage)
        self.scene.addGameObject(backgroundSprite)

    def init(self):
        self.initialX = self.x
        self.initialY = self.y
    

    def update(self):
        # boarddaki o tagdaki hayvanları say
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
                        
        
        ratio = targetTagCount/(totalAnimalCount + 0.1)
        print(ratio)
        self.height = self.maxBarSize * ratio   

        self.y = self.initialY + self.maxBarSize - self.height
        self._updateScale(1)
             