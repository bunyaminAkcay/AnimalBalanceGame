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


def getLevel3():

    base_path = os.path.dirname(__file__)
    font_path = os.path.join(base_path, "..", "sprites", "Orange_kid.ttf")
    UIText.setFont(font_path)    

    screenSize = (1920, 1080)

    level1Camera = Camera( screenSize[0]//2, screenSize[1]//2, 1) 
    level1 = Scene("level1", level1Camera, (34,32,52))
    level1.addGameObject(level1Camera)

    squareSize = 64
    boardSize = (18, 16)

    boardPosition = ( 364, 25)
        
    room = Box(boardPosition[0] -64, boardPosition[1] -64, 1344, 1152, 10, getImage("Room1.png"), (0,0,0,0))
    level1.addGameObject(room)
    
    items = Items(100,50, (192, 192), 0, level1)
    level1.addGameObject(items)

    board = Board(squareSize, boardPosition, boardSize, level1, items)
    level1.addGameObject(board)

    cat1 = Cat(13, 2, board, 0)
    level1.addGameObject(cat1)
    
    cat2 = Cat(5, 13, board, 0)
    level1.addGameObject(cat2)

    mouse1= Mouse(5,2,board,0)
    level1.addGameObject(mouse1)

    mouse2= Mouse(13,13,board,0)
    level1.addGameObject(mouse2)



    wallLocations = [(2,4), (3,4), (4,4), (5,4), (2, 5), (3, 5), (4, 5), (5,5),
                     (13,4), (14,4), (15,4), (16,4),(13,5), (14,5), (15,5), (16,5),
                     (2,10), (3,10), (4,10), (5,10), (2, 11), (3, 11), (4, 11), (5,11),
                     (13,10), (14,10), (15,10), (16,10),(13,11), (14,11), (15,11), (16,11)]

    for wallLoc in wallLocations:        
        wall = Wall(wallLoc[0], wallLoc[1], board, 2)
        wall.visibility = False
        level1.addGameObject(wall)

    animalTagsInScene = ["Animal.Mouse", "Animal.Cat"]
    barSpace = 100
    barPosition = 1650
    barHeigth = 250

    homeButton = HomeButton(1650, 700, 128, 128, -5, level1, getImage("BackToMenu.png"), (255,255,255,0))
    level1.addGameObject(homeButton)
    

    barObjects = []

    for i, tag in enumerate(animalTagsInScene):
        bar = Bar(barPosition + i * barSpace, 100, 40, barHeigth, -25, board, tag, level1, None)
        level1.addGameObject(bar)
        barObjects.append(bar)

    balanceLine = SpriteObject(barPosition - 20, 100 + barHeigth * (len(animalTagsInScene)-1)/len(animalTagsInScene), 180, 5, -35, None, (0, 255, 0, 255))
    level1.addGameObject(balanceLine)

    resultScreen = ResultScreen(barObjects, (-820, 230), len(animalTagsInScene), balanceLine,level1, "level1")
    level1.addGameObject(resultScreen)

    timer = Timer( "Timer start", 1650, 390, 96, -20, (255,255,255), 60, board, resultScreen)
    level1.addGameObject(timer)

    return level1

def getImage(filename):
    base_path = os.path.dirname(__file__)
    image_path = os.path.join(base_path, "..", "sprites", filename)
    return pygame.image.load(image_path)


class HomeButton(Button):
    def call(self):
        Game.changeScene("MainMenu")
        lvl1 = getLevel3()
        pygame.mouse.set_visible(True)