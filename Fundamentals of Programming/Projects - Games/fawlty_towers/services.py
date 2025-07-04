import unittest
from datetime import date, datetime, timedelta

from reservation import Reservation
from reservationsRepo import ReservationsRepo
from room import Room


class Services:
    def __init__(self, resFile="reservations.txt", roomsFile="rooms.txt"):
        self.roomsFile = roomsFile
        self.rooms = []
        self.loadRooms()

        resRepo = ReservationsRepo(resFile)
        self.resRepo = resRepo
        self.resFile = resFile
        self.loadReservations()

    def loadReservations(self):
        with open(self.resFile, "r") as fin:
            for line in fin:
                tokens = line.split(",")
                id = tokens[0].strip()
                roomNr = int(tokens[1].strip())
                name = tokens[2].strip()
                nrGuests = int(tokens[3].strip())

                arrivalStr = tokens[4].strip()
                arrivalDate = datetime.strptime(arrivalStr, "%d.%m").date()
                arrivalDate = date(2018, arrivalDate.month, arrivalDate.day)

                departureStr = tokens[5].strip()
                departureDate = datetime.strptime(departureStr, "%d.%m").date()
                departureDate = date(2018, departureDate.month, departureDate.day)
                # making the reservation
                self.resRepo.reservations.append(Reservation(id, roomNr, name, nrGuests, arrivalDate, departureDate))
                self.resRepo.resIDs.append(id)
                # reserving the room
                room = self.roomByID(roomNr)
                room.reserveRoom(arrivalDate, departureDate)

    def loadRooms(self):
        with open(self.roomsFile, "r") as fin:
            for line in fin:
                tokens = line.split(" ")
                id = int(tokens[0].strip())
                type = int(tokens[1].strip())
                newRoom = Room(id, type)
                self.rooms.append(newRoom)

    def createReservation(self, roomNr: int, name: str, nrGuests: int, arrivalDate: date, departureDate: date):
        """
        The function creates a reservation
        :param roomNr: roomNr
        :param name: name
        :param nrGuests: nrGuests
        :param arrivalDate: arrivalDate
        :param departureDate: departureDate
        :return: nothing
        """
        # reserving the room
        room = self.roomByID(roomNr)
        room.reserveRoom(arrivalDate, departureDate)
        # creating the reservation
        self.resRepo.createReservation(roomNr, name, nrGuests, arrivalDate, departureDate)

    def roomByID(self, roomNr):
        """
        Return a room by its id or False if it does not exist
        :param roomNr: roomNr
        :return:a room by its id or False if it does not exist
        """
        for room in self.rooms:
            if room.id == roomNr:
                return room
        return False

    def freeRooms(self, type: int, arrivalDate: date, departureDate: date):
        for room in self.rooms:
            if room.type == type and room.RoomFree(arrivalDate, departureDate):
                return room.id
        return False

    def deleteReservation(self, ID: str):
        """
        Deleting a reservation
        :param ID: The unique id of the reservation
        :return: nothing
        """
        res = self.resRepo.reservationById(ID)
        room = self.roomByID(res.roomNr)
        room.unreserveRoom(res.arrivalDate, res.departureDate)
        self.resRepo.deleteReservation(ID)

    def availableRooms(self, arrivalDate: date, departureDate: date):
        string = "Available Rooms:\n"
        for room in self.rooms:
            if room.RoomFree(arrivalDate, departureDate):
                string += f"{room.id} - {room.type} person(s)\n"

        if string == "Available Rooms:\n":
            return "There are no available rooms in the period of time given."

        return string

    def monthlyReport(self):
        months = [100]
        for i in range(1, 13):
            day = date(2018, i, 1)
            months.append(0)
            last = date(2018 + (i // 12), ((i + 1) % 13 + (i == 12)), 1)
            while day < last:
                available = True
                for room in self.rooms:
                    if day in room.used:
                        available = False
                day = day + timedelta(days=1)
                months[i] += (available == False)

        months2 = ["Monthly report:", "January", "February", "March", "April", "May", "June", "July", "August",
                   "September", "October", "November", "December"]
        for i in range(1, 12):
            for j in range(i + 1, 13):
                if months[i] < months[j]:
                    months2[i], months2[j] = months2[j], months2[i]
                    months[i], months[j] = months[j], months[i]

        string = ""
        for month in months2:
            string += month + "\n"

        return string

    def dayOfWeekReport(self):
        weekdays = [0] * 7
        day = date(2018, 1, 1)
        last = date(2019, 1, 1)
        while day < last:
            available = True
            for room in self.rooms:
                if day in room.used:
                    available = False
            day = day + timedelta(days=1)
            if available == False:
                weekdays[day.weekday()] += 1

        weekdaysStr = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for i in range(0, 6):
            for j in range(i + 1, 7):
                if weekdays[i] < weekdays[j]:
                    weekdaysStr[i], weekdaysStr[j] = weekdaysStr[j], weekdaysStr[i]
                    weekdays[i], weekdays[j] = weekdays[j], weekdays[i]

        string = "Day of week report:\n"
        for i in range(0, 7):
            string += weekdaysStr[i] + "\n"

        return string


if __name__ == "__main__":
    print("??")