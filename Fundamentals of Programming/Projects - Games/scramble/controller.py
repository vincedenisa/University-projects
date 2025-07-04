import unittest
from random import choice

from repository import Repository


class Controller:
    def __init__(self, repoFile="sentences.txt"):
        self.repoFile = repoFile
        self.repo = Repository(repoFile)

    def selectSentence(self):
        """
        Randomly selects a sentence from the file.
        :return: the sentence
        """
        return self.repo.selectSentence()

    def scrambleSentence(self, sentence: str):
        """
        Scrambles the sentence.
        :param sentence: the sentence to be scrambled
        :return: the scrambled sentence
        """
        scrambled = ""
        letters = []
        for i in range(len(sentence)-1):
            if sentence[i] != " " and i != 0 and i != len(sentence) and sentence[i-1] != " " and sentence[i+1] != " ":
                letters.append(sentence[i])
                scrambled += "_"
            else:
                scrambled += sentence[i]
        scrambled += sentence[-1]
        result = ""
        for let in scrambled:
            if let == "_":
                let = choice(letters)
                result += let
                letters.remove(let)
            else:
                result += let

        return result

    def nrOfLetters(self, sentence: str):
        """
        Counts the number of letters in a sentence.
        :param sentence:  the sentence
        :return: number of letters
        """
        contor = 0
        for let in sentence:
            contor += (let != " ")

        return contor - 1 # because it also counts the "\n"

    def changeLetters(self, sentence: str, word1: int, letter1: int, word2: int, letter2: int):
        """
        Changes the letters from the sentence.
        :param sentence: the sentence
        :param word1: position of the first word
        :param letter1: position of the first letter
        :param word2: position of the second word
        :param letter2: position of the second letter
        :return: the changed sentence
        """
        words = sentence.split(" ")
        if letter1 == len(words[word1]) - 1 or letter2 == len(words[word2]):
            raise ValueError("The first and last letter of every word cannot be changed.")
        if word1 == word2:
            words[word1] = self.swapLettersInWord(words[word1], letter1, letter2)
        else:
            words[word1], words[word2] = self.swapLetters(words[word1], letter1, words[word2], letter2)

        newSentence = ""
        for word in words:
            newSentence += word + " "
        newSentence = newSentence.strip()
        return newSentence

    def swapLetters(self, word1: str, letter1: int, word2: str, letter2: int):
        """
        Swaps the letters from the words.
        :param word1: position of the first word
        :param letter1: position of the first letter
        :param word2: position of the second word
        :param letter2: position of the second letter
        :return: swapped words
        """
        newWord1 = ""
        newWord2 = ""
        for i in range(len(word1)):
            if i != letter1:
                newWord1 += word1[i]
            else:
                newWord1 += word2[letter2]

        for i in range(len(word2)):
            if i != letter2:
                newWord2 += word2[i]
            else:
                newWord2 += word1[letter1]

        return newWord1, newWord2

    def swapLettersInWord(self, word: str, letter1:int, letter2: int):
        newWord = ""
        for i in range(len(word)):
            if i == letter1:
                newWord += word[letter2]
            elif i == letter2:
                newWord += word[letter1]
            else:
                newWord += word[i]

        return newWord


if __name__ == "__main__":
    service = Controller()
    word1 = "AnaMaria"
    word2 = "John"
    print(service.swapLetters(word1, 3,word2, 2))