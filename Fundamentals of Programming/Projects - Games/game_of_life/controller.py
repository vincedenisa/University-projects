from board import Board


class Controller:
    def __init__(self, file = "simulation.txt"):
        self.file = file
        self.board = Board()

    def displayGrid(self):
        return str(self.board)