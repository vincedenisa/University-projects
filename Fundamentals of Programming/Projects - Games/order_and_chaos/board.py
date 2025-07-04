from texttable import Texttable

class BoardException(Exception):
    pass

class EndOfGameException(Exception):
    pass

class Board:
    def __init__(self, repo: bool, file_name = "savedGame.txt"):
        self.__matrix = []
        # building the matrix
        for i in range(6):
            self.__matrix.append([" "] * 6)

        self.__usedCells = 0
        self.xs = 0     # counting the x's placed
        self.os = 0     # counting the o's placed

        # loading the last game if the user choose that
        if repo == True:
            self.file = file_name
            self.loadGame()



    def loadGame(self):
        with open(self.file, "r") as fin:
            for line in fin:
                try:
                    tokens = line.split(" ")
                    symbol = tokens[0].strip()
                    row = int(tokens[1].strip())
                    col = int(tokens[2].strip())

                    self.placeSymbol(row, col, symbol)
                except BoardException as be:
                    raise BoardException(be)
                except:
                    raise BoardException("There is a problem in the file, either try to solv it or play a new game.")

    def saveToFile(self):
        with open(self.file, "w") as fin:
            for i in range(6):
                for j in range(6):
                    if self.__matrix[i][j] != " ":
                        fin.write(f"{self.__matrix[i][j]} {i} {j}\n")

    def placeSymbol(self, row: int, col: int, symbol: str):
        if row not in [0, 1, 2, 3, 4, 5] or col not in [0, 1, 2, 3, 4, 5]:
            raise BoardException("You picked a place outside the board!")
        if self.__matrix[row][col] != " ":
            raise BoardException("The cell you chose is already used!")

        if symbol not in "xo":
            raise BoardException("The symbol is not 'x' or 'o'!")

        self.__matrix[row][col] = symbol
        self.__usedCells += 1
        if symbol == "x":
            self.xs += 1
        if symbol == "o":
            self.os += 1


    def usedCells(self):
        return self.__usedCells

    @property
    def matrix(self):
        return self.__matrix

    def __str__(self):
        table = Texttable()

        table.header(["\\", 1, 2, 3, 4, 5, 6])
        for i in range(6):
            row = [i + 1]
            for j in range(6):
                row.append(self.__matrix[i][j])
            table.add_row(row)

        return table.draw()