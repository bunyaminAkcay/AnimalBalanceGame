from animal import Animal

import os
import pygame
class Frog(Animal):
    
    def __init__(self, boardX, boardY, boardObject, layer, visibility=True):
        base_path = os.path.dirname(__file__)
        cat_image_path = os.path.join(base_path, "..", "sprites", "Frog.png")
        
        catImage = pygame.image.load(cat_image_path)

        super().__init__(boardX, boardY, boardObject, layer, catImage, (0, 0, 0, 0), visibility)
        self.targetAnimalTag = "Animal.Nothing"
        self.enemyAnimalTag = "Animal.Snake" 
        self.birthChance = 0.05

    def init(self):
        super().init()
        self.setTag("Animal.Frog")

    