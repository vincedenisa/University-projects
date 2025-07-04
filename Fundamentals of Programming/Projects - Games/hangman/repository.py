

class SentenceException(Exception):
    pass

class RepoTextFile:
    def __init__(self, fileName = "sentences.txt"):
        self.__sentences = []
        self.__file = fileName
        self.loadFile()

    def loadFile(self):
        """
        Loads the sentences from the text file
        :return:
        """
        with open(self.__file, "r") as fin:
            for line in fin:
                self.__sentences.append(line)

    def addSentence(self, newSentence: str):
        """
        Adds a sentence to the list
        :param newSentence: the new sentence
        :return: -
        """
        # validation 1
        if len(newSentence.strip()) < 3:
            raise SentenceException("Each sentence must consist of at least 1 word. Every word must have at least 3 letters.")

        # validation 2
        words = newSentence.split(" ")
        for word in words:
            if len(word) < 3 and word != "":
                raise SentenceException("Every word must have at least 3 letters.")

        # validation 3
        if newSentence in self.__sentences:
            raise SentenceException("This sentence is already in the list!")

        # adding the sentence
        self.__sentences.append(newSentence)

        # adding to the file
        with open(self.__file, "a") as fap:
            fap.write(newSentence + "\n")

    def getAllSentences(self):
        """
        Return all sentences
        :return: list with all sentences
        """
        return self.__sentences
