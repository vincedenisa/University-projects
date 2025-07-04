from texttable import Texttable

class Board:
    def __init__(self):
        self.grid = []

    def __str__(self):
        table = Texttable()
        for i in range(1, 9):
            row = []
            for j in range(1, 9):
                if (i, j) in self.grid:
                    row.append("x")
                else:
                    row.append(" ")
            table.add_row(row)

        return table.draw() + "\n"