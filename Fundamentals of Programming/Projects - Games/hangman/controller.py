from repository import RepoTextFile
from random import choice

class Controller:
    def __init__(self, repo: RepoTextFile):
        self.__repo = repo

    def addSentence(self, newSentence: str):
        """
        Adds a sentence to the list
        :param newSentence: the new sentence
        :return: -
        """
        self.__repo.addSentence(newSentence)

    def getAllSentences(self):
        """
        Return all sentences
        :return: list with all sentences
        """
        return self.__repo.getAllSentences()

    def firstLastLetters(self, sentence: str):
        """
        Find the first & last letters of the words in a sentence
        :param sentence: a sentence
        :return: a string with all the first & last letters
        """
        FLletters = ""      #firstLastLetters
        words = sentence.split(" ")
        for word in words:
            if word[0] not in FLletters:
                FLletters += word[0]
            if word.strip()[-1] not in FLletters:
                FLletters += word[-1]

        return FLletters

    def chooseSentence(self):
        sentence = choice(self.__repo.getAllSentences())
        return sentence

    def revealLetters(self, sentence, letters):
        outputSentence = ""
        for i in range(len(sentence)):
            if sentence[i] not in letters and sentence[i] != " ":
                outputSentence += "_"
            else:
                outputSentence += sentence[i]

        return outputSentence

    def distinctLetters(self, sentence):
        DistinctLetters = ""
        for letter in sentence:
            if letter not in DistinctLetters and letter != " ":
                DistinctLetters += letter

        return len(DistinctLetters)
