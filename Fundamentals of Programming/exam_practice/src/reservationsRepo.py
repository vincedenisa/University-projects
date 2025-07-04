from datetime import date, datetime
from random import randint
from reservation import Reservation

class ReservationsRepo:
    def __init__(self, resFile: "reservations.txt"):
        self.resFile = resFile
        self.reservations = []
        self.resIDs = []

    def createReservation(self, roomNr: int, name:str, nrGuests:int, arrDate:date, depDate:date):
        ID = str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
        while ID in self.resIDs:
            ID = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
        self.resIDs.append(ID)
        newReservation = Reservation(ID, name, nrGuests, arrDate, depDate)
        self.reservations.append(newReservation)

    def deleteReservation(self, ID:str):
        for reservation in self.reservations:
            if reservation.ID == ID:
                self.reservations.remove(reservation)
                self.resIDs.remove(ID)
                return
            raise ValueError("Reservation not found")

    def reservationByID(self, ID:str):
        for reservation in self.reservations:
            if reservation.ID == ID:
                return reservation
        return False
        

