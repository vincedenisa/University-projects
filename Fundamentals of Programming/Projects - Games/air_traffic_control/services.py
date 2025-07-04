from TextRepo import FlightTextRepo


class FlightsService:
    def __init__(self, repo: FlightTextRepo):
        self._repo = repo

    def add_flight(self, id, departure_city, departure_time, arrival_city, arrival_time):
        self._repo.add_flight(id, departure_city, departure_time, arrival_city, arrival_time)

    def delete_flight(self, id):
        self._repo.delete_flight(id)

    def list_airports(self):
        return self._repo.list_airports()
    def determine_max_flights(self):
        return self._repo.determine_max_flights()