import random
from Board import Board

class AttackBot:
    
    def __init__(self):
        self.attackLog = set()
        self.sunkLog = set()
        self.nearby = []
        self.reccommended = [[1]*10]*10
        self.last = set()
        self.adj = False

    def attack(self, board):
        if not board.isGameOver():
            if self.nearby:
                x,y = self.nearby.pop()
            else:
                while True:
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    if (x,y) not in self.attackLog:
                        break
            self.attackLog.add((x, y))
            success = board.newAttack(x, y)
            if success > 0:
                if success == 2:
                    self.sunkLog.add((x, y))
                else:
                    self.adj = True
                    self.getNeighbors(x, y)

    def getNeighbors(self, x, y):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i, j in directions:
            if 0 <= (x+i) < 10 and 0 <= (y+j) < 10 and (x+i, y+j) not in self.attackLog:
                self.nearby.append((x, y))