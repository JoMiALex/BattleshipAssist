import random
import time
from Piece import Piece

class Board:

    def __init__(self):
        self.currState = [[' ' for _ in range(10)] for _ in range(10)]
        self.carrier = Piece(5)
        self.battleship = Piece(4)
        self.cruiser = Piece(3)
        self.submarine = Piece(3)
        self.destroyer = Piece(2)
        self.ships = [self.carrier, self.battleship, self.cruiser, self.submarine, self.destroyer]
        self.occupied = set()
        self.sunkShips = 0
        self.gameOver = False
        random.seed(time.time())

    def printBoard(self):
        for row in self.currState:
            print(row)
    
    def isGameOver(self):
        return self.gameOver
    
    def manualPlacing(self):
        for s in self.ships:
            while True:
                print("Enter the starting coordinates for your", s.getLength(), "length ship:")
                x = int(input("X: "))
                y = int(input("Y: "))
                orientation = int(input("Orientation (0 for horizontal, 1 for vertical): "))
                if orientation == 0:
                    if y + s.getLength() > 9:
                        print("Ship out of bounds!")
                        continue
                    else:
                        for i in range(s.getLength()):
                            if (x, y+i) in self.occupied:
                                print("Ship overlaps with another ship!")
                                break
                        else:
                            self.occupied.update(s.setPositions(x, y, orientation))
                else:
                    if x + s.getLength() > 9:
                        print("Ship out of bounds!")
                        continue
                    else:
                        for i in range(s.getLength()):
                            if (x+i, y) in self.occupied:
                                print("Ship overlaps with another ship!")
                                break
                        else:
                            self.occupied.update(s.setPositions(x, y, orientation))
                self.printBoard()
                break
        for i,j in self.occupied:
            self.currState[i][j] = 'A'

    def placePiecesRandom(self):
        for s in self.ships:
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                orientation = random.randint(0, 1)
                if orientation == 0:
                    if y + s.getLength() > 9:
                        continue
                    else:
                        for i in range(s.getLength()):
                            if (x, y+i) in self.occupied:
                                break
                        else:
                            self.occupied.update(s.setPositions(x, y, orientation))
                else:
                    if x + s.getLength() > 9:
                        continue
                    else:
                        for i in range(s.getLength()):
                            if (x+i, y) in self.occupied:
                                break
                        else:
                            self.occupied.update(s.setPositions(x, y, orientation))
                break
        for i,j in self.occupied:
            self.currState[i][j] = 'A'
    
    def newAttack(self, x, y):
        hit = 0
        sLen = 0
        if self.currState[x][y] == 'A':
            self.currState[x][y] = 'H'
            for s in self.ships:
                if s.checkInPositions((x,y)):
                    sunk, sLen = s.addHit(x,y)
                    if sunk:
                        for i,j in s.positions:
                            self.currState[i][j] = 'X'
                        self.sunkShips += 1
                        if self.sunkShips == 5:
                            self.gameOver = True
                        hit += 1
                    break
            print("Hit!")
            hit += 1
        else:
            #self.currState[x][y] = -1
            self.currState[x][y] = 'm'
            print("Miss!")
        return hit