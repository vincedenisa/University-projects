

class Question:
    def __init__(self, id: int, text: str, choiceA: str, choiceB: str, choiceC: str, correctChoice: str, difficulty: str):
        self.id = id
        self.text = text
        self.choiceA = choiceA
        self.choiceB = choiceB
        self.choiceC = choiceC
        self.correctChoice = correctChoice
        self.difficulty = difficulty

    def __str__(self):
        return f"{self.id};{self.text};{self.choiceA};{self.choiceB};{self.choiceC};{self.correctChoice};{self.difficulty}"