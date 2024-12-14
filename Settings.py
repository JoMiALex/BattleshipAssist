class Settings:

    def __init__(self):
        self.runCount = 20
        self.heatmapActive = True
        self.skipTt = True
        self.botControl = True
        self.corner = False
        self.setControl = False
        self.playerControl = False

    def menu(self):
        print("Welcome to Battleship AI!")
        print('')
        while(True):
            answer = input("Play(p)    Game Type(t)    Settings(s)    Quit(q): ")
            if answer.lower() == 'p':
                return 1
            elif answer.lower() == 't':
                print('')
                print("Select a game type that isn't already selected.")
                while(True):
                    answer = input("Random Board(r): " + str(self.botControl) + "    set Board(s): " + str(self.setControl) + 
                                   "    Player Board(p): " + str(self.playerControl) + "    Back(q): ")
                    if answer.lower() == 'r' and (not self.botControl):
                            while(True):
                                answer = input("Corner bot? (y or n): ")
                                if answer.lower() == 'y':
                                    self.corner = True
                                    break
                                elif answer.lower() == 'n':
                                    self.corner = False
                                    break
                                print("Please enter a valid input.")
                                print('')
                            self.botControl = True
                            self.setControl = False
                            self.playerControl = False
                            print("Selecting random board...")
                    elif answer.lower() == 's' and (not self.setControl):
                            self.botControl = False
                            self.setControl = True
                            self.playerControl = False
                            self.corner = False
                            print("Selecting set board...")
                    elif answer.lower() == 'p' and (not self.playerControl):
                            self.botControl = False
                            self.setControl = False
                            self.playerControl = True
                            self.corner = False
                            print("Selecting player board...")
                    elif answer.lower() == 'q':
                        print('')
                        break
                    else:
                        print("Please select a board that isn't already selected.")
                        continue
                    input("Press Enter to continue...")
            elif answer.lower() == 's':
                print('')
                while(True):
                    answer = input("RunCount(r): " + str(self.runCount) + "    Heatmap(h): " + str(self.heatmapActive) + 
                                   "    Skip through turns(t): " + str(self.skipTt) + "    Back(q): ")
                    if answer.lower() == 'r':
                        while True:
                            try:
                                answer = int(input("How many games would you like to run? "))       
                            except ValueError:
                                print("Not an integer!")
                                continue
                            else:
                                self.runCount = answer
                                break 
                    elif answer.lower() == 'h':
                        if (self.heatmapActive):
                            self.heatmapActive = False
                            print("Deactivating Heatmap...")
                        elif (not self.heatmapActive):
                            self.heatmapActive = True
                            print("Activating Heatmap...")
                    elif answer.lower() == 't':
                        if (self.skipTt):
                            self.skipTt = False
                            print("Deactivating Turn-by-Turn...")
                        elif (not self.skipTt):
                            self.skipTt = True
                            print("Activating Turn-by-Turn...")
                    elif answer.lower() == 'q':
                        print('')
                        break
                    else:
                        print("Please enter a valid input.")
                        continue
                    input("Press Enter to continue...")
            elif answer.lower() == 'q':
                print("Thank you for using Battleship AI!")
                print('')
                return 0
            else:
                print("Please enter a valid input.")
                continue
        print('')