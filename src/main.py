import pygame

from core.game import Game
from core.scene import Scene
from core.camera import Camera


from box import Box
from Board import Board
from animal import Animal
from wall import Wall
def main():

    

    screenSize = (1920, 1080)


    level1Camera = Camera( screenSize[0]//2, screenSize[1]//2, 1) 
    level1 = Scene("level1", level1Camera)
    level1.addGameObject(level1Camera)

    squareSize = 80
    boardSize = (5, 5)

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
    
    board = Board(squareSize, boardPosition, boardSize)
    level1.addGameObject(board)

    animal = Animal(0, 0, board, 1, None, (0,0,0,255))
    level1.addGameObject(animal)

    wall1 = Wall(0, 1, board, 2, None, (255,255,255,255))
    level1.addGameObject(wall1)

    game = Game(screenSize, "level1", 60, 120, pygame.FULLSCREEN, (255, 255, 255))
    game.run()


    pass


main()