from TextRepo import FlightException
from services import FlightsService
from datetime import datetime

class UserInterface:
    def __init__(self, service: FlightsService):
        self._service = service

    def __call__(self):


        while True:
            choise = input("""
            1 - add a flight
            2 - delete a flight
            3 - list the airports in descending order of their operations
            4 - list the no flights time
            5 - determine the maximum number of flights with a single radar   
            x - exit
            >>>         
            """)

            if choise == "1":
                try:
                    id = input("id: ")

                    departure_city = input("departure city: ")
                    departure_timeStr = input("departure time (%H:%M): ")
                    departure_time = datetime.strptime(departure_timeStr.strip(), "%H:%M").time()

                    arrival_city = input("arrival city: ")
                    arrival_timeStr = input("arrival time (%H:%M): ")
                    arrival_time = datetime.strptime(arrival_timeStr.strip(), "%H:%M").time()

                    self._service.add_flight(id, departure_city, departure_time, arrival_city, arrival_time)

                except FlightException as fe:
                    print(fe)

            elif choise == "2":
               try:
                   id = input("id: ")
                   self._service.delete_flight(id)
               except FlightException as fe:
                   print(fe)


            elif choise == "3":
                print(self._service.list_airports())

            elif choise == "4":
                pass
            elif choise == "5":
                print(self._service.determine_max_flights())
            elif choise == "x":
                return
            else:
                print("Invalid command. Try again!")