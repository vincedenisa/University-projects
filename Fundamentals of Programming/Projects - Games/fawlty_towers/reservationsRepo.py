from datetime import date, datetime
from random import randint

from reservation import Reservation


class ReservationsRepo:
    def __init__(self, resFile = "reservations.txt"):
        self.reservations = []
        self.resIDs = []
        self.resFile = resFile

    def createReservation(self, roomNr: int, name: str, nrGuests: int, arrivalDate: date, departureDate: date):

        ID = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
        while ID in self.resIDs:
            ID = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))

        self.resIDs.append(ID)
        newRes = Reservation(ID, roomNr, name, nrGuests, arrivalDate, departureDate)
        self.reservations.append(newRes)

    def deleteReservation(self, ID: str):
        """
        Deletes a reservation by its ID
        :param ID: ID
        :return: nothing
        """
        for res in self.reservations:
            if res.id == ID:
                self.reservations.remove(res)
                self.resIDs.remove(ID)
                return
        raise ValueError("Reservation not found")

    def reservationById(self, ID):
        for res in self.reservations:
            if res.id == ID:
                return res
        return False
