import mainMenu
import level1
import level2
import level3

from core.game import Game 
import pygame
import Settings
import cutScene
import levelScene
import cutScene2
import cutScene3

def main():
    screenSize = (1920, 1080)

    mainManu = mainMenu.getMainMenuScene()
    
    l1 = level1.getLevel1()
    l2 = level2.getLevel2()
    l3 = level3.getLevel3()
    settings= Settings.getSettingsScene()

    CutScene1 = cutScene.getCutScene()
    CutScene2 = cutScene2.getCutScene()
    CutScene3 = cutScene3.getCutScene()

    lvlScene= levelScene.getlevelScene()

    game = Game(screenSize, "MainMenu", 60, 60, pygame.FULLSCREEN)
    game.run()


main()