import mainMenu
import level2
from core.game import Game 
import pygame

def main():
    screenSize = (1920, 1080)

    mainManu = mainMenu.getMainMenuScene()
    
    l2 = level2.getLevel()

    game = Game(screenSize, "level2", 60, 60, pygame.FULLSCREEN, (255, 255, 255))
    game.run()


main()