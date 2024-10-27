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
from dog import Dog
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
    level1 = Scene("level3", level1Camera, (34,32,52))
    level1.addGameObject(level1Camera)

    squareSize = 64
    boardSize = (16, 12)

    boardPosition = ( 450, 200)
        
    room = Box(boardPosition[0] -64, boardPosition[1] -64, 576*2, 448 *2, 10, getImage("Final-Lab.png"), (0,0,0,0))
    level1.addGameObject(room)
    
    items = Items(100,50, (192, 192), 0, level1)
    level1.addGameObject(items)

    board = Board(squareSize, boardPosition, boardSize, level1, items)
    level1.addGameObject(board)
    
    mouse1= Mouse(15,1,board,0)
    level1.addGameObject(mouse1)

    mouse2= Mouse(15,2,board,0)
    level1.addGameObject(mouse2)

    mouse1= Cat(0,4,board,0)
    level1.addGameObject(mouse1)

    mouse2= Cat(0,5,board,0)
    level1.addGameObject(mouse2)

    dog1 = Dog(15,8,board,0)
    level1.addGameObject(dog1)

    dog2 = Dog(15,9,board,0)
    level1.addGameObject(dog2)


    wallLocations = [(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4),(9,4),(10,4),(11,4),(12,4),(13,4),(14,4),(15,4),
                     (2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5),(11,5),(12,5),(13,5),(14,5),(15,5)]

    for wallLoc in wallLocations:        
        wall = Wall(wallLoc[0], wallLoc[1], board, 2)
        wall.visibility = False
        level1.addGameObject(wall)

    animalTagsInScene = ["Animal.Mouse", "Animal.Cat", "Animal.Dog"]
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

    balanceLine = SpriteObject(barPosition - 20, 100 + barHeigth * (len(animalTagsInScene)-1)/len(animalTagsInScene), 280, 5, -35, None, (0, 255, 0, 255))
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
