from core.gameObject import GameObject
from skillBox import SkillBox
from core.animation import Animation
from core.spriteObject import SpriteObject
from core.animatedObject import AnimatedObject

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
        self.handSize = 48

        self.skillActivity = [True] * 5 

        handAnimation = Animation([Items.getImage("El1.png"), Items.getImage("El2.png"), Items.getImage("El3.png"), Items.getImage("El4.png"), Items.getImage("El5.png")], 100)
        wallAnimation = Animation([Items.getImage('Duvar2.png')], 1000)
        yemAnimation = Animation([Items.getImage('Yem.png')], 1000)
        posionAnimation = Animation([Items.getImage('Zehir.png')], 1000)
        kafesAnimation = Animation([Items.getImage('Kafes.png')], 1000)

        cursorAnimationList = [handAnimation, wallAnimation, yemAnimation, posionAnimation, kafesAnimation]
        self.hand = AnimatedObject(0,0, self.handSize, self.handSize, -100, cursorAnimationList)
        scene.addGameObject(self.hand)
        self.skillBoxes = []
        for i in range(self.skillCount):

            idleAnimation = Animation( [Items.getImage("İtemBox6.png")], 1000)
            closeAnimation = Animation( [Items.getImage("İtemBox5.png"), Items.getImage("İtemBox4.png"), Items.getImage("İtemBox3.png"), Items.getImage("İtemBox2.png"), Items.getImage("İtemBox1.png")], 200, False)
            openAnimation = Animation( [Items.getImage("İtemBox1.png"), Items.getImage("İtemBox2.png"), Items.getImage("İtemBox3.png"), Items.getImage("İtemBox4.png"), Items.getImage("İtemBox5.png")], 200)
            skillBox = SkillBox(xPosition, yPositon + i * (space + skillBoxSize[1]), skillBoxSize[0], skillBoxSize[1], 0, [idleAnimation, closeAnimation, openAnimation])
            scene.addGameObject(skillBox)
            self.skillBoxes.append(skillBox)
        skillImages = [Items.getImage("El1.png"), Items.getImage("Duvar2.png"), Items.getImage("Yem.png"), Items.getImage("Zehir.png"), Items.getImage("Kafes.png")]
        
        for i in range(self.skillCount):
            skillSprite = SpriteObject(xPosition + skillBoxSize[0] * 0.25, yPositon + i * skillBoxSize[1] + skillBoxSize[0] * 0.25, skillBoxSize[0] * 0.5, skillBoxSize[1] * 0.5, -1, skillImages[i])
            scene.addGameObject(skillSprite)
            self.skillSprites.append(skillSprite)

        self.skillBoxEffect = SpriteObject(xPosition , yPositon, skillBoxSize[0] , skillBoxSize[1] , 20, Items.getImage("Effect-1.png"), (0, 0, 0, 0))
        scene.addGameObject(self.skillBoxEffect)
        self.setSkillId(self.skillId)
        
    def init(self):
        pygame.mouse.set_visible(False)
        return super().init()
    
    @staticmethod
    def getImage(filename):
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "..", "sprites", filename)
        return pygame.image.load(image_path)

    def setSkillId(self, skillId):
        if self.skillActivity[skillId] == False:
            return
        self.skillId = skillId
        y = self.yPosition + self.skillId * (self.space + self.skillBoxSize[1])

        self.skillBoxEffect.y = y 

    def getSkillId(self):
        return self.skillId

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        self.hand.x = mouse_pos[0] - self.handSize//2
        self.hand.y = mouse_pos[1] - self.handSize//2

        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            self.setSkillId(0)
            self.hand.currentAnimationIndex = 0
        if keys[pygame.K_2]:
            self.setSkillId(1)
            self.hand.currentAnimationIndex = 1
        if keys[pygame.K_3]:
            self.setSkillId(2)
            self.hand.currentAnimationIndex = 2
        if keys[pygame.K_4]:
            self.setSkillId(3)
            self.hand.currentAnimationIndex = 3
        if keys[pygame.K_5]:
            self.setSkillId(4) 
            self.hand.currentAnimationIndex = 4
    
    def closeSkill(self, id):
        print(id)
        self.skillBoxes[id].currentAnimationIndex = 1
        self.skillBoxes[id].animationList[1].clear()
        self.skillSprites[id].visibility = False
        self.setSkillId(0)
        self.hand.currentAnimationIndex = 0
        self.skillActivity[id] = False