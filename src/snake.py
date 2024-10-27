from animal import Animal

import os
import pygame
class Snake(Animal):
    
    def __init__(self, boardX, boardY, boardObject, layer, visibility=True):
        base_path = os.path.dirname(__file__)
        cat_image_path = os.path.join(base_path, "..", "sprites", "Snake.png")
        
        catImage = pygame.image.load(cat_image_path)

        super().__init__(boardX, boardY, boardObject, layer, catImage, (0, 0, 0, 0), visibility)
        self.targetAnimalTag = "Animal.Frog"
        self.enemyAnimalTag = "Animal.Eagle" 
        self.birthChance = 0.04

    def init(self):
        super().init()
        self.setTag("Animal.Snake")

    