from core.scene import Scene
from core.camera import Camera
from button import Button
from core.UIText import UIText
from core.game import Game
import os
from core.spriteObject import SpriteObject
import pygame

def getImage(filename):
    base_path = os.path.dirname(__file__)
    image_path = os.path.join(base_path, "..", "sprites", filename)
    return pygame.image.load(image_path)


def getMainMenuScene():
    
   
    base_path = os.path.dirname(__file__)
    font_path = os.path.join(base_path, "..", "sprites", "Orange_kid.ttf")
    UIText.setFont(font_path)    

    screenSize = (1920, 1080)

    camera = Camera( screenSize[0]//2, screenSize[1]//2, 1) 
    mainMenu = Scene("MainMenu", camera)
    mainMenu.addGameObject(camera)

    playButton = PlayButton(960-100, 540-50, 250, 100, 0, mainMenu, None, (0,0,0,255))
    mainMenu.addGameObject(playButton)

    playText = UIText("      Play", 960-100, 540-50, 64, -1, (255,255,255))
    mainMenu.addGameObject(playText)

    settingsButton=SettingsButton(1790,10,100,100,0, mainMenu, getImage("Settings.png"),(0,255,0,0)) 
    mainMenu.addGameObject(settingsButton)

    quitButton=QuitButton(0,0,200,200,0,mainMenu,getImage("Close.png"),(0,0,0,0) )
    mainMenu.addGameObject(quitButton)

    background=SpriteObject(0,0,1920,1080, 100, getImage("Background.png"))
    mainMenu.addGameObject(background)

    return mainMenu

class PlayButton(Button):

    def call(self):
        Game.changeScene("levelScene")


class SettingsButton(Button):
    def call(self):
        Game.changeScene("Settings")
class QuitButton(Button):
    def call(self):
        pygame.quit()