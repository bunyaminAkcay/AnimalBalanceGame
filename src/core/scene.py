from .camera import Camera
class Scene:
    
    _sceneDictionary = {}

    def __init__(self, name : str, mainCamera : Camera, gameObjects = []):
        self.gameObjects = gameObjects
        self.__name = name
        self._sceneDictionary[name] = self
        self.mainCamera = mainCamera
        self.__gameObjectsInitialized = False
        
    def addGameObject(self, gameObject):
        if gameObject._drawable == False:
            self.gameObjects.append(gameObject)
        else:
            inserted = False

            for i in range(len(self.gameObjects)):
                if self.gameObjects[i]._drawable == False:
                    self.gameObjects.insert(i, gameObject)
                    inserted = True
                    break
                elif self.gameObjects[i]._layer <= gameObject._layer:
                    self.gameObjects.insert(i, gameObject)
                    inserted = True
                    break
            
            if inserted == False:
                self.gameObjects.append(gameObject)
                
    def removeGameObject(self, gameObject):
        self.gameObjects.remove(gameObject)

    def sortLayers(self):
        pass

    def _initGameObjects(self):
        if self.__gameObjectsInitialized == False:
            for gameObject in self.gameObjects:
                gameObject.init()