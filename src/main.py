import pygame

from core.game import Game
from core.scene import Scene
from core.camera import Camera
import os


from box import Box
from Board import Board
from animal import Animal
from wall import Wall
from cat import Cat
from mouse import Mouse
from bar import Bar
from skillBox import SkillBox
from items import Items

def main():

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

    board = Board(squareSize, boardPosition, boardSize, level1, items)
    level1.addGameObject(board)

    cat1 = Cat(3, 3, board, 0)
    level1.addGameObject(cat1)
    
    cat2 = Cat(3, 5, board, 0)
    level1.addGameObject(cat2)

    mouse1= Mouse(3,6,board,0)
    level1.addGameObject(mouse1)

    mouse2= Mouse(3,0,board,0)
    level1.addGameObject(mouse2)

    wall1 = Wall(0, 1, board, 2)
    level1.addGameObject(wall1)


    animalTagsInScene = ["Animal.Mouse", "Animal.Cat"]
    barSpace = 100
    barPosition = 1600
    for i, tag in enumerate(animalTagsInScene):
        bar = Bar(barPosition + i * barSpace, 100, 40, 250, 99, board, tag, level1, None)
            
        level1.addGameObject(bar)

    game = Game(screenSize, "level1", 60, 60, pygame.FULLSCREEN, (255, 255, 255))
    game.run()

    
    pass


main()


