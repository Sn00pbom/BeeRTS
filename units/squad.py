

class Squad():

    def __init__(self):
        self.units = []

    def addUnit(self,unit):
        if not self.units.__contains__(unit): self.units.append(unit)


    def setVelTowards(self,pos):
        for unit in self.units:
            unit.setVelTowards(pos)

    def clear(self):
        self.units = []