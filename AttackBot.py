import random
import time
from Board import Board

class AttackBot:
    
    def __init__(self):
        self.attackLog = set()
        #self.sunkLog = set()
        self.reccommended = [[1]*10]*10
        self.direct = 0
        self.chain = []
        self.next = []
        self.Forward = False
        #self.adj = False
        self.moves = 0
        random.seed(time.time())

    def attack(self, board):
        #print("Attack!")
        if not board.isGameOver() and self.moves < 100:
            if self.next:
                x,y = self.next.pop()
            else:
                while True:
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    if (x,y) not in self.attackLog:
                        break
            self.attackLog.add((x, y))
            self.moves += 1
            print(f"Attacking {x},{y} for move {self.moves}")
            success = board.newAttack(x, y)
            if success == 2:
                #self.sunkLog.add((x, y))
                self.direct = 0
                self.chain.clear()
                self.next.clear()
                self.Forward = False
            elif success == 1:
                if not self.chain:
                    self.chain = [x,y]
                else:
                    self.Forward = True
                self.getAdj(x, y)
            else:
                if self.chain:
                    x, y = self.chain
                    if self.Forward:
                        print("Backtracking")
                        self.direct = (self.direct + 2) % 4
                        self.getAdj(x, y)
                    else:
                        self.direct += 1
                        self.getAdj(x, y)
                else:
                    self.direct = 0
                    self.chain.clear()
                    self.next.clear()
            return True
        else:
            board.gameOver = True
            #print("Game Over!")
            return False            

    def getAdj(self, x, y):
        directions = [(0, 1), (1, 0),(0, -1), (-1, 0)]
        if self.direct < 4:
            i, j = directions[self.direct]
        else:
            return
        if 0 <= (x+i) < 10 and 0 <= (y+j) < 10 and (x+i, y+j) not in self.attackLog and not self.next:
            self.next.append((x+i, y+j))
        elif self.direct < 3:
            self.direct += 1
            self.getAdj(x, y)
        else:
            self.direct = 0
            self.chain.clear()
            self.next.clear()
            self.Forward = False