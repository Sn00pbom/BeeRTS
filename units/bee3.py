from unit import Unit


class Bee3(Unit):

    def __init__(self, hp, speed, x, y, side):
        self.side = side
        super(self.__class__, self).__init__(hp, speed, x, y)


        self.hp = 30