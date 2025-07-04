from datetime import date


class Reservation:
    def __init__(self, id: str, roomNr: int, name: str, nrGuests: int, arrivalDate: date, departureDate: date):
        self.id = id
        self.roomNr = roomNr
        self.name = name
        self.nrGuests = nrGuests
        self.arrivalDate = arrivalDate
        self.departureDate = departureDate
