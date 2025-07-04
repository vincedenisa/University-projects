from random import choice


class Repository:
    def __init__(self, repoFile="sentences.txt"):
        self.repoFile = repoFile
        self.sentences = []
        self.loadFile()

    def loadFile(self):
        with open(self.repoFile, 'r') as f:
            for line in f:
                self.sentences.append(line)

    def selectSentence(self):
        return choice(self.sentences)