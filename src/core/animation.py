import pygame
from .clock import Clock

class Animation:

    def __init__(self, imageList, animationSpeed):
        self.__imageList = imageList
        self.__currentImageIndex = 0
        self.__imageListSize = len(imageList)
        self.clock = Clock(animationSpeed)

    def getCurrentImage(self):
        self.__currentImageIndex = (self.__currentImageIndex + self.clock.getTicks()) % self.__imageListSize
        return self.__imageList[self.__currentImageIndex]

    def clear(self):
        self.clock.clear()

    @staticmethod
    def spriteSheetToImageList(spriteSheet, frameWidth, frameHeight, frameCount):
        frames = []
        for i in range(frameCount):
            frame = spriteSheet.subsurface(pygame.Rect(i * frameWidth, 0, frameWidth, frameHeight))
            frames.append(frame)
        return frames

