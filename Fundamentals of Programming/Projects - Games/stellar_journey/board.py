from random import choice

from texttable import Texttable

class BoardErrors(Exception):
    pass

class Board:
    def __init__(self):
        self.stars = []
        self.Endeavour = (-1, -1)
        self.Blingons = []

    def __str__(self):
        table = Texttable()
        table.header([0, 1, 2, 3, 4, 5, 6, 7, 8])
        letters = ["/", "A", "B", "C", "D", "E", "F", "G", "H"]
        for i in range(1, 9):
            row = [letters[i]]
            for j in range(1, 9):
                if (i, j) in self.stars:
                    row.append("*")
                elif (i, j) == self.Endeavour:
                    row.append("E")
                elif (i, j) in self.Blingons and (
                        self.Endeavour == (i + 1, j + 1) or self.Endeavour == (i - 1, j - 1) or self.Endeavour == (
                i + 1, j - 1) or self.Endeavour == (i - 1, j + 1) or self.Endeavour == (i, j + 1) or self.Endeavour == (
                        i, j - 1) or self.Endeavour == (i + 1, j) or self.Endeavour == (i - 1, j)):
                    row.append("B")
                else:
                    row.append(" ")

            table.add_row(row)
        return table.draw() + "\n"

    def cheatShowFullBoard(self):
        table = Texttable()
        table.header([0, 1, 2, 3, 4, 5, 6, 7, 8])
        letters = ["/", "A", "B", "C", "D", "E", "F", "G", "H"]
        for i in range(1, 9):
            row = [letters[i]]
            for j in range(1, 9):
                if (i, j) in self.stars:
                    row.append("*")
                elif (i, j) == self.Endeavour:
                    row.append("E")
                elif (i, j) in self.Blingons:
                    row.append("B")
                else:
                    row.append(" ")

            table.add_row(row)
        return table.draw() + "\n\n"

    def placeStars(self):
        places = []
        for i in range(1, 9):
            for j in range(1, 9):
                places.append((i, j))

        while len(self.stars) < 10:
            i, j = choice(places)
            if (i, j) in self.stars or (i + 1, j) in self.stars or (i - 1, j) in self.stars or (
            i, j + 1) in self.stars or (i, j - 1) in self.stars or (i + 1, j + 1) in self.stars or (
            i - 1, j - 1) in self.stars or (i + 1, j - 1) in self.stars or (i - 1, j + 1) in self.stars:
                continue
            else:
                self.stars.append((i, j))

    def firstPlaceEndeavor(self):
        places = []
        for i in range(1, 9):
            for j in range(1, 9):
                if (i, j) not in self.stars:
                    places.append((i, j))
        self.Endeavour = choice(places)

    def firstPlaceBlingons(self):
        # place 3 blingons
        places = []
        for i in range(1, 9):
            for j in range(1, 9):
                if (i, j) not in self.stars and (i, j) != self.Endeavour:
                    places.append((i, j))

        while len(self.Blingons) < 3:
            i, j = choice(places)
            if (i, j) not in self.Blingons:
                self.Blingons.append((i, j))

    def replaceBlingonsLeft(self):
        # place blingons left
        blingonsLeft = len(self.Blingons)
        self.Blingons = []  # clear blingons
        places = []
        for i in range(1, 9):
            for j in range(1, 9):
                if (i, j) not in self.stars and (i, j) != self.Endeavour:
                    places.append((i, j))

        while len(self.Blingons) < blingonsLeft:
            i, j = choice(places)
            if (i, j) not in self.Blingons:
                self.Blingons.append((i, j))


if __name__ == "__main__":
    board = Board()
    board.placeStars()
    board.firstPlaceEndeavor()
    board.firstPlaceBlingons()
    print(board)