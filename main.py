from Board import Board
from AttackBot import AttackBot
from Settings import Settings
from HeatMap import HeatMap
import random

testboard = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ','D','D',' ',' ',' ',' ',' '],
             ['S',' ',' ',' ',' ',' ',' ',' ',' ',' '],
             ['S',' ',' ',' ',' ',' ',' ',' ','B',' '],
             ['S',' ',' ',' ',' ',' ',' ',' ','B',' '],
             [' ',' ',' ',' ',' ',' ',' ',' ','B',' '],
             [' ',' ','C','C','C',' ',' ',' ','B',' '],
             [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
             [' ','A','A','A','A','A',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
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
    settings = Settings()
    print("Settings initialized!")

    playerHeatmap = HeatMap()
    print("Heatmap initialized!")
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
        menu = settings.menu()
        if (menu == 0):
            return 0
        average = 0
        total = 0

        for i in range(settings.runCount):
            print(f"Game {i + 1} begin!")
            playerBoard = Board()
            if (settings.botControl and not settings.setControl and not settings.playerControl):
                playerBoard.placePiecesRandom(settings.corner)
            elif (not settings.botControl and settings.setControl and not settings.playerControl):
                playerBoard.placeTestPlacements()
            elif (not settings.botControl and not settings.setControl and settings.playerControl):
                playerBoard.manualPlacing()
            print("Board initialized!")
            print("Populating board...")
            bot1 = AttackBot()
            print("Bot initialized!")
            turns = 0
            
            while not playerBoard.isGameOver():
                turns += 1
                if (settings.skipTt == False):
                    playerBoard.printBoard()
                    input("Press Enter to continue...")
                    bot1.attack(playerBoard, playerHeatmap, settings.heatmapActive)
                else:
                    playerBoard.printBoard()
                    bot1.attack(playerBoard, playerHeatmap, settings.heatmapActive)
            else:
                print("Game Over!")
                if (settings.heatmapActive):
                    playerHeatmap.updateHeatmap(playerBoard.occupied)
                    playerHeatmap.printHeatmap()

            print(f"Attack Log: {i} with {len(bot1.attackLog)} moves")
            #print(bot1.attackLog)
            total += bot1.moves
            playerBoard.evaluator.printScore(turns)
        
        average = total/settings.runCount
        print(f"Average Moves: {average} Over {settings.runCount} runs.")
        average = 0
        total = 0
        input("Press Enter to continue...")
        print('')

    return -1

if __name__ == "__main__":
    final_average = main()