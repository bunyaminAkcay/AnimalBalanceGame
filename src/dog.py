from animal import Animal

import os
import pygame
class Dog(Animal):
    
    def __init__(self, boardX, boardY, boardObject, layer, visibility=True):
        base_path = os.path.dirname(__file__)
        cat_image_path = os.path.join(base_path, "..", "sprites", "Dog.png")
        
        catImage = pygame.image.load(cat_image_path)

        super().__init__(boardX, boardY, boardObject, layer, catImage, (0, 0, 0, 0), visibility)
        self.targetAnimalTag = "Animal.Cat"
        self.enemyAnimalTag = "Animal.Human" 
        self.birthChance = 0.02

    def init(self):
        super().init()
        self.setTag("Animal.Dog")

    