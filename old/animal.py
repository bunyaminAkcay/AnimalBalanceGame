from boardObject import BoardObject
import random

class Animal(BoardObject):

    #returns targetLocation
    def move(self, x, y):
        random_number = random.randint(0, 3)

        if random_number == 0:
            return (x+1, y)
        elif random_number == 1:
            return (x, y+1)
        elif random_number == 2:
            return (x-1, y)
        elif random_number == 3:
            return (x, y-1)
        
        return (x,y)