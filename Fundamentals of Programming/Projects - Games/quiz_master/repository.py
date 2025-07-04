import unittest

from questionDomain import Question

class RepoException(Exception):
    pass

class Repository:
    def __init__(self, file="questionsList.txt"):
        self.questions = []
        self.difficulty = {"easy": 0, "medium": 0, "hard": 0}
        self.ids = []
        self.file = file
        self.loadFile()

    def __len__(self):
        return len(self.questions)

    def __str__(self):
        return str(self.questions)

    def loadFile(self):
        """
        Loads the questions from the file
        :return: nothing
        """
        with open(self.file, "r") as fin:
            for line in fin:
                tokens = line.split(";")
                id = int(tokens[0])
                text = tokens[1]
                choiceA = tokens[2]
                choiceB = tokens[3]
                choiceC = tokens[4]
                correctChoice = tokens[5]
                difficulty = tokens[6].strip()
                question = Question(id, text, choiceA, choiceB, choiceC, correctChoice, difficulty)
                self.difficulty[difficulty] += 1
                self.questions.append(question)
                self.ids.append(id)

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
        if id in self.ids:
            raise RepoException("Id already exists")
        question = Question(id, text, choiceA, choiceB, choiceC, correctChoice, difficulty)
        self.questions.append(question)
        self.difficulty[difficulty] += 1
        self.ids.append(id)
        self.saveFile()

    def saveFile(self):
        """
        Saves the questions to the file
        :return: nothing
        """
        with open(self.file, "w") as fout:
            for question in self.questions:
                fout.write(str(question) + "\n")

    def startTest(self, file):
        """
        Starts the test
        :param file: the file where the questions are
        :return: the list of questions
        """
        questions = []
        with open(file, "r") as fin:
            for line in fin:
                tokens = line.split(";")
                id = int(tokens[0])
                text = tokens[1]
                choiceA = tokens[2]
                choiceB = tokens[3]
                choiceC = tokens[4]
                correctChoice = tokens[5]
                difficulty = tokens[6].strip()
                question = [id, text, choiceA, choiceB, choiceC, correctChoice, difficulty]
                questions.append(question)
        return questions


class testRepo(unittest.TestCase):
    def setUp(self) -> None:
        with open("questionsTest.txt", "w") as fin:
            fin.write("1;Which number is the largest;1;4;3;4;easy" + "\n")
            fin.write("2;Which number is the smallest;-3;0;3;-3;easy" + "\n")
            fin.write("3;Which number is prime;2;32;9;2;easy" + "\n")
        self.repo = Repository("questionsTest.txt")

    def test_loadFile(self):
        """
        These are the questions from the file
        1;Which number is the largest;1;4;3;4;easy
        2;Which number is the smallest;-3;0;3;-3;easy
        3;Which number is prime;2;32;9;2;easy
        :return:
        """
        self.assertEqual(len(self.repo), 3)
        self.assertEqual(self.repo.difficulty["easy"], 3)
        self.assertEqual(self.repo.ids, [1, 2, 3])
        self.assertEqual(self.repo.questions[0].id, 1)
        self.assertEqual(self.repo.questions[0].text, "Which number is the largest")
        self.assertEqual(self.repo.questions[0].choiceA, "1")
        self.assertEqual(self.repo.questions[0].choiceB, "4")
        self.assertEqual(self.repo.questions[0].choiceC, "3")
        self.assertEqual(self.repo.questions[0].correctChoice, "4")
        self.assertEqual(self.repo.questions[0].difficulty, "easy")
        self.assertEqual(self.repo.questions[1].id, 2)
        self.assertEqual(self.repo.questions[1].text, "Which number is the smallest")
        self.assertEqual(self.repo.questions[1].choiceA, "-3")
        self.assertEqual(self.repo.questions[1].choiceB, "0")
        self.assertEqual(self.repo.questions[1].choiceC, "3")
        self.assertEqual(self.repo.questions[1].correctChoice, "-3")
        self.assertEqual(self.repo.questions[1].difficulty, "easy")
        self.assertEqual(self.repo.questions[2].id, 3)
        self.assertEqual(self.repo.questions[2].text, "Which number is prime")
        self.assertEqual(self.repo.questions[2].choiceA, "2")
        self.assertEqual(self.repo.questions[2].choiceB, "32")
        self.assertEqual(self.repo.questions[2].choiceC, "9")
        self.assertEqual(self.repo.questions[2].correctChoice, "2")
        self.assertEqual(self.repo.questions[2].difficulty, "easy")

    def test_addQuestion(self):
        self.repo.addQuestion(4, "What is the capital of Romania?", "Bucharest", "Cluj", "Iasi", "Bucharest", "easy")
        self.assertEqual(len(self.repo), 4)
        self.assertEqual(self.repo.difficulty["easy"], 4)
        self.assertEqual(self.repo.ids, [1, 2, 3, 4])
        self.assertEqual(self.repo.questions[3].id, 4)
        self.assertEqual(self.repo.questions[3].text, "What is the capital of Romania?")
        self.assertEqual(self.repo.questions[3].choiceA, "Bucharest")
        self.assertEqual(self.repo.questions[3].choiceB, "Cluj")
        self.assertEqual(self.repo.questions[3].choiceC, "Iasi")
        self.assertEqual(self.repo.questions[3].correctChoice, "Bucharest")
        self.assertEqual(self.repo.questions[3].difficulty, "easy")



    def test_startTest(self):
        questions = self.repo.startTest("questionsTest.txt")
        self.assertEqual(len(questions), 3)
        self.assertEqual(questions[0][0], 1)
        self.assertEqual(questions[0][1], "Which number is the largest")
        self.assertEqual(questions[0][2], "1")
        self.assertEqual(questions[0][3], "4")
        self.assertEqual(questions[0][4], "3")
        self.assertEqual(questions[0][5], "4")
        self.assertEqual(questions[0][6], "easy")
        self.assertEqual(questions[1][0], 2)
        self.assertEqual(questions[1][1], "Which number is the smallest")
        self.assertEqual(questions[1][2], "-3")
        self.assertEqual(questions[1][3], "0")
        self.assertEqual(questions[1][4], "3")
        self.assertEqual(questions[1][5], "-3")
        self.assertEqual(questions[1][6], "easy")
        self.assertEqual(questions[2][0], 3)
        self.assertEqual(questions[2][1], "Which number is prime")
        self.assertEqual(questions[2][2], "2")
        self.assertEqual(questions[2][3], "32")
        self.assertEqual(questions[2][4], "9")
        self.assertEqual(questions[2][5], "2")
        self.assertEqual(questions[2][6], "easy")
