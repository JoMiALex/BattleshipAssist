from Board import Board
from AttackBot import AttackBot
import random

testboard = [[0,0,0,0,0,0,0,0,0,0],
           [0,0,0,1,1,0,0,0,0,0],
           [1,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,0,1,0],
           [1,0,0,0,0,0,0,0,1,0],
           [0,0,0,0,0,0,0,0,1,0],
           [0,0,1,1,1,0,0,0,1,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,1,1,1,1,1,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0]]
startboard = [[0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0]]
#to be used for tracking patterns freq/total runs
#trend = [[1]*10]*10
#frequencies = [[0]*10]*10


def main():
    total = 0
    runCount = 10

    for i in range(runCount):
        print(f"Game {i} Begin!")
        playerBoard = Board()
        print("Board Initialized")
        playerBoard.placePiecesRandom()
        print("Populating Board")
        bot1 = AttackBot()
        print("Bot Initialized")
        playerBoard.printBoard()

        while not playerBoard.isGameOver():
            bot1.attack(playerBoard)
        else:
            print("Game Over!")
        print(f"Ships Sunk: {playerBoard.sunkShips}")
        playerBoard.printBoard()
        
        print(f"Attack Log: {i} with {len(bot1.attackLog)}")
        print(bot1.attackLog)
        total += bot1.moves
    
    average = total/runCount
    print(f"Average Moves: {average} Over {runCount} runs.")

    return average

if __name__ == "__main__":
    final_average = main()