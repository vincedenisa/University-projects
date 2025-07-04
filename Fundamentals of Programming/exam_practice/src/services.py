import unittest
from datetime import date, timedelta, datetime
from reservation import Reservation
from reservationsRepo import ReservationsRepo
from room import Room

class Services:
    def __init__(self, resFile:"reservations.txt", roomsFile:"rooms.txt"):
        self.roomsFile = roomsFile
        self.rooms = []
        self.loadRooms()

        resRepo = ReservationsRepo(resFile)
        self.resFile= resFile
        self.resRepo = resRepo
        self.loadReservations()

    def loadReservations(self):
        with open(self.roomsFile, "r") as fin:
            for line in fin:
                tokens = line.split(",")
                id = tokens[0].strip()
                roomNr = int(tokens[1].strip())
                name = tokens[2].strip()
                nrGuests = int(tokens[3].strip())

                arrStr = tokens[4].strip()
                arrDate = datetime.strptime(arrStr, "%Y-%m-%d").date()
                arrDate = date(arrDate.year, arrDate.month, arrDate.day)

                depStr = tokens[5].strip()
                depDate = datetime.strptime(depStr, "%Y-%m-%d").date()
                depDate = date(depDate.year, depDate.month, depDate.day)

                self.resRepo.reservations.append(Reservation(id, name, nrGuests, arrDate, depDate))
                self.resRepo.resIDs.append(id)
                room = self.roomByID(roomNr)
                room.reserveRoom(arrDate, depDate)

    def loadRooms(self):
        with open(self.roomsFile, "r") as fin:
            for line in fin:
                tokens = line.split(" ")
                id = tokens[0].strip()
                type = int(tokens[1].strip())
                newRoom = Room(id, type)
                self.rooms.append(newRoom)

    def createReservation(self, roomNr:int, name:str, nrGuests:int, arrDate:date, depDate:date):
        room = self.roomByID(roomNr)
        room.reserveRoom(arrDate, depDate)
        self.resRepo.createReservation(roomNr, name, nrGuests, arrDate, depDate)

    def roomByID(self, roomNr:int):
        for room in self.rooms:
            if room.id == roomNr:
                return room
        return False

    def freeRooms(self, type:int, arrDate:date, depDate:date):
        for room in self.rooms:
            if room.type == type and room.roomFree(arrDate, depDate):
                return room.id
        return False

    def deleteReservation(self, ID:str):
        res = self.resRepo.reservationByID(ID)
        room = self.roomByID(res.roomNr)
        room.unreserveRoom(res.arrDate, res.depDate)
        self.resRepo.deleteReservation(ID)

    def availableRooms(self, arrDate:date, depDate:date):
        string = "Available Rooms: \n"
        for room in self.rooms:
            if room.roomFree(arrDate, depDate):
                string += f"{room.id} - {room.type} person(s)\n"
            if string == "Available Rooms: \n":
                return ("There are no available rooms")
        return string



if __name__ == "__main__":
    print("??")



