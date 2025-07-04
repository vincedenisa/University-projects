from board import BoardException, EndOfGameException
from game import Game


class UserInterface:
    def __init__(self):
        # self.service = service
        pass

    def __call__(self):

        while True:
            choice1 = input("""
            1 - play a new game
            2 - load a previous game from the file
            """)
            if choice1 == "2":
                self.service = Game(True)
            elif choice1 == "1":
                self.service = Game(False)
            else:
                print("Invalid command!")
                continue

            while True:

                print(self.service.displayBoard())

                choice2 = input("""
                                1 - continue playing
                                2 - save the current play
                                """)
                if choice2 == "2":
                    self.service.saveToFile()
                    continue
                elif choice2 == "1":
                    row = int(input("row: "))
                    col = int(input("col: "))
                    symbol = input("symbol (x/o):")
                    if symbol not in "xo":
                        print("Symbol is not 'x' or 'o'!")
                        continue

                    # human move
                    try:
                        self.service.humanMove(row-1, col-1, symbol)
                    except EndOfGameException as eog:
                        print(eog)
                        return
                    except BoardException as be:
                        print(be)

                    # computer move
                    try:
                        self.service.computerMove()
                    except EndOfGameException as eog:
                        print(eog)
                        return
                else:
                    print("You have not chosen 1 or 2.")