import pygame

from core.game import Game
from core.scene import Scene
from core.camera import Camera
from core.UIText import UIText
from core.spriteObject import SpriteObject
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
from timer import Timer
from resultScreen import ResultScreen
from button import Button

from eagle import Eagle
from frog import Frog
from snake import Snake

def getLevel2():

    base_path = os.path.dirname(__file__)
    font_path = os.path.join(base_path, "..", "sprites", "Orange_kid.ttf")
    UIText.setFont(font_path)    

    screenSize = (1920, 1080)

    level2Camera = Camera( screenSize[0]//2, screenSize[1]//2, 1) 
    level2 = Scene("level2", level2Camera, (34,32,52))
    level2.addGameObject(level2Camera)

    squareSize = 64
    boardSize = (16, 10)

    boardPosition = ( 500, 300)
        
    room = Box(boardPosition[0] -64, boardPosition[1] -64, 64*18, 64*12, 10, getImage("RuinLevel.png"), (0,0,0,0))
    level2.addGameObject(room)
    
    items = Items(100,50, (192, 192), 0, level2)
    level2.addGameObject(items)

    board = Board(squareSize, boardPosition, boardSize, level2, items)
    level2.addGameObject(board)

    s1 = Snake(0, 1, board, 0)
    level2.addGameObject(s1)
    
    s2 = Snake(1, 0, board, 0)
    level2.addGameObject(s2)

    e1= Eagle(14,9,board,0)
    level2.addGameObject(e1)

    e2= Eagle(15,8,board,0)
    level2.addGameObject(e2)

    f1 = Frog(0,9,board,0)
    level2.addGameObject(f1)

    f2 = Frog(1,8, board, 0)
    level2.addGameObject(f2)

    wallLocations = [(2,3),(2,4), (2,5), (3,3), (3,4), (3,5), (2,6), (3,6),
                     (7,2), (8,2), (9,2), (10,2), (11,2),
                     (7,3), (8,3), (9,3), (10,3), (11,3),
                     (7,6), (8,6), (9,6), (10,6), (11,6),
                     (7,7), (8,7), (9,7), (10,7), (11,7),
                     ]

    for wallLoc in wallLocations:        
        wall = Wall(wallLoc[0], wallLoc[1], board, 2)
        wall.visibility = False
        level2.addGameObject(wall)

    animalTagsInScene = ["Animal.Frog", "Animal.Eagle", "Animal.Snake"]
    barSpace = 100
    barPosition = 1650
    barHeigth = 250

    homeButton = HomeButton(1650, 700, 128, 128, -5, level2, getImage("BackToMenu.png"), (255,255,255,0))
    level2.addGameObject(homeButton)

    barObjects = []

    for i, tag in enumerate(animalTagsInScene):
        bar = Bar(barPosition + i * barSpace, 100, 40, barHeigth, -25, board, tag, level2, None)
        level2.addGameObject(bar)
        barObjects.append(bar)

    balanceLine = SpriteObject(barPosition - 20, 100 + barHeigth * (len(animalTagsInScene)-1)/len(animalTagsInScene), 280, 5, -35, None, (0, 255, 0, 255))
    level2.addGameObject(balanceLine)

    resultScreen = ResultScreen(barObjects, (-820, 230), len(animalTagsInScene), balanceLine, level2, "level2")
    level2.addGameObject(resultScreen)

    timer = Timer( "Timer start", 1650, 390, 96, -20, (255,255,255), 60, board, resultScreen)
    level2.addGameObject(timer)

    return level2

def getImage(filename):
    base_path = os.path.dirname(__file__)
    image_path = os.path.join(base_path, "..", "sprites", filename)
    return pygame.image.load(image_path)


class HomeButton(Button):
    def call(self):
        Game.changeScene("MainMenu")
        lvl1 = getLevel2()
        pygame.mouse.set_visible(True)