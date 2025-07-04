import unittest
from random import choice

from repository import Repository


class Controller:
    def __init__(self):
        self.repo = Repository()

    def addQuestion(self, id, text, choiceA, choiceB, choiceC, correctChoice, difficulty):
        """
        Adds a question to the repository
        :param id: the id of the question
        :param text: the text of the question
        :param choiceA: the first choice
        :param choiceB: the second choice
        :param choiceC: the third choice
        :param correctChoice: the correct choice
        :param difficulty: the difficulty of the question
        :return: nothing
        """
        self.repo.addQuestion(id, text, choiceA, choiceB, choiceC, correctChoice, difficulty)

    def createTest(self, difficulty: str, number: int, file: str):
        """
        Creates a test with the given difficulty and number of questions
        :param difficulty: the difficulty of the questions
        :param number: the number of questions
        :param file: the file where the questions will be written
        :return: nothing
        """
        if self.repo.difficulty[difficulty] < (number // 2):
            raise Exception("Not enough questions of this difficulty")
        queThatDiff = []
        queOtherDiff = []
        for que in self.repo.questions:
            if que.difficulty == difficulty:
                queThatDiff.append(que)
            else:
                queOtherDiff.append(que)

        finalQue = []
        if len(queThatDiff) >= number:
            while len(finalQue) < number:
                que = choice(queThatDiff)
                queThatDiff.remove(que)
        else:
            finalQue = queThatDiff
            while len(finalQue) < number:
                que = choice(queOtherDiff)
                finalQue.append(que)
                queOtherDiff.remove(que)

        with open(file, "w") as fout:
            for que in finalQue:
                fout.write(str(que) + "\n")

    def startTest(self, file):
        """
        Starts the test
        :param file: the file where the questions are
        :return: the list of questions
        """
        return self.repo.startTest(file)


class testController(unittest.TestCase):
    def setUp(self) -> None:
        with open("questionsTest.txt", "w") as fin:
            fin.write("1;Which number is the largest;1;4;3;4;easy" + "\n")
            fin.write("2;Which number is the smallest;-3;0;3;-3;easy" + "\n")
            fin.write("3;Which number is prime;2;32;9;2;easy" + "\n")
        self.repo = Repository("questionsTest.txt")

    def testAddQuestion(self):
        self.repo.addQuestion(4, "Which number is the largest", "1", "4", "3", "4", "easy")
        self.assertEqual(len(self.repo.questions), 4)
        self.assertEqual(self.repo.difficulty["easy"], 4)
        self.assertEqual(self.repo.ids, [1, 2, 3, 4])

    def testCreateTest(self):
        self.repo.addQuestion(4, "Which number is the largest", "1", "4", "3", "4", "easy")
        self.repo.addQuestion(5, "Which number is the largest", "1", "4", "3", "4", "easy")


