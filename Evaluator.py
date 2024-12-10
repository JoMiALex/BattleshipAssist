class Evaluator:

    def __init__(self, ):
        #self.carrierVal = 1
        #self.battleshipVal = 2
        #self.cruiserVal = 3
        #self.submarineVal = 3
        #self.destroyerVal = 4
        self.total = 0

    def addScore(self, s, order):
        #if (s == "Aircraft carrier"):
        #   self.total += self.carrierVal/order
        #elif (s == "Battleship"):
        #   self.total += self.battleshipVal/order
        #elif (s == "Cruiser"):
        #    self.total += self.cruiserVal/order
        #elif (s == "Submarine"):
        #   self.total += self.submarineVal/order
        #elif (s == "Destroyer"):
        #   self.total += self.destroyerVal/order
        self.total = order/5

    def printScore(self, turns):
        print("The Admiral evaluator gives you a score of " + str(round(self.total*(100-turns), 2)) + ".")
        return self.total