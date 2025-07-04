from controller import Controller
from repository import SentenceException


class UserInterface:
    def __init__(self, serivice: Controller):
        self.__service = serivice

    def __call__(self):

        while True:
            choice1 = input("""
            1 - Add a sentence to the list
            2 - Play the game
            >>>
            """)
            if choice1 == "1":
                newSentence = input("New sentence: ")
                try:
                    self.__service.addSentence(newSentence)
                except SentenceException as se:
                    print(se)

            elif choice1 == "2":
                sentence = self.__service.chooseSentence().strip()
                lettersFound = self.__service.firstLastLetters(sentence)
                outputSentence = self.__service.revealLetters(sentence, lettersFound)
                nrOfDistinctLetters = self.__service.distinctLetters(sentence)
                hangman = ""    #
                mistakes = 0
                hangmanSTR = "hangman"

                while True:
                    letterGuess = input(f"""
                    {outputSentence} - "{hangman}"
                    >>>""")
                    if letterGuess not in sentence or letterGuess in lettersFound:
                        hangman += hangmanSTR[mistakes]
                        mistakes += 1
                        if mistakes == 7:
                            print("User loses.")
                            return

                    else:
                        lettersFound += letterGuess
                        if len(lettersFound) == nrOfDistinctLetters:
                            print("User WOOON! Yeyy")
                        outputSentence = self.__service.revealLetters(sentence, lettersFound)
            else:
                print("Invalid command!")