import pygame

class GlobalClock:
    
    _globalClockInstance = None
    _accumulator = [0]

    def __new__(cls, *args, **kwargs):
        if cls._globalClockInstance is None:
            cls._globalClockInstance = super(GlobalClock, cls).__new__(cls)
            cls._globalClockInstance.__init__(*args, **kwargs)
        return cls._globalClockInstance

    def __init__(self):
        self.__clock = pygame.time.Clock()
    
    def tick(self, miliseconds):
        self._accumulator[0] += self.__clock.tick(miliseconds)
    
    @staticmethod
    def getAccumulator():
        return GlobalClock._accumulator[0]