from board import Board, EndOfGameException
from random import choice

class Game:
    def __init__(self, repo: bool, fileName="savedGame.txt"):
        self.repo = Board(repo, fileName)

    def placeSymbol(self, row, col, symbol):
        self.repo.placeSymbol(row, col, symbol)

    def displayBoard(self):
        return str(self.repo)

    def saveToFile(self):
        self.repo.saveToFile()

    def humanMove(self, row, col, symbol):
        self.placeSymbol(row, col, symbol)  # taking into conside
        self.isWon()    # checking if is won

    def computerMove(self):
        # -----trying to block-----
        if True:
            # checking rows
            for i in range(6):
                xs = 0  # the number of x's
                os = 0  # the number of o's
                freeCell = (-1, -1)
                for j in range(5):
                    if self.repo.matrix[i][j] == 'x':
                        xs += 1
                    elif self.repo.matrix[i][j] == 'o':
                        os += 1
                    else:
                        freeCell = (i, j)  # in case when there are 4 identical symbols it will place here the other symbol

                if xs == 4:
                    print(freeCell)
                    self.repo.placeSymbol(freeCell[0], freeCell[1], "o")
                    self.isWon()  # checking if the game is won
                    return
                elif os == 4:
                    print(freeCell)
                    self.repo.placeSymbol(freeCell[0], freeCell[1], "x")
                    self.isWon()  # checking if the game is won
                    return

                for j in range(1, 6):
                    if self.repo.matrix[i][j] == 'x':
                        xs += 1
                    elif self.repo.matrix[i][j] == 'o':
                        os += 1
                    else:
                        freeCell = (i, j)  # in case when there are 4 identical symbols it will place here the other symbol

                if xs == 4:
                    print(freeCell)
                    self.repo.placeSymbol(freeCell[0], freeCell[1], "o")
                    self.isWon()  # checking if the game is won
                    return
                elif os == 4:
                    print(freeCell)
                    self.repo.placeSymbol(freeCell[0], freeCell[1], "x")
                    self.isWon()  # checking if the game is won
                    return

            # checking columns
            for j in range(6):
                xs = 0  # the number of x's
                os = 0  # the number of o's
                freeCell = (-1, -1)
                for i in range(5):
                    if self.repo.matrix[i][j] == 'x':
                        xs += 1
                    elif self.repo.matrix[i][j] == 'o':
                        os += 1
                    else:
                        freeCell = (i, j)  # in case when there are 4 identical symbols it will place here the other symbol

                if xs == 4:
                    print(freeCell)
                    self.repo.placeSymbol(freeCell[0], freeCell[1], "o")
                    self.isWon()  # checking if the game is won
                    return
                elif os == 4:
                    print(freeCell)
                    self.repo.placeSymbol(freeCell[0], freeCell[1], "x")
                    self.isWon()  # checking if the game is won
                    return

                for i in range(1, 6):
                    if self.repo.matrix[i][j] == 'x':
                        xs += 1
                    elif self.repo.matrix[i][j] == 'o':
                        os += 1
                    else:
                        freeCell = (i, j)  # in case when there are 4 identical symbols it will place here the other symbol

                if xs == 4:
                    print(freeCell)
                    self.repo.placeSymbol(freeCell[0], freeCell[1], "o")
                    self.isWon()  # checking if the game is won
                    return
                elif os == 4:
                    print(freeCell)
                    self.repo.placeSymbol(freeCell[0], freeCell[1], "x")
                    self.isWon()  # checking if the game is won
                    return

            # ----------checking diagonals 1-------------
            if True:
                #1
                if True:
                    xs = 0  # the number of x's
                    os = 0  # the number of o's
                    freeCell = (-1, -1)
                    I = 1
                    J = 0
                    for k in range(5):
                        if self.repo.matrix[I][J] == 'x':
                            xs += 1
                        elif self.repo.matrix[I][J] == 'o':
                            os += 1
                        else:
                            freeCell = (I, J)  # in case when there are 4 identical symbols it will place here the other symbol
                        I += 1
                        J += 1

                    if xs == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "o")
                        self.isWon()  # checking if the game is won
                        return
                    elif os == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "x")
                        self.isWon()  # checking if the game is won
                        return

                # 2
                if True:
                    xs = 0  # the number of x's
                    os = 0  # the number of o's
                    freeCell = (-1, -1)
                    I = 0
                    J = 0
                    for k in range(5):
                        if self.repo.matrix[I][J] == 'x':
                            xs += 1
                        elif self.repo.matrix[I][J] == 'o':
                            os += 1
                        else:
                            freeCell = (I, J)  # in case when there are 4 identical symbols it will place here the other symbol
                        I += 1
                        J += 1

                    if xs == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "o")
                        self.isWon()  # checking if the game is won
                        return
                    elif os == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "x")
                        self.isWon()  # checking if the game is won
                        return

                # 3
                if True:
                    xs = 0  # the number of x's
                    os = 0  # the number of o's
                    freeCell = (-1, -1)
                    I = 1
                    J = 1
                    for k in range(5):
                        if self.repo.matrix[I][J] == 'x':
                            xs += 1
                        elif self.repo.matrix[I][J] == 'o':
                            os += 1
                        else:
                            freeCell = (I, J)  # in case when there are 4 identical symbols it will place here the other symbol
                        I += 1
                        J += 1

                    if xs == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "o")
                        self.isWon()  # checking if the game is won
                        return
                    elif os == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "x")
                        self.isWon()  # checking if the game is won
                        return

                # 4
                if True:
                    xs = 0  # the number of x's
                    os = 0  # the number of o's
                    freeCell = (-1, -1)
                    I = 1
                    J = 1
                    for k in range(5):
                        if self.repo.matrix[I][J] == 'x':
                            xs += 1
                        elif self.repo.matrix[I][J] == 'o':
                            os += 1
                        else:
                            freeCell = (I, J)  # in case when there are 4 identical symbols it will place here the other symbol
                        I += 1
                        J += 1

                    if xs == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "o")
                        self.isWon()  # checking if the game is won
                        return
                    elif os == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "x")
                        self.isWon()  # checking if the game is won
                        return

            # ----------checking diagonals 2-------------
            if True:
                # 1'
                if True:
                    xs = 0  # the number of x's
                    os = 0  # the number of o's
                    freeCell = (-1, -1)
                    I = 4
                    J = 0
                    for k in range(5):
                        if self.repo.matrix[I][J] == 'x':
                            xs += 1
                        elif self.repo.matrix[I][J] == 'o':
                            os += 1
                        else:
                            freeCell = (I, J)  # in case when there are 4 identical symbols it will place here the other symbol
                        I -= 1
                        J += 1

                    if xs == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "o")
                        self.isWon()  # checking if the game is won
                        return
                    elif os == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "x")
                        self.isWon()  # checking if the game is won
                        return

                # 2'
                if True:
                    xs = 0  # the number of x's
                    os = 0  # the number of o's
                    freeCell = (-1, -1)
                    I = 5
                    J = 0
                    for k in range(5):
                        if self.repo.matrix[I][J] == 'x':
                            xs += 1
                        elif self.repo.matrix[I][J] == 'o':
                            os += 1
                        else:
                            freeCell = (I, J)  # in case when there are 4 identical symbols it will place here the other symbol
                        I -= 1
                        J += 1

                    if xs == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "o")
                        self.isWon()  # checking if the game is won
                        return
                    elif os == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "x")
                        self.isWon()  # checking if the game is won
                        return

                # 3'
                if True:
                    xs = 0  # the number of x's
                    os = 0  # the number of o's
                    freeCell = (-1, -1)
                    I = 4
                    J = 1
                    for k in range(5):
                        if self.repo.matrix[I][J] == 'x':
                            xs += 1
                        elif self.repo.matrix[I][J] == 'o':
                            os += 1
                        else:
                            freeCell = (I, J)  # in case when there are 4 identical symbols it will place here the other symbol
                        I -= 1
                        J += 1

                    if xs == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "o")
                        self.isWon()  # checking if the game is won
                        return
                    elif os == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "x")
                        self.isWon()  # checking if the game is won
                        return

                # 4'
                if True:
                    xs = 0  # the number of x's
                    os = 0  # the number of o's
                    freeCell = (-1, -1)
                    I = 5
                    J = 1
                    for k in range(5):
                        if self.repo.matrix[I][J] == 'x':
                            xs += 1
                        elif self.repo.matrix[I][J] == 'o':
                            os += 1
                        else:
                            freeCell = (I, J)  # in case when there are 4 identical symbols it will place here the other symbol
                        I -= 1
                        J += 1

                    if xs == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "o")
                        self.isWon()  # checking if the game is won
                        return
                    elif os == 4:
                        print(freeCell)
                        self.repo.placeSymbol(freeCell[0], freeCell[1], "x")
                        self.isWon()  # checking if the game is won
                        return

        # otherwise random move
        possibleMoves = []
        for i in range(6):
            for j in range(6):
                if self.repo.matrix[i][j] == " ":
                    possibleMoves.append((i , j))

        chosenMove = choice(possibleMoves)
        # placing a symbol that is rarer
        if self.repo.xs > self.repo.os:
            symbol = "o"
        else:
            symbol = "x"
        self.repo.placeSymbol(chosenMove[0], chosenMove[1], symbol)
        self.isWon()

    def isWon(self):

        #----Checking if the human won----
        # checking on rows
        for i in range(6):
            xs = 0  # the number of x's
            os = 0  # the number of o's
            for j in range(5):
                if self.repo.matrix[i][j] == 'x':
                    xs += 1
                elif self.repo.matrix[i][j] == 'o':
                    os += 1
            if xs == 5 or os == 5:
                raise EndOfGameException("The user one!!!")

            xs = 0  # the number of x's
            os = 0  # the number of o's
            for j in range(1, 6):
                if self.repo.matrix[i][j] == 'x':
                    xs += 1
                elif self.repo.matrix[i][j] == 'o':
                    os += 1
            if xs == 5 or os == 5:
                raise EndOfGameException("The user one!!!")

        # checking on collumns
        for j in range(6):
            xs = 0  # the number of x's
            os = 0  # the number of o's
            for i in range(5):
                if self.repo.matrix[i][j] == 'x':
                    xs += 1
                elif self.repo.matrix[i][j] == 'o':
                    os += 1
            if xs == 5 or os == 5:
                raise EndOfGameException("The user one!!!")

            xs = 0  # the number of x's
            os = 0  # the number of o's
            for i in range(1, 6):
                if self.repo.matrix[i][j] == 'x':
                    xs += 1
                elif self.repo.matrix[i][j] == 'o':
                    os += 1
            if xs == 5 or os == 5:
                raise EndOfGameException("The user one!!!")

        # checking on diagonal 1
        # 1
        if self.repo.matrix[0][1] == self.repo.matrix[1][2] == self.repo.matrix[2][3] == self.repo.matrix[3][4] == \
                self.repo.matrix[4][5] != " ":
            raise EndOfGameException("The user one!!!")
        # 2
        if self.repo.matrix[0][0] == self.repo.matrix[1][1] == self.repo.matrix[2][2] == self.repo.matrix[3][3] == \
                self.repo.matrix[4][4] != " ":
            raise EndOfGameException("The user one!!!")
        # 3
        if self.repo.matrix[5][5] == self.repo.matrix[1][1] == self.repo.matrix[2][2] == self.repo.matrix[3][3] == \
                self.repo.matrix[4][4] != " ":
            raise EndOfGameException("The user one!!!")
        # 4
        if self.repo.matrix[1][0] == self.repo.matrix[2][1] == self.repo.matrix[3][2] == self.repo.matrix[4][3] == \
                self.repo.matrix[5][4] != " ":
            raise EndOfGameException("The user one!!!")

        # checking on diagonal 2
        # 1'
        if self.repo.matrix[4][0] == self.repo.matrix[3][1] == self.repo.matrix[2][2] == self.repo.matrix[1][3] == \
                self.repo.matrix[0][4] != " ":
            raise EndOfGameException("The user one!!!")
        # 2'
        if self.repo.matrix[5][0] == self.repo.matrix[4][1] == self.repo.matrix[3][2] == self.repo.matrix[2][3] == \
                self.repo.matrix[1][4] != " ":
            raise EndOfGameException("The user one!!!")
        # 3'
        if self.repo.matrix[5][5] == self.repo.matrix[4][1] == self.repo.matrix[3][2] == self.repo.matrix[2][3] == \
                self.repo.matrix[1][4] != " ":
            raise EndOfGameException("The user one!!!")
        # 4'
        if self.repo.matrix[5][1] == self.repo.matrix[4][2] == self.repo.matrix[3][3] == self.repo.matrix[2][4] == \
                self.repo.matrix[1][5] != " ":
            raise EndOfGameException("The user one!!!")

        #----checking if the computer won----
        if self.repo.usedCells() >= 36:
            raise EndOfGameException("The computer won!")
