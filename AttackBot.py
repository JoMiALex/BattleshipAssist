import random
from Board import Board

class AttackBot:
    
    def __init__(self):
        self.attackLog = set()
        self.sunkLog = set()
        self.targets = []

    def attack(self, board):
        
        if self.targets:
            x,y = self.targets.pop()
        else:
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if (x,y) not in self.attackLog:
                    break
        