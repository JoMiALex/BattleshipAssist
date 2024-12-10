class Evaluator:

    def __init__(self, board):
        self.board = board
        self.carrierVal = 20
        self.battleshipVal = 30
        self.cruiserVal = 45
        self.submarineVal = 45
        self.destroyerVal = 60
        self.total = 0

    def addScore(self, s, order):
        if (s == "Aircraft carrier"):
            self.total += self.carrierVal/order
        elif (s == "Battleship"):
            self.total += self.battleshipVal/order
        elif (s == "Cruiser"):
            self.total += self.cruiserVal/order
        elif (s == "Submarine"):
            self.total += self.submarineVal/order
        elif (s == "Destroyer"):
            self.total += self.destroyerVal/order

    def printScore(self):
        print("The Admiral evaluator gives you a score of " + str(round(self.total, 2)) + "/100.")
        return self.total