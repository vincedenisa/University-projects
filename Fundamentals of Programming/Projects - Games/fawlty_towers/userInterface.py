from datetime import datetime, date

from services import Services


class UserInterface:
    def __init__(self, resFile= "reservations.txt", roomsFile="rooms.txt"):
        self.services = Services(resFile, roomsFile)

    def __call__(self):
        while True:
            choice = input("""
            1 - create a room reservation
            2 - delete reservation
            3 - show available rooms
            4 - monthly report
            5 - day of week report
            >>>
            """)
            if choice == "1":
                name = input("Name: ")
                if name == "":
                    print("The name is empty. Try again.")
                    continue

                type = int(input("""
                1 - single room
                2 - double room
                4 - family room
                """))
                if type not in [1, 2, 4]:
                    print("Invalid type.")
                    continue

                nrGuests = int(input("Number of guests: "))
                if nrGuests < 1 or nrGuests > 4:
                    print("Number of Guests must be between 1 and 4.")
                    continue
                if nrGuests > type:
                    print("Too many guests for this type. Try another type.")
                    continue

                arrivalStr = input("Arrival date (%d.%m):")
                arrivalDate = datetime.strptime(arrivalStr, "%d.%m").date()
                arrivalDate = date(2018, arrivalDate.month, arrivalDate.day)

                departureStr = input("Departure date (%d.%m):")
                departureDate = datetime.strptime(departureStr, "%d.%m").date()
                departureDate = date(2018, departureDate.month, departureDate.day)

                if arrivalDate > departureDate:
                    print("The arrival date is bigger than departure date. Try again.")
                    continue

                roomNr = self.services.freeRooms(type, arrivalDate, departureDate)
                if roomNr == False:
                    print("There are no rooms of this type on that period. Please try again with another type or another period.")
                    continue
                self.services.createReservation(roomNr, name, nrGuests, arrivalDate, departureDate)
            elif choice == "2":
                id = input("Id of the reservation: ")
                try:
                    self.services.deleteReservation(id)
                    print(f"Reservation {id} was deleted succesfully.")
                except Exception as e:
                    print(e)
            elif choice == "3":
                arrivalStr = input("Arrival date (%d.%m):")
                arrivalDate = datetime.strptime(arrivalStr, "%d.%m").date()
                arrivalDate = date(2018, arrivalDate.month, arrivalDate.day)

                departureStr = input("Departure date (%d.%m):")
                departureDate = datetime.strptime(departureStr, "%d.%m").date()
                departureDate = date(2018, departureDate.month, departureDate.day)
                print(self.services.availableRooms(arrivalDate, departureDate))
            elif choice == "4":
                print(self.services.monthlyReport())
            elif choice == "5":
                print(self.services.dayOfWeekReport())
            else:
                print("Invalid command.")