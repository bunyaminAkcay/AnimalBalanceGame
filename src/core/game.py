import pygame
from .scene import Scene
from .transform import Transform
from .globalClock import GlobalClock
class Game:

    _gameInstance = None
    _scene = [None]
    _screenSize = [0,0]

    def __new__(cls, *args, **kwargs):
        if cls._gameInstance is None:
            cls._gameInstance = super(Game, cls).__new__(cls)
            cls._gameInstance.__init__(*args, **kwargs)
        return cls._gameInstance

    def __init__(self, screenSize : tuple, sceneName, maxFps = 60, maxFixedFps = 60, screenFlag = pygame.FULLSCREEN, backgroundColor = (0, 0, 0)):
        pygame.init()
        self.__backgroundColor = backgroundColor
        Game._screenSize[0] = screenSize[0]
        Game._screenSize[1] = screenSize[1]
        self.__screen = pygame.display.set_mode(screenSize, screenFlag)
        self.__fps = maxFps
        self.__oneOverFps = 1000/float(maxFps)
        self.__fixedFps = maxFixedFps
        self.__oneOverFixedFps = 1000/float(self.__fixedFps)
        self.__loopFps = max(maxFps, maxFixedFps)
        self.__loopFpsDeterminedByFps = False
        if (maxFps >=  maxFixedFps):
            self.__loopFpsDeterminedByFps = True
        self.__running = True
        self.__globalClock = GlobalClock()
        self.__lastClockAccumulator = self.__globalClock.getAccumulator()
        self.__startingSceneName = sceneName

    def run(self):
        
        self.changeScene(self.__startingSceneName)

        while self.__running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False

            if(self.__loopFpsDeterminedByFps):
                #fixed update
                if(self.__globalClock.getAccumulator() - self.__lastClockAccumulator >= self.__oneOverFixedFps):
                    self.__fixedGameLoop()
                    self.__lastClockAccumulator = self.__globalClock.getAccumulator()
                #update
                self.__gameLoop()
            else:
                #fixed update
                self.__fixedGameLoop()
                #update
                if(self.__globalClock.getAccumulator() - self.__lastClockAccumulator >= self.__oneOverFps):
                    self.__gameLoop()
                    self.__lastClockAccumulator = self.__globalClock.getAccumulator()
            
            self.__globalClock.tick(self.__loopFps)
    
    def __gameLoop(self):
        self.__screen.fill(self.__backgroundColor)
        
        for gameObject in self.getScene().gameObjects:
            gameObject.update()
        
        mainCameraX = self.getScene().mainCamera.centerX
        mainCameraY = self.getScene().mainCamera.centerY
        mainCameraZoom = self.getScene().mainCamera._zoom
        for gameObject in self.getScene().gameObjects:
            if gameObject._drawable == False:
                continue
            
            if gameObject.visibility == False:
                continue
            
            if gameObject._isUI == True:
                self.__screen.blit(gameObject._getSurface(), gameObject.getRect())
                continue

            if self.getScene().mainCamera._zoomed == True:
                gameObject._updateScale(mainCameraZoom)
            
            gameObjectSize = gameObject._getSurface().get_size()
            isInWindow, pixelPosition = Transform.getPixelPositionFromPosition(
                                                                    Game._screenSize[0],
                                                                    Game._screenSize[1],
                                                                    gameObject.x,
                                                                    gameObject.y,
                                                                    gameObjectSize[0],
                                                                    gameObjectSize[1],
                                                                    mainCameraX,
                                                                    mainCameraY,
                                                                    mainCameraZoom)
            
            if isInWindow:
                self.__screen.blit(gameObject._getSurface(), pixelPosition)

        pygame.display.flip()

    def __fixedGameLoop(self):
        for gameObject in Game.getScene().gameObjects:
            gameObject.fixedUpdate()
    
    @staticmethod
    def changeScene(sceneName):
        if(sceneName in Scene._sceneDictionary):
            Game._scene[0] = Scene._sceneDictionary[sceneName]
            Game.getScene().sortLayers()
            Game.getScene()._initGameObjects()
        else:
            print("FATAL: ", "Scene not found.")
            exit()
    
    @staticmethod
    def getScene():
        return Game._scene[0]

    @staticmethod
    def getScreenSize():
        return (Game._screenSize[0], Game._screenSize[1])