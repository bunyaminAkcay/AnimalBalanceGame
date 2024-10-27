from core.spriteObject import SpriteObject
from core.game import Game
import pygame

class Button(SpriteObject):

    def __init__(self, x, y, width, height, layer, scene, image=None, backgroundColor=..., visibility=True):
        super().__init__(x, y, width, height, layer, image, backgroundColor, visibility)
        self.scene = scene
        #uzerine geldiginde

    def call(self):
        print("Called")
        pass

    def update(self):
        super().update()
        
        mouse_pos = pygame.mouse.get_pos()
        if self.getScreenRect().collidepoint(mouse_pos[0], mouse_pos[1]):
            if Game.mouseClicked[0]:
                Game.mouseClicked[0] = False
                
                self.call()

            

            

