from TextRepo import FlightTextRepo
from services import FlightsService
from user_interface import UserInterface

if __name__ == "__main__":
    textRepo = FlightTextRepo()
    services = FlightsService(textRepo)
    userInterface = UserInterface(services)
    userInterface()