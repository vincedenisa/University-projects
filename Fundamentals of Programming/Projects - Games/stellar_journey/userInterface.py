from board import BoardErrors
from service import Game, EndOfGame


class UserInterface:
    def __init__(self):
        self.game = Game()

    def __call__(self):
        print("""Available commands:
        warp <coordonate> (e.g. warp G5)
        fire <coordonate> (e.g. fire B4)
        cheat -> Displays the full board. Not recommanded:))
        """)
        while True:
            print(self.game.displayBoard())
            command = input(">>>")

            tokens = command.split(" ")
            for token in tokens:
                if token == "":
                    tokens.remove(token)

            if tokens[0] == "warp":
                if len(tokens) != 2:
                    print("Invalid number of arguments!")
                try:
                    coordonate = tokens[1].strip()
                    # if the user enter 8C interchange the coordonate
                    if coordonate[0] in "12345678":
                        coordonate = coordonate[1] + coordonate[0]
                    if coordonate[0].upper() not in "ABCDEFGH" or coordonate[1] not in "12345678":
                        print("Invalid coordonate!")
                        continue
                    i = ord(coordonate[0].upper()) - ord("A") + 1
                    j = int(coordonate[1])
                    try:
                        self.game.warp(i, j)
                    except BoardErrors as be:
                        print(be)
                    except EndOfGame as eog:
                        print(eog)
                        return
                except Exception as e:
                    print(f"Invalid command - {e}")

            elif tokens[0] == "fire":
                if len(tokens) != 2:
                    print("Invalid number of arguments!")
                try:
                    coordonate = tokens[1].strip()
                    # if the user enter 8C interchange the coordonate
                    if coordonate[0] in "12345678":
                        coordonate = coordonate[1] + coordonate[0]
                    if coordonate[0].upper() not in "ABCDEFGH" or coordonate[1] not in "12345678":
                        print("Invalid coordonate!")
                        continue
                    i = ord(coordonate[0].upper()) - ord("A") + 1
                    j = int(coordonate[1])
                    try:
                        print(self.game.fire(i, j))
                    except EndOfGame as eog:
                        print(eog)
                        return
                    except BoardErrors as be:
                        print(be)
                except Exception as e:
                    print(f"Invalid command - {e}")

            elif tokens[0].strip() == "cheat":
                print(self.game.cheatShowFullBoard())

            else:
                print("Invalid command!")