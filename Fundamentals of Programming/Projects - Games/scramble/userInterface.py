from controller import Controller




class UserInterface:
    def __init__(self, repoFile= "sentences.txt"):
        self.service = Controller(repoFile)

    def __call__(self):
        sentence = self.service.selectSentence().strip()
        Scrambled = self.service.scrambleSentence(sentence)
        contor = self.service.nrOfLetters(sentence)
        undo = None
        print("""Commands:
        swap <nrOfWord1> <letterFromWord1> - <nrOfWord2> <letterFromWord2>
        undo (To undo the last swap)
        """)

        while True:
            if contor <= 0:
                print("You have lost!")
                return
            if Scrambled == sentence:
                print("You have won!")
                return
            command = input(f"{Scrambled} [score is: {contor}]\n"
                            f">>>")
            tokens = command.split(" ")
            # remove empty strings - in case the user introduced more spaces than needed
            for token in tokens:
                if token == "":
                    tokens.remove(token)

            if tokens[0] == "swap":
                if len(tokens) != 6:
                    print("Invalid command - not enough arguments.")
                    continue
                try:
                    word1 = int(tokens[1])
                    letter1 = int(tokens[2])
                    word2 = int(tokens[4])
                    letter2 = int(tokens[5].strip())    # because it will have "\n" at the end
                    if letter1 == 0 or letter2 == 0:
                        print("The first and last letter of every word cannot be changed.")
                    try:
                        notScrambled = Scrambled
                        Scrambled = self.service.changeLetters(Scrambled, word1, letter1, word2, letter2)
                        undo = notScrambled
                        contor -= 1
                    except Exception as e:
                        print(e)
                except Exception as e:
                    print(f"Invalid command - {e}")

            elif tokens[0] == "undo":
                Scrambled = undo

            else:
                print("Invalid command!")
                continue