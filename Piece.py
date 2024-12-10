class Piece:

    def __init__(self, lShip):
        self.positions = set()
        self.damage = set()
        self.orientation = -2  # 0 is right, 1 is down
        self.destroyed = False
        self.shipLength = lShip

    def getLength(self):
        return self.shipLength

    # stores the positions that the ship will occupy
    def setPositions(self, startX, startY, orient):
        # print(startingX, startingY)
        if orient == 0:
            self.positions = set((startX,startY+i) for i in range(self.shipLength))
            #for i in range(0, self.shipLength):
            #    self.positions.add((startingX, startingY + i))
        else:
            self.positions = set((startX+i,startY) for i in range(self.shipLength))
        return self.positions

    # sets a position as destroyed
    def addHit(self, i, j):
        if self.destroyed:
            print("Ship already destroyed!")
        else:
            self.damage.add((i, j))
            if len(self.damage) == self.shipLength:
                self.destroyed = True
                print("Ship destroyed!")


    def checkInPositions(self, pos):
        if pos in self.positions:
            return True
        return False