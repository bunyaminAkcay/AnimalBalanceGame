from core.gameObject import GameObject
from skillBox import SkillBox
from core.animation import Animation
from core.spriteObject import SpriteObject

import os
import pygame


class Items(GameObject):

    def __init__(self, xPosition, yPositon, skillBoxSize, space, scene):
        super().__init__()
        self.skillBoxSize = skillBoxSize
        self.skillCount = 5
        self.skillId = 0
        self.skillSprites = []
        self.xPosition = xPosition
        self.yPosition = yPositon
        self.space = space
        for i in range(self.skillCount):

            idleAnimation = Animation( [Items.getImage("İtemBox6.png")], 1000)
            closeAnimation = Animation( [Items.getImage("İtemBox5.png"), Items.getImage("İtemBox4.png"), Items.getImage("İtemBox3.png"), Items.getImage("İtemBox2.png"), Items.getImage("İtemBox1.png")], 200)
            openAnimation = Animation( [Items.getImage("İtemBox1.png"), Items.getImage("İtemBox2.png"), Items.getImage("İtemBox3.png"), Items.getImage("İtemBox4.png"), Items.getImage("İtemBox5.png")], 200)
            skillBox = SkillBox(xPosition, yPositon + i * (space + skillBoxSize[1]), skillBoxSize[0], skillBoxSize[1], 0, [idleAnimation, closeAnimation, openAnimation])
            scene.addGameObject(skillBox)
        skillImages = [Items.getImage("El1.png"), Items.getImage("Duvar2.png"), Items.getImage("Yem.png"), Items.getImage("Zehir.png"), Items.getImage("Kafes.png")]
        for i in range(self.skillCount):
            skillSprite = SpriteObject(xPosition + skillBoxSize[0] * 0.25, yPositon + i * skillBoxSize[1] + skillBoxSize[0] * 0.25, skillBoxSize[0] * 0.5, skillBoxSize[1] * 0.5, -1, skillImages[i])
            scene.addGameObject(skillSprite)
            self.skillSprites.append(skillSprite)

        self.skillBoxEffect = SpriteObject(xPosition , yPositon, skillBoxSize[0] , skillBoxSize[1] , 20, Items.getImage("Effect-1.png"), (0, 0, 0, 0))
        scene.addGameObject(self.skillBoxEffect)
        self.setSkillId(self.skillId)

    @staticmethod
    def getImage(filename):
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "..", "sprites", filename)
        return pygame.image.load(image_path)

    def setSkillId(self, skillId):
        self.skillId = skillId
        y = self.yPosition + self.skillId * (self.space + self.skillBoxSize[1])

        self.skillBoxEffect.y = y 

    def getSkillId(self):
        return self.skillId

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            self.setSkillId(0)
        if keys[pygame.K_2]:
            self.setSkillId(1)
        if keys[pygame.K_3]:
            self.setSkillId(2)
        if keys[pygame.K_4]:
            self.setSkillId(3)
        if keys[pygame.K_5]:
            self.setSkillId(4) 