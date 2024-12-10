from Board import Board
from AttackBot import AttackBot
from Evaluator import Evaluator
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
    skip = False

    while(True):
        answer = input("Skip turn-by-turn? (y or n): ")
        if answer.lower() == 'y':
            skip = True
            break
        elif answer.lower() == 'n':
            break
        print("Please enter yes or no.")

    for i in range(runCount):
        print(f"Game {i + 1} Begin!")
        playerBoard = Board()
        print("Board Initialized")
        playerBoard.placePiecesRandom()
        print("Populating Board")
        bot1 = AttackBot()
        print("Bot Initialized")
        playerBoard.printBoard()
        botEvaluator = Evaluator(playerBoard)
        print("Eval Initialized")

        while not playerBoard.isGameOver():
            bot1.attack(playerBoard)
            if (not skip):
                input("Press Enter to continue...")
                playerBoard.printBoard()
        else:
            print("Game Over!")

        print(f"Attack Log: {i} with {len(bot1.attackLog)} moves")
        #print(bot1.attackLog)
        total += bot1.moves
    
    average = total/runCount
    #print(f"Average Moves: {average} Over {runCount} runs.")
    return average

if __name__ == "__main__":
    final_average = main()