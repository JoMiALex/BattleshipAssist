from Board import Board
from AttackBot import AttackBot
from Dialogue import Dialogue
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
    heatmapActive = False
    skipTt = False

    dialogue = Dialogue(runCount, heatmapActive, skipTt)
    print("Dialogue initialized!")
    
    #while(True):
    #    answer = input("Skip turn-by-turn? (y or n): ")
    #    if answer.lower() == 'y':
    #        skipTt = True
    #        break
    #    elif answer.lower() == 'n':
    #        skipTt = False
    #        break
    #        break
    #    print("Please enter a valid input.")
    #print('')

    while(True):
        menu = dialogue.menu()
        if (menu == 0):
            return 0

        for i in range(runCount):
            print(f"Game {i + 1} begin!")
            playerBoard = Board()
            print("Board initialized!")
            playerBoard.placePiecesRandom()
            print("Populating board...")
            bot1 = AttackBot()
            print("Bot initialized!")
            playerBoard.printBoard()
            turns = 0

            while not playerBoard.isGameOver():
                turns += 1
                if (skipTt == True):
                    input("Press Enter to continue...")
                    playerBoard.printBoard()
                bot1.attack(playerBoard, heatmapActive)
            else:
                print("Game Over!")

            print(f"Attack Log: {i} with {len(bot1.attackLog)} moves")
            #print(bot1.attackLog)
            total += bot1.moves
            playerBoard.evaluator.printScore(turns)
        
        average = total/runCount
        print(f"Average Moves: {average} Over {runCount} runs.")
        input("Press Enter to continue...")
        print('')

    return -1

if __name__ == "__main__":
    final_average = main()