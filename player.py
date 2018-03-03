import units

class Player():


    def __init__(self,gameWidth,gameHeight):

        self.selected = []
        self.dbbee = units.Unit(gameWidth,gameHeight)