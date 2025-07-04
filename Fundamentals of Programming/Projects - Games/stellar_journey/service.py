import unittest

from board import Board, BoardErrors


class EndOfGame(Exception):
    pass


class Game:
    def __init__(self):
        self.board = Board()
        self.board.placeStars()
        self.board.firstPlaceEndeavor()
        self.board.firstPlaceBlingons()

    def displayBoard(self):
        return str(self.board)

    def cheatShowFullBoard(self):
        return self.board.cheatShowFullBoard()

    def warp(self, ito: int, jto: int):
        """
        This function moves the player to the desired position
        :param ito: the row where the player wants to warp
        :param jto: the column where the player wants to warp
        :return: nothing
        """
        if ito == self.board.Endeavour[0]:
            for j in range(min(ito, self.board.Endeavour[0]), max(ito, self.board.Endeavour[0]) + 1):
                if (ito, j) in self.board.stars:
                    raise BoardErrors("You cannot go through a star!")
            if (ito, jto) in self.board.Blingons:
                raise EndOfGame("You've lost! You have landed on a Blingon cruise.")
            self.board.Endeavour = (ito, jto)

        elif jto == self.board.Endeavour[1]:
            for i in range(min(ito, self.board.Endeavour[1]), max(ito, self.board.Endeavour[1]) + 1):
                if (i, jto) in self.board.stars:
                    raise BoardErrors("You cannot go through a star!")
            if (ito, jto) in self.board.Blingons:
                raise EndOfGame("You've lost! You have landed on a Blingon cruise.")
            self.board.Endeavour = (ito, jto)

        elif abs(ito - jto) == abs(self.board.Endeavour[0] - self.board.Endeavour[1]):
            if ito == jto:
                if ito > self.board.Endeavour[0]:
                    for i in range(self.board.Endeavour[0], ito + 1):
                        if (i, i) in self.board.stars:
                            raise BoardErrors("You cannot go through a star!")
                    if (ito, jto) in self.board.Blingons:
                        raise EndOfGame("You've lost! You have landed on a Blingon cruise.")
                    self.board.Endeavour = (ito, jto)
                else:
                    for i in range(ito, self.board.Endeavour[0] + 1):
                        if (i, i) in self.board.stars:
                            raise BoardErrors("You cannot go through a star!")
                    if (ito, jto) in self.board.Blingons:
                        raise EndOfGame("You've lost! You have landed on a Blingon cruise.")
                    self.board.Endeavour = (ito, jto)
            else:
                i = ito
                j = jto
                if ito > self.board.Endeavour[0]:
                    while i > self.board.Endeavour[0]:
                        if (i, j) in self.board.stars:
                            raise BoardErrors("You cannot go through a star!")
                        i -= 1
                        j += 1
                        if (ito, jto) in self.board.Blingons:
                            raise EndOfGame("You've lost! You have landed on a Blingon cruise.")
                        self.board.Endeavour = (ito, jto)
                else:
                    while i < max(ito, self.board.Endeavour[0]):
                        if (i, j) in self.board.stars:
                            raise BoardErrors("You cannot go through a star!")
                        i += 1
                        j -= 1
                if (ito, jto) in self.board.Blingons:
                    raise EndOfGame("You've lost! You have landed on a Blingon cruise.")
                self.board.Endeavour = (ito, jto)

        else:
            raise BoardErrors("You can't warp the Endeavour on that position!")

    def fire(self, i: int, j: int):
        if (i + 1, j + 1) != self.board.Endeavour and (i - 1, j - 1) != self.board.Endeavour and (
        i + 1, j - 1) != self.board.Endeavour and (i - 1, j + 1) != self.board.Endeavour and (
        i, j + 1) != self.board.Endeavour and (i, j - 1) != self.board.Endeavour and (
        i + 1, j) != self.board.Endeavour and (i - 1, j) != self.board.Endeavour:
            raise BoardErrors("You can fire only to adiacent positions!")
        if (i, j) in self.board.Blingons:
            self.board.Blingons.remove((i, j))
            if len(self.board.Blingons) == 0:
                raise EndOfGame("You've won! You have destroyed all the Blingon ships!")
            self.board.replaceBlingonsLeft()
            return f"You've destroyed a Blingon ship! You have {len(self.board.Blingons)} left!"
        else:
            return "You've missed!"


class testController(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Game()
        self.game.board.stars = [(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)]
        self.game.board.Blingons = [(5, 2), (5, 4), (5, 6)]
        self.game.board.Endeavour = (5, 8)

    def testWrap(self):
        try:
            self.game.warp(5, 6)
            assert False
        except EndOfGame:
            assert True

        try:
            self.game.warp(4, 3)
            assert False
        except BoardErrors:
            assert True

        self.game.warp(8, 8)
        self.assertEqual(self.game.board.Endeavour, (8, 8))