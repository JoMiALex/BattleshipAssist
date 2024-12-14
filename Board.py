import random
import time
from Piece import Piece
from TestBoard import TestBoard
from Evaluator import Evaluator

class Board:
    def __init__(self):
        self.currState = [[' ' for _ in range(10)] for _ in range(10)]
        
        #self.carrier = Piece(5)
        #self.battleship = Piece(4)
        #self.cruiser = Piece(3)
        #self.submarine = Piece(3)
        #self.destroyer = Piece(2)
        self.ships = [Piece("Aircraft carrier"), Piece("Battleship"), Piece("Cruiser"), Piece("Submarine"), Piece("Destroyer")]
        self.occupied = set()
        self.sunkShips = []
        self.sunkTotal = 0
        self.gameOver = False
        random.seed(time.time())
        self.evaluator = Evaluator()

    def printBoard(self):
        for row in self.currState:
            print(row)
    
    def isGameOver(self):
        return self.gameOver
    
    def manualPlacing(self):
        for s in self.ships:
            while True:
                print("Enter the starting coordinates for your " + s.shipType + ", " + str(s.getLength()) + ":")
                x = int(input("X: "))
                y = int(input("Y: "))
                orientation = int(input("Orientation (0 for horizontal, 1 for vertical): "))
                if orientation == 0:
                    if y + s.getLength() > 9:
                        print("Ship out of bounds!")
                        continue
                    for i in range(s.getLength()):
                        #print("(" + str(x) + ", " + str(y+i) + ")")
                        if (x, y+i) in self.occupied:
                            print("Ship overlaps with another ship " + self.currState[x][y+i] + " at (" + str(x) + ", " + str(y+i) + ")!")
                            break
                    else:
                        print("It's good, setting ship at (" + str(x) + ", " + str(y) + ") to (" + str(x) + ", " + str(y+i) + ")!")
                        self.occupied.update(s.setPositions(x, y, orientation))
                        print("Setting " + s.shipType + "...")
                        for i in range(s.getLength()):
                            if s.shipType == "Aircraft carrier":
                                self.currState[x][y+i] = 'A'
                            elif s.shipType == "Battleship":
                                self.currState[x][y+i] = 'B'
                            elif s.shipType == "Cruiser":
                                self.currState[x][y+i] = 'C'
                            elif s.shipType == "Submarine":
                                self.currState[x][y+i] = 'S'
                            elif s.shipType == "Destroyer":
                                self.currState[x][y+i] = 'D'
                        break

                else:
                    if x + s.getLength() > 9:
                        print("Ship out of bounds!")
                        continue
                    for i in range(s.getLength()):
                        #print("(" + str(x+i) + ", " + str(y) + ")")
                        if (x+i, y) in self.occupied:
                            print("Ship overlaps with another ship " + self.currState[x+i][y] + " at (" + str(x+i) + ", " + str(y) + ")!")
                            break
                    else:
                        print("It's good, setting ship at (" + str(x) + ", " + str(y) + ") to (" + str(x+i) + ", " + str(y) + ")!")
                        self.occupied.update(s.setPositions(x, y, orientation))
                        print("Setting " + s.shipType + "...")
                        for i in range(s.getLength()):
                            if s.shipType == "Aircraft carrier":
                                self.currState[x+i][y] = 'A'
                            elif s.shipType == "Battleship":
                                self.currState[x+i][y] = 'B'
                            elif s.shipType == "Cruiser":
                                self.currState[x+i][y] = 'C'
                            elif s.shipType == "Submarine":
                                self.currState[x+i][y] = 'S'
                            elif s.shipType == "Destroyer":
                                self.currState[x+i][y] = 'D'
                        break     
                print("Try again!")

    def placePiecesRandom(self, corner):
        for s in self.ships:
            while True:
                if (corner):
                    x = random.randint(0, 5)
                    y = random.randint(0, 5)
                else:
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                orientation = random.randint(0, 1)
                if orientation == 0:
                    if (y + s.getLength() > 9 and not corner) or (y + s.getLength() > 5 and corner):
                        continue
                    for i in range(s.getLength()):
                        #print("(" + str(x) + ", " + str(y+i) + ")")
                        if (x, y+i) in self.occupied:
                            print("Ship overlaps with another ship " + self.currState[x][y+i] + " at (" + str(x) + ", " + str(y+i) + ")!")
                            break
                    else:
                        print("It's good, setting ship at (" + str(x) + ", " + str(y) + ") to (" + str(x) + ", " + str(y+i) + ")!")
                        self.occupied.update(s.setPositions(x, y, orientation))
                        print("Setting " + s.shipType + "...")
                        for i in range(s.getLength()):
                            if s.shipType == "Aircraft carrier":
                                self.currState[x][y+i] = 'A'
                            elif s.shipType == "Battleship":
                                self.currState[x][y+i] = 'B'
                            elif s.shipType == "Cruiser":
                                self.currState[x][y+i] = 'C'
                            elif s.shipType == "Submarine":
                                self.currState[x][y+i] = 'S'
                            elif s.shipType == "Destroyer":
                                self.currState[x][y+i] = 'D'
                        break

                else:
                    if (x + s.getLength() > 9 and not corner) or (x + s.getLength() > 5 and corner):
                        continue
                    for i in range(s.getLength()):
                        #print("(" + str(x+i) + ", " + str(y) + ")")
                        if (x+i, y) in self.occupied:
                            print("Ship overlaps with another ship " + self.currState[x+i][y] + " at (" + str(x+i) + ", " + str(y) + ")!")
                            break
                    else:
                        print("It's good, setting ship at (" + str(x) + ", " + str(y) + ") to (" + str(x+i) + ", " + str(y) + ")!")
                        self.occupied.update(s.setPositions(x, y, orientation))
                        print("Setting " + s.shipType + "...")
                        for i in range(s.getLength()):
                            if s.shipType == "Aircraft carrier":
                                self.currState[x+i][y] = 'A'
                            elif s.shipType == "Battleship":
                                self.currState[x+i][y] = 'B'
                            elif s.shipType == "Cruiser":
                                self.currState[x+i][y] = 'C'
                            elif s.shipType == "Submarine":
                                self.currState[x+i][y] = 'S'
                            elif s.shipType == "Destroyer":
                                self.currState[x+i][y] = 'D'
                        break     
                print("Try again!")
                                         
    def placeTestPlacements(self):
        for s in self.ships:
            if s.shipType == "Aircraft carrier":
                x = 8
                y = 1
                orientation = 0
                print("Setting " + s.shipType + " at (" + str(x) + ", " + str(y) + ") to (" + str(x) + ", " + str(y+5) + ")!")
                self.occupied.update(s.setPositions(x, y, orientation))
                for i in range(s.getLength()):
                    self.currState[x][y+i] = 'A'
            elif s.shipType == "Battleship":
                x = 3
                y = 8
                orientation = 1
                print("Setting " + s.shipType + " at (" + str(x) + ", " + str(y) + ") to (" + str(x+4) + ", " + str(y) + ")!")
                self.occupied.update(s.setPositions(x, y, orientation))
                for i in range(s.getLength()):
                    self.currState[x+i][y] = 'B'
            elif s.shipType == "Cruiser":
                x = 6
                y = 2
                orientation = 0
                print("Setting " + s.shipType + " at (" + str(x) + ", " + str(y) + ") to (" + str(x) + ", " + str(y+3) + ")!")
                self.occupied.update(s.setPositions(x, y, orientation))
                for i in range(s.getLength()):
                    self.currState[x][y+i] = 'C'
            elif s.shipType == "Submarine":
                x = 2
                y = 0
                orientation = 1
                print("Setting " + s.shipType + " at (" + str(x) + ", " + str(y) + ") to (" + str(x+3) + ", " + str(y) + ")!")
                self.occupied.update(s.setPositions(x, y, orientation))
                for i in range(s.getLength()):
                    self.currState[x+i][y] = 'S'
            elif s.shipType == "Destroyer":
                x = 1
                y = 3
                orientation = 0
                print("Setting " + s.shipType + " at (" + str(x) + ", " + str(y) + ") to (" + str(x) + ", " + str(y+2) + ")!")
                self.occupied.update(s.setPositions(x, y, orientation))
                for i in range(s.getLength()):
                    self.currState[x][y+i] = 'D'

    def newAttack(self, x, y):
        hit = 0
        if self.currState[x][y] in ['A', 'B', 'C', 'S', 'D']:
            self.currState[x][y] = 'H'
            for s in self.ships:
                if s.checkInPositions((x,y)):
                    sunk = s.addHit(x,y)
                    if sunk:
                        self.sunkShips.append(s.shipType)
                        self.sunkTotal += 1
                        self.evaluator.addScore(self.sunkTotal)
                        for i,j in s.positions:
                            self.currState[i][j] = 'X'
                        if self.sunkTotal >= 5:
                            self.gameOver = True
                        hit += 1
                    break
            hit += 1
        else:
            #self.currState[x][y] = -1
            self.currState[x][y] = 'm'
            print("Miss!")
        return hit