from datetime import time


class Flight:
    def __init__(self, id: str, departure_city: str, departure_time: time, arrival_city: str, arrival_time: time):
        self.__id = id
        self.departure_city = departure_city
        self.departure_time = departure_time
        self.arrival_city = arrival_city
        self.arrival_time = arrival_time

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f"{self.departure_time} | {self.arrival_time} | {self.id} | {self.departure_city} - {self.arrival_city}"

    def __repr__(self):
        return f"{self.id}, {self.departure_city}, {self.departure_time.hour}:{self.departure_time.min}, {self.arrival_city}, {self.arrival_time.hour}:{self.arrival_time.min}"