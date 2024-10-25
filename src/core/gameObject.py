class GameObject:

    def __init__(self):
        self._drawable = False
        self.__tag = None

    def init(self):
        pass
    
    def update(self):
        pass

    def fixedUpdate(self):
        pass

    def setTag(self, tagName :str):
        self.__tag = tagName
    
    def getTag(self):
        return self.__tag