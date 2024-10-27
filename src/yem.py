from boardObject import BoardObject
import os
import pygame

class Yem(BoardObject):
    
    count = [30]
    def __init__(self, boardX, boardY, boardObject, layer, visibility=True):
        base_path = os.path.dirname(__file__)
        yem_image_path = os.path.join(base_path, "..", "sprites", "Yem.png")
        yem_Image = pygame.image.load(yem_image_path)
        super().__init__(boardX, boardY, boardObject, layer, yem_Image, (0,0,0,0), visibility)
        self.setTag("Yem")    
    

    def move(self):
        pass


    def use(self):
        print("yem")
        self.count[0] -= 1
        
        if self.count[0] == 0:
            
            self.boardObject.skillItems.closeSkill(2)