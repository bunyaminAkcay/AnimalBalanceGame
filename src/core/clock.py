from .globalClock import GlobalClock

class Clock:

    def __init__(self, interval):
        self.__globalClock = GlobalClock()
        self.__lastTicked = self.__globalClock.getAccumulator()
        self.interval = interval

    def checkTickable(self):
        accumulatorDiff = self.__globalClock.getAccumulator() - self.__lastTicked
        tickedCount = accumulatorDiff//self.interval
        if tickedCount == 0:
            return False
        return True
    
    def getTicks(self):
        accumulatorDiff = self.__globalClock.getAccumulator() - self.__lastTicked
        tickedCount = accumulatorDiff//self.interval
        self.__lastTicked += tickedCount * self.interval
        return tickedCount

    def clear(self):
        self.__lastTicked = self.__globalClock.getAccumulator()