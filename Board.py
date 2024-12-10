import random
from Piece import Piece

class Board:

    def __init__(self):
        self.currState = [['O']*10]*10
        self.carrier = Piece(5)
        self.battleship = Piece(4)
        self.cruiser = Piece(3)
        self.submarine = Piece(3)
        self.destroyer = Piece(2)
        self.ships = [self.carrier, self.battleship, self.cruiser, self.submarine, self.destroyer]
        self.occupied = set()
        self.sunkShips = 0
        self.gameOver = False

    def printBoard(self):
        print(self.currState)
    
    def isGameOver(self):
        return self.gameOver

    def placePiecesRandom(self, piece):
        for s in self.ships:
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                orientation = random.randint(0, 1)
                if orientation == 0:
                    if y + piece.length > 9:
                        continue
                    else:
                        for i in range(piece.length):
                            if (x, y+i) in self.occupied:
                                break
                        else:
                            self.occupied.update(s.setPositions(x, y, orientation))
                else:
                    if x + piece.length > 9:
                        continue
                    else:
                        for i in range(piece.length):
                            if (x+i, y) in self.occupied:
                                break
                        else:
                            self.occupied.update(s.setPositions(x, y, orientation))
        for i,j in self.occupied:
            self.currState[i][j] = '-'
    
    def newAttack(self, x, y):
        hit = 0
        sLen = 0
        if self.currState[x][y] == '-':
            self.currState[x][y] = 'x'
            for s in self.ships:
                if s.checkInPositions((x,y)):
                    sunk, sLen = s.addHit(x,y)
                    if sunk:
                        for i,j in s.positions:
                            self.currState[i][j] = 'X'
                        sunkShips += 1
                        if sunkShips == 5:
                            self.gameOver = True
                    hit += 1
                    break
            print("Hit!")
            hit += 1
        else:
            #self.currState[x][y] = -1
            print("Miss!")
        return hit, sLen