from boardObject import BoardObject
import os
import pygame

class Wall(BoardObject):
    
    def __init__(self, boardX, boardY, boardObject, layer, visibility=True):
        base_path = os.path.dirname(__file__)
        wall_image_path = os.path.join(base_path, "..", "sprites", "ET-Yan-1.png")
        wall_Image = pygame.image.load(wall_image_path)
        super().__init__(boardX, boardY, boardObject, layer, wall_Image, (0,0,0,0), visibility)

    def init(self):
        self.setTag("Wall")
    

    def move(self):
        pass

