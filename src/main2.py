from core.camera import Camera
from core.scene import Scene
from core.game import Game
from core.gameObject import GameObject
from core.UIText import UIText
from box import Box
from items import Items
import pygame

import os



def main():
    base_path = os.path.dirname(__file__)
    font_path = os.path.join(base_path, "..", "sprites", "Orange_kid.ttf")
    UIText.setFont(font_path)    

    screenSize = (1920, 1080)

    level1Camera = Camera( screenSize[0]//2, screenSize[1]//2, 1) 
    level1 = Scene("level1", level1Camera)
    level1.addGameObject(level1Camera)


    squareSize = 64
    boardSize = (17, 14)

    boardPosition = ( 420, 100)
        
        
    for j in range(boardSize[1]):
            for i in range(boardSize[0]):
                boxX = boardPosition[0] + i * squareSize
                boxY = boardPosition[1] + j * squareSize
                colorType = (i+j) % 2
                color = (255, 255, 0)
                if colorType == 1:
                    color = (255, 125, 0)

                b = Box(boxX, boxY, squareSize, squareSize, 10, None, color)
                level1.addGameObject(b)
        
    items = Items(100,50, (192, 192), 0, level1)
    level1.addGameObject(items)









    game = Game(screenSize, "level1", 60, 60, pygame.FULLSCREEN, (200, 90, 150))
    game.run()


main()