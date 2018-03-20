from unit import Unit


class Bee1(Unit):

    def __init__(self, hp, speed, x, y, side):
        self.side = side
        super(self.__class__, self).__init__(hp, speed, x, y)

        if side == 0:
            self.image = pg.image.load("./assets/units/unit_worker.png")

        self.hp = 10
