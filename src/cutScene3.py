from core.scene import Scene
from core.camera import Camera
from button import Button
from core.UIText import UIText
from core.game import Game
import os
from core.spriteObject import SpriteObject
from core.clock import Clock
from core.gameObject import GameObject
import pygame


def getImage(filename):
    base_path = os.path.dirname(__file__)
    image_path = os.path.join(base_path, "..", "sprites", filename)
    return pygame.image.load(image_path)


def getCutScene():
    
    base_path = os.path.dirname(__file__)
    font_path = os.path.join(base_path, "..", "sprites", "Orange_kid.ttf")
    UIText.setFont(font_path)

    screenSize = (1920, 1080)

    camera = Camera( screenSize[0]//2, screenSize[1]//2, 1) 
    cutScene = Scene("cutScene3", camera)
    cutScene.addGameObject(camera)
    background2=SpriteObject(480,50,960,540, 100, getImage("Sprite-0014.png"),(0,0,0))
    cutScene.addGameObject(background2)

    clock2 = Clock2()
    cutScene.addGameObject(clock2)

    texts = ["Ben: Bu kadar tür olduğunu bilmiyordum",
             "Raporladıktan sonra AI kesin özgürlüğümü vericek İnşallah",
             "Bir süre sonra",
             "AI: Gerçekten fevkalade efendim",
             "Ben: Estağfirullah verilmiş sadakamız varmış",
             "AI: Bahçedeki dengeyi sağla ve özgürsün",
             "Bir süre sonra",
             "???: Hey!",
             "Ben: Merhaba bayan robot böyle bayan başınıza geziyorsunuz",
             "Bayan Robot: Ayol yardım et",
             "Son için bölümden sonra ayarlara gir"]

    for i, t in enumerate(texts):

        textI=UIText(t, 700,500 + i * 32,30,10,(255,255,255,255),None)
        cutScene.addGameObject(textI)



class Clock2(GameObject):

    def __init__(self):
        super().__init__()
        self.clock = Clock(25000)

    def update(self):
        if self.clock.getTicks() > 0:
            Game.changeScene("level3")


