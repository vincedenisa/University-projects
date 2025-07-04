from controller import Controller


class UserInterface:
    def __init__(self, saveLoadFile = "simulation.txt"):
        self.service = Controller(saveLoadFile)

    def __call__(self):
        while True:
            print(self.service.displayGrid())