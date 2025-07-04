import unittest

from controller import Controller
from repository import RepoTextFile


class TestsController(unittest.TestCase):
    def setUp(self) -> None:
        repo = RepoTextFile("testSentences.txt")
        self.service = Controller(repo)

    def testAddSentence(self):
        sentencesTest = []
        with open("testSentences.txt", "r") as fin:
            for line in fin:
                sentencesTest.append(line)
        sentencesRepo = self.service.getAllSentences()

        self.assertEqual(len(sentencesTest), len(sentencesRepo))
        for i in range(len(sentencesTest)):
            self.assertEqual(sentencesTest[i], sentencesRepo[i])

    def testFirstLastLetters(self):

        self.assertEqual(self.service.firstLastLetters("beautiful weather"), "blwr")

    def testChooseSentence(self):

        self.assertNotEqual(self.service.chooseSentence(), None)

    def testRevealLetters(self):

        self.assertEqual(self.service.revealLetters("beautiful", "bl"), "b_______l")

    def testDistinctLetters(self):

        self.assertEqual(self.service.distinctLetters("beautiful"), 8)