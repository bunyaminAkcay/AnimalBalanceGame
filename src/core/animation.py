import pygame
from .clock import Clock

class Animation:

    def __init__(self, imageList, animationSpeed, loop = True):
        self.__imageList = imageList
        self.__currentImageIndex = 0
        self.__imageListSize = len(imageList)
        self.clock = Clock(animationSpeed)
        self.__loop = loop
        self.__loopEnd = False

    def getCurrentImage(self):

        if self.__loopEnd:
            return self.__imageList[self.__imageListSize -1]            

        self.__currentImageIndex = (self.__currentImageIndex + self.clock.getTicks()) % self.__imageListSize
        
        if self.__loop == False and self.__currentImageIndex + 1 == self.__imageListSize:
            self.__loopEnd = True
        
        return self.__imageList[self.__currentImageIndex]

    def clear(self):
        self.clock.clear()
        self.__loopEnd = False
        self.__currentImageIndex = 0

    @staticmethod
    def spriteSheetToImageList(spriteSheet, frameWidth, frameHeight, frameCount):
        frames = []
        for i in range(frameCount):
            frame = spriteSheet.subsurface(pygame.Rect(i * frameWidth, 0, frameWidth, frameHeight))
            frames.append(frame)
        return frames

