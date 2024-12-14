class Piece:

    def __init__(self, ship):
        self.positions = set()
        self.damage = set()
        self.orientation = -2  # 0 is right, 1 is down
        self.destroyed = False
        self.shipType = ship

    def getLength(self):
        if self.shipType == "Aircraft carrier":
            return 5
        elif self.shipType == "Battleship":
            return 4
        elif self.shipType == "Cruiser":
            return 3
        elif self.shipType == "Submarine":
            return 3
        elif self.shipType == "Destroyer":
            return 2
        return 0

    # stores the positions that the ship will occupy
    def setPositions(self, startX, startY, orient):
        # print(startingX, startingY)
        if orient == 0:
            self.positions = set((startX,startY+i) for i in range(self.getLength()))
            #for i in range(0, self.shipLength):
            #    self.positions.add((startingX, startingY + i))
        else:
            self.positions = set((startX+i,startY) for i in range(self.getLength()))
        return self.positions

    # sets a position as destroyed
    def addHit(self, i, j):
        print("Hit!")
        if self.destroyed:
            print(self.shipType + " already destroyed!")
            return True
        else:
            self.damage.add((i, j))
            if len(self.damage) == self.getLength():
                self.destroyed = True
                print(self.shipType + " destroyed!")
            return self.destroyed


    def checkInPositions(self, pos):
        if pos in self.positions:
            return True
        return False