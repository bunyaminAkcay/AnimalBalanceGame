from wall import Wall

class UserWall(Wall):

    def __init__(self, boardX, boardY, boardObject, layer, visibility=True):
        super().__init__(boardX, boardY, boardObject, layer, visibility)
        self.setTag("UserWall")
        self.lifetime = 10
        
    
    def move(self):
        pass

    def reduceLifeTime(self):
        self.lifetime -= 1