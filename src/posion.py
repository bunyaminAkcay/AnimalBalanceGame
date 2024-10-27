from boardObject import BoardObject
import os
import pygame

class Posion(BoardObject):
    
    count = [3]
    def __init__(self, boardX, boardY, boardObject, layer, visibility=True):
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "..", "sprites", "Zehir.png")
        image = pygame.image.load(image_path)
        super().__init__(boardX, boardY, boardObject, layer, image, (0,0,0,0), visibility)
        
        self.setTag("Posion")
        
    

    def move(self):
        pass

    
    def use(self):
        print("use")
        self.count[0] -= 1
        
        if self.count[0] == 0:
            self.boardObject.skillItems.closeSkill(3)