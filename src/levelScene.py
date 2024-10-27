from core.scene import Scene
from core.camera import Camera
from button import Button
from core.UIText import UIText
from core.game import Game
import os
from core.spriteObject import SpriteObject
from core.clock import Clock
from core.gameObject import GameObject
from button import Button
from core.UIText import UIText
import pygame


def getImage(filename):
    base_path = os.path.dirname(__file__)
    image_path = os.path.join(base_path, "..", "sprites", filename)
    return pygame.image.load(image_path)


def getlevelScene():
    
    base_path = os.path.dirname(__file__)
    font_path = os.path.join(base_path, "..", "sprites", "Orange_kid.ttf")
    UIText.setFont(font_path)

    screenSize = (1920, 1080)

    camera = Camera( screenSize[0]//2, screenSize[1]//2, 1) 
    levelScene = Scene("levelScene", camera, (255,255,255))
    levelScene.addGameObject(camera)
    
    background = SpriteObject(0, 0, 1920, 1080, 0, getImage("Settings-Bg.png"))
    levelScene.addGameObject(background)

    level1Button = Level1Button(300, 340, 400, 400, -1, levelScene, getImage("Level.png"), (0,0,0,0))
    levelScene.addGameObject(level1Button)

    level1Text = UIText("1", 480, 430, 144, -25, (255,255,255))
    levelScene.addGameObject(level1Text)

    level2Button = Level2Button(760, 340, 400, 400, -1, levelScene, getImage("Level.png"), (0,0,0,0))
    levelScene.addGameObject(level2Button)

    level2Text = UIText("2", 480 + 460, 430, 144, -25, (255,255,255))
    levelScene.addGameObject(level2Text)

    level3Button = Level3Button(1220, 340, 400, 400, -1, levelScene, getImage("Level.png"), (0,0,0,0))
    levelScene.addGameObject(level3Button)

    level3Text = UIText("3", 480 + 2* 460, 430, 144, -25, (255,255,255))
    levelScene.addGameObject(level3Text)

    return levelScene


class Level1Button(Button):

    def call(self):
        import cutScene
        c = cutScene.getCutScene()
        Game.changeScene("cutScene")

class Level2Button(Button):

    def call(self):
        import cutScene2
        c = cutScene2.getCutScene()
        Game.changeScene("cutScene2")

class Level3Button(Button):

    def call(self):
        import cutScene3
        c = cutScene3.getCutScene()
        Game.changeScene("cutScene3")


