from core.gameObject import GameObject
from core.spriteObject import SpriteObject
from core.UIText import UIText
import os
import pygame

class ResultScreen(GameObject):

    def __init__(self, bars, barOffset, scene):
        self.bars = bars
        self.barOffset = barOffset
        self.scene = scene
        self.reportSprite = SpriteObject(720, 135, 320 * 1.5, 540 * 1.5, -10, ResultScreen.getImage("Rapor.png"))
        self.scene.addGameObject(self.reportSprite)
        self.reportSprite.visibility = False
        self.moved = False
        self.reportText = UIText("Report", 885, 165, 64, -40, (255, 255, 255, 255))
        self.reportText.visibility = False
        self.scene.addGameObject(self.reportText)
        super().__init__()
    
    def moveBars(self):
        for i in self.bars:
            i.x += self.barOffset[0]
            i.y += self.barOffset[1]

    def showResults(self):
        self.reportSprite.visibility = True
        self.reportText.visibility = True
        if self.moved == False:
            self.moveBars()
            self.moved = True
        pass

    @staticmethod
    def getImage(filename):
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "..", "sprites", filename)
        return pygame.image.load(image_path)
