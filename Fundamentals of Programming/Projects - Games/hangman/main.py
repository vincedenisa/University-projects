from controller import Controller
from repository import RepoTextFile
from userInterface import UserInterface

if __name__ == "__main__":
    #initialising the classes
    repo = RepoTextFile()
    service = Controller(repo)
    userInterface = UserInterface(service)

    #calling the user interface
    userInterface()