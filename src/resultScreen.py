from core.gameObject import GameObject
from core.spriteObject import SpriteObject
from core.UIText import UIText
from core.clock import Clock
import os
import pygame
from core.UIText import UIText
from core.game import Game

from button import Button


class ResultScreen(GameObject):

    def __init__(self, bars, barOffset, barCount, balanceLine, scene, levelTag):
        self.bars = bars
        self.barOffset = barOffset
        self.scene = scene
        self.reportSprite = SpriteObject(720, 135, 320 * 1.5, 540 * 1.5, -10, ResultScreen.getImage("Rapor.png"))
        self.scene.addGameObject(self.reportSprite)
        self.reportSprite.visibility = False
        self.moved = False
        self.reportText = UIText("Report", 885, 165, 80, -40, (255, 255, 255, 255))
        self.reportText.visibility = False
        self.scene.addGameObject(self.reportText)
        self.barCount = barCount
        self.balanceLine = balanceLine
        self.clock = Clock(100)
        self.showedResult = False
        self.point = 1000 * barCount
        self.pointCalculated = False
        self.scoreText = UIText("", 880, 625, 64, -40, (0,0,0,255))
        self.scene.addGameObject(self.scoreText)
        
        self.buttonReload=ReloadButton(800,755,150,150,-50, self.scene, levelTag, ResultScreen.getImage("Replay.png"),(0,0,0,0))
        self.scene.addGameObject(self.buttonReload)
        self.buttonReload.visibility = False
        
        self.buttonNextlevel=LevelButton(970,755,150,150,-50, self.scene, ResultScreen.getImage("Start.png"),(0,0,0,0))
        self.scene.addGameObject(self.buttonNextlevel)
        self.buttonNextlevel.visibility=False
        
        self.GameWin=UIText("YOU WIN!",880,700,32,-50,(255,255,255,255))
        self.GameWin.visibility=False
        self.scene.addGameObject(self.GameWin)
        
        self.GameOver=UIText("YOU LOST!",880,700,32,-50,(255,255,255,255))
        self.GameOver.visibility=False
        self.scene.addGameObject(self.GameOver)
       
        #UIText
        super().__init__()
    
    def moveBars(self):
        for i in range(self.barCount):
            self.bars[i].x += self.barOffset[0]
            self.bars[i].y += self.barOffset[1]

            self.bars[i].backgroundSprite.x += self.barOffset[0]
            self.bars[i].backgroundSprite.y += self.barOffset[1]

            self.bars[i].animalSprite.x += self.barOffset[0]
            self.bars[i].animalSprite.y += self.barOffset[1]

            self.bars[i].initialX += self.barOffset[0]
            self.bars[i].initialY += self.barOffset[1]
            
        
        self.balanceLine.x += self.barOffset[0]
        self.balanceLine.y += self.barOffset[1]

    def update(self):
        if self.showedResult:
            if self.clock.getTicks() > 0 and not self.pointCalculated:
                
                calculatedForAllBars = True
                for bar in self.bars:
                    
                    isEnd, reducePoint = bar.reduceToBalance(float(1/self.barCount), self.barCount)
                    if not isEnd:
                        calculatedForAllBars = False

                    self.point -= reducePoint
                    if self.point < 0:
                        self.point = 0
                self.pointCalculated = calculatedForAllBars
                self.scoreText.setText(str(self.point))


    def checkButtonClicks(self):
        # Check if buttons are clicked
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:  # Left-click
            if self.buttonReload.visibility and self.buttonReload.rect.collidepoint(mouse_pos):
                self.onReloadClick()
            elif self.buttonNextlevel.visibility and self.buttonNextlevel.rect.collidepoint(mouse_pos):
                self.onNextLevelClick()

    def onReloadClick(self):
        print("Reload button clicked!")
        # Add functionality for reloading the level

    def onNextLevelClick(self):
        print("Next level button clicked!")
        # Add functionality for moving to the next level

    def showResults(self):
        self.reportSprite.visibility = True
        self.reportText.visibility = True
        
        self.buttonReload.visibility = True
        self.buttonNextlevel.visibility = True

        if self.moved == False:
            self.moveBars()
            self.moved = True
        
        everyAnimalExist = True
        for bar in self.bars:
            if bar.ratio <= 0:
                everyAnimalExist = False 

        if everyAnimalExist:
            self.GameWin.visibility=True
            
            
        else:
            self.GameOver.visibility=True
          
            #lose
            

        self.showedResult = True
        #self.clock.clear()
    
    

    @staticmethod
    def getImage(filename):
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "..", "sprites", filename)
        return pygame.image.load(image_path)



class ReloadButton(Button):

    def __init__(self, x, y, width, height, layer, scene, levelTag, image=None, backgroundColor=..., visibility=True):
        super().__init__(x, y, width, height, layer, scene, image, backgroundColor, visibility)
        self.levelTag = levelTag

    def call(self):

        if self.levelTag == "level1":
            import level1
            lvl1 = level1.getLevel1()
        if self.levelTag == "level2":
            import level2
            lvl2 = level2.getLevel1()
        if self.levelTag == "level3":
            import level3
            lvl3 = level3.getLevel1()

        Game.changeScene(self.levelTag)

class LevelButton(Button):

    def call(self):
        print("levelScene")