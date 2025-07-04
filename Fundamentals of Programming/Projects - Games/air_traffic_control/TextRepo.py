from datetime import datetime

from domain import Flight


class FlightException(Exception):
    pass


class FlightTextRepo:
    def __init__(self, file="flights.txt"):
        self.__file = file
        self.flights = []
        self.airports = {}
        self.load_file()

    def load_file(self):
        with open(self.__file, "r") as fin:
            for line in fin:
                tokens = line.split(",")
                id = tokens[0].strip()
                departure_city = tokens[1].strip()
                departure_time = datetime.strptime(tokens[2].strip(), "%H:%M").time()
                arrival_city = tokens[3]
                arrival_time = datetime.strptime(tokens[4].strip(), "%H:%M").time()

                # adding the flight
                flight = Flight(id, departure_city, departure_time, arrival_city, arrival_time)
                self.flights.append(flight)

                # adding the time to the airports
                if departure_city not in self.airports:
                    self.airports[departure_city] = [departure_time]
                else:
                    self.airports[departure_city].append(departure_time)

                if arrival_city not in self.airports:
                    self.airports[arrival_city] = [arrival_time]
                else:
                    self.airports[arrival_city].append(arrival_time)

    def save_file(self):
        with open(self.__file, "w") as fout:
            for flight in self.flights:
                fout.write(repr(flight) + "\n")

    def add_flight(self, id, departure_city, departure_time, arrival_city, arrival_time):

        # validating the new flight
        if id in self.flights:
            raise FlightException("This id already exists!")

        if departure_city not in self.airports:
            self.airports[departure_city] = [departure_time]
        elif departure_time in self.airports[departure_city]:
            raise FlightException(f"{departure_city} cannot handle 2 operations at the same minute!")

        if arrival_city not in self.airports:
            self.airports[arrival_city] = [arrival_time]
        elif arrival_time in self.airports[arrival_city]:
            raise FlightException(f"{arrival_city} cannot handle 2 operations at the same minute!")

        #compute the difference between the arrival and departure time
        difference = arrival_time.hour * 60 + arrival_time.minute - departure_time.hour * 60 - departure_time.minute


        if difference > 90:
            raise FlightException("The flight is too long. It must between 15 and 90 min!")
        if difference < 15:
            raise FlightException("The flight is too short. It must between 15 and 90 min!")

        # adding the flight
        self.flights.append(Flight(id, departure_city, departure_time, arrival_city, arrival_time))

        # saving to the file
        self.save_file()

    def delete_flight(self, id):
        for flight in self.flights:
            if flight.id == id:
                self.flights.remove(flight)
                return
        # if not found
        raise FlightException("The flight does not exist!")

    def list_airports(self):
        result = ""
        # sorting airports
        sorted_airpots = sorted(self.airports, key=lambda x: len(self.airports[x]), reverse=True)
        for airport in sorted_airpots:
            result += airport + ' - ' + str(len(self.airports[airport])) + " operations" + '\n'
        return result

    def determine_max_flights(self):
        result = ""
        count = 0

        sorted_flights = sorted(self.flights, key=lambda x: x.arrival_time)
        last_flight_used = sorted_flights[0]
        for flight in sorted_flights:
            if flight.departure_time > last_flight_used.arrival_time:
                last_flight_used = flight
                result += str(flight) + '\n'
                count += 1
        result += f"The maximum number of flights is {count}"
        return result


if __name__ == "__main__":
    # textRepo = FlightTextRepo()
    # print(textRepo.list_airports())
    arrival_time = datetime.time(15, 20)
    departure_time = datetime.time(17, 25)
    difference = arrival_time - departure_time