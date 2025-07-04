import unittest

from repository import RepoTextFile


class TestsRepoTextFile(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = RepoTextFile("testSentences.txt")

    def testLoadFile(self):
        sentencesTest = []
        with open("testSentences.txt", "r") as fin:
            for line in fin:
                sentencesTest.append(line)
        sentencesRepo = self.repo.getAllSentences()

        self.assertEqual(len(sentencesTest), len(sentencesRepo))
        for i in range(len(sentencesTest)):
            self.assertEqual(sentencesTest[i], sentencesRepo[i])

    def testAddSentence(self):
        self.repo.addSentence("testing the addSentence")
        self.assertEqual(self.repo.getAllSentences()[-1], "testing the addSentence")

    def testGetAllSentences(self):
        sentencesTest = []
        with open("testSentences.txt", "r") as fin:
            for line in fin:
                sentencesTest.append(line)
        sentencesRepo = self.repo.getAllSentences()
        self.assertEqual(len(sentencesTest), len(sentencesRepo))
        for i in range(len(sentencesTest)):
            self.assertEqual(sentencesTest[i], sentencesRepo[i])