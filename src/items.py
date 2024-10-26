from core.gameObject import GameObject
from skillBox import SkillBox
from core.animation import Animation

import os
import pygame


class Items(GameObject):

    def __init__(self, xPosition, yPositon, skillBoxSize, space, scene):
        super().__init__()
        self.skillBoxSize = skillBoxSize
        self.skillCount = 5
        self.skillId = 0
        self.activeSkillList = [True] * 5
        self.xPosition = xPosition
        self.yPosition = yPositon
        for i in range(self.skillCount):

            idleAnimation = Animation( [Items.getImage("İtemBox6.png")], 1000)
            closeAnimation = Animation( [Items.getImage("İtemBox5.png"), Items.getImage("İtemBox4.png"), Items.getImage("İtemBox3.png"), Items.getImage("İtemBox2.png"), Items.getImage("İtemBox1.png")], 200)
            openAnimation = Animation( [Items.getImage("İtemBox1.png"), Items.getImage("İtemBox2.png"), Items.getImage("İtemBox3.png"), Items.getImage("İtemBox4.png"), Items.getImage("İtemBox5.png")], 200)
            skillBox = SkillBox(xPosition, yPositon + i * (space + skillBoxSize[1]), skillBoxSize[0], skillBoxSize[1], 0, [idleAnimation, closeAnimation, openAnimation])
            scene.addGameObject(skillBox)
        

    @staticmethod
    def getImage(filename):
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "..", "sprites", filename)
        return pygame.image.load(image_path)

    
    def update(self):
        if pygame.key.get_pressed("1"):
            self.skillId = 0
        elif pygame.key.get_pressed("2"):
            self.skillId = 1
        elif pygame.key.get_pressed("3"):
            self.skillId = 2 
        elif pygame.key.get_pressed("4"):
            self.skillId = 3      
        pass