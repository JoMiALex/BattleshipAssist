import random
from Piece import Piece

class Board:

    def __init__(self):
        self.currState = [[0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0]]
        self.carrier = Piece(5)
        self.battleship = Piece(4)
        self.cruiser = Piece(3)
        self.submarine = Piece(3)
        self.destroyer = Piece(2)
        self.ships = [self.carrier, self.battleship, self.cruiser, self.submarine, self.destroyer]
        self.occupied = set()


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
            self.currState[i][j] = 1