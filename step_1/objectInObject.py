
class Fridge :
    def __init__(self) :
        self.isOpened = False
        self.foods = []

    def open(self) :
        self.isOpened = True
        return 'Open'

    def put(self, thing) : 
        if self.isOpened :
            self.foods.append(thing)
            return 'in food'
        else:
            return 'not open'

    def close(self) :
        self.isOpened = False
        return 'close'

class Food:
    pass