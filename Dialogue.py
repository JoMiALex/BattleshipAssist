class Dialogue:

    def __init__(self, r, h, s):
        self.count = r
        self.heatmap = h
        self.skip = s

    def menu(self):
        print("Welcome to Battleship AI!")
        print('')
        while(True):
            answer = input("Play(p)    Settings(s)    Quit(q): ")
            if answer.lower() == 'p':
                return 1
            elif answer.lower() == 's':
                print('')
                while(True):
                    answer = input("RunCount(r): " + str(self.count) + "    Heatmap(h): " + str(self.heatmap) + 
                                   "    Turn-by-Turn(t): " + str(self.skip) + "    Back(q): ")
                    if answer.lower() == 'r':
                        while True:
                            try:
                                answer = int(input("How many games would you like to run? "))       
                            except ValueError:
                                print("Not an integer!")
                                continue
                            else:
                                self.count = answer
                                break 
                    elif answer.lower() == 'h':
                        if (self.heatmap):
                            self.heatmap = False
                            print("Deactivating Heatmap...")
                        elif (not self.heatmap):
                            self.heatmap = True
                            print("Activating Heatmap...")
                    elif answer.lower() == 't':
                        if (self.skip):
                            self.skip = False
                            print("Deactivating Turn-by-Turn...")
                        elif (not self.skip):
                            self.skip = True
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