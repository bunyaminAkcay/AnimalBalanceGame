from animal import Animal
import pygame
import os

class Mouse(Animal):
    def __init__(self, boardX, boardY, boardObject, layer,  visibility=True):
        base_path = os.path.dirname(__file__)
        mouse_image_path = os.path.join(base_path, "..", "sprites", "Fare.png")
        
        Mouse_Image = pygame.image.load(mouse_image_path)

        super().__init__(boardX, boardY, boardObject, layer, Mouse_Image,  visibility)
 
 
 
 
 
    def init(self):
        super().init()
        self.setTag("Mouse")