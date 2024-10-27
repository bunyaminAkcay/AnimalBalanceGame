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


def getSettingsScene():
    
    base_path = os.path.dirname(__file__)
    font_path = os.path.join(base_path, "..", "sprites", "Orange_kid.ttf")
    UIText.setFont(font_path)    

    screenSize = (1920, 1080)
    
    camera = Camera( screenSize[0]//2, screenSize[1]//2, 1) 
    settings = Scene("Settings", camera,(255,255,255,255))
    settings.addGameObject(camera)
    text=UIText("Sadece Ölüler Görür.",920,540,50,10,(0,0,0))
    settings.addGameObject(text)

    backButton=BackButton(120,10,60,60,10,settings,None,(0,255,0,255))
    settings.addGameObject(backButton)
    background_sts=SpriteObject(0,0,1920,1080,-5,getImage("Sprite-0017.png"))
    settings.addGameObject(background_sts)



class BackButton(Button):
    def call(self):
        Game.changeScene("MainMenu")