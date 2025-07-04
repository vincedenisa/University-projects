from controller import Controller
from repository import RepoException


class UserInterface:
    def __init__(self):
        self.service = Controller()

    def __call__(self):
        print("""
        Commands:
        add <id>;<text>; <choiceA>; <choiceB>; <choiceC>; <correctChoice>; <difficulty>
        create <difficulty> <number_of_question> <file_name>
        start <file_name>
        """)
        while True:
            command = input(">>>")
            tokens = command.split(" ", maxsplit=1)
            if tokens[0] == "add":
                properties = tokens[1].split(";")
                try:
                    id = int(properties[0].strip())
                    text = properties[1].strip()
                    choiceA = properties[2].strip()
                    choiceB = properties[3].strip()
                    choiceC = properties[4].strip()
                    correctChoice = properties[5].strip()
                    difficulty = properties[6].strip()
                    if difficulty not in ["easy", "medium", "hard"]:
                        print("Invalid difficulty")
                        continue
                    self.service.addQuestion(id, text, choiceA, choiceB, choiceC, correctChoice, difficulty)
                except RepoException as re:
                    print(re)
                except Exception as e:
                    print(f"Invalid command - {e}")

            elif tokens[0] == "create":
                try:
                    properties = tokens[1].split(" ")
                    difficulty = properties[0].strip()
                    if difficulty not in ["easy", "medium", "hard"]:
                        print("Invalid difficulty")
                        continue
                    number = int(properties[1].strip())
                    file = properties[2].strip()
                    self.service.createTest(difficulty, number, file)
                except Exception as e:
                    print(e)
            elif tokens[0] == "start":
                try:
                    file = tokens[1].strip()
                    score = 0
                    totalScore = 0
                    questions = self.service.startTest(file)
                    wrong = []
                    for que in questions:
                        print(que[1])
                        print(que[2])
                        print(que[3])
                        print(que[4])
                        answer = input(">>>")
                        if que[6] == "easy":
                            totalScore += 1
                            if answer == que[5]:
                                score += 1
                            else:
                                wrong.append(que)
                        elif que[6] == "medium":
                            totalScore += 2
                            if answer == que[5]:
                                score += 2
                            else:
                                wrong.append(que)
                        elif que[6] == "hard":
                            totalScore += 3
                            if answer == que[5]:
                                score += 3
                            else:
                                wrong.append(que)
                    print(f"""Your score is {score}/{totalScore}""")
                    if len(wrong) > 0:
                        print("Wrong answers:")
                        for que in wrong:
                            print(que[1] )
                            print(f"-{que[2]} -{que[3]} -{que[4]}")
                            print(f"Correct answer: {que[5]}")
                except Exception as e:
                    print(e)
