from datetime import date, timedelta
from services import Services
from room import Room
from reservationsRepo import ReservationsRepo
from reservation import Reservation


class UserInterface:
    def __init__(self, resFile = "reservations.txt", roomsFile = "rooms.txt"):
        self.services = Services(resFile, roomsFile)

    def __call__(self):
        while True:
            choice = input("""
            1. Create a new reservation
            2. Delete a reservation
            3. Show available rooms
            4. Exit
            >>>""")
            if choice == "1":
                name = input("Enter reservation name: ")
                if name =="":
                    print("Please enter a valid reservation name")
                    continue
                type = int(input("""
                1- single room
                2 - double room
                3 - family room
                >>>"""))
                if type not in [1, 2, 3]:
                    print("Please enter a valid reservation type")
                    continue
                nrGuests = input("How many guests do you have? ")
                if nrGuests < 1 or nrGuests > 4:
                    print("Please enter a valid number of guests")
                    continue
                if nrGuests > type:
                    print("Too many guests for this type of room")
                    continue
                arrStr = input("Arrival date (%d.%m.%Y): ")
                arrDate = datetime.strptime(arrStr, "%d.%m.%Y").date()
                arrDate = date(arrDate.year, arrDate.month, arrDate.day)

                depStr = input("Departure date (%d.%m.%Y): ")
                depDate = datetime.strptime(depStr, "%d.%m.%Y").date()
                depDate = date(depDate.year, depDate.month, depDate.day)

                if arrDate > depDate:
                    print("The arrival date is after the departure")
                    continue


