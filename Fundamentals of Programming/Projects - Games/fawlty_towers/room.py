from datetime import date, timedelta


class Room:
    def __init__(self, id: int, type: int):
        self.id = id
        self.type = type
        self.used = []

    def reserveRoom(self, arrivalDate: date, departureDate: date):
        """
        The function reserves a room
        :param arrivalDate: arrivalDate
        :param departureDate: departureDate
        :return: nothing
        """
        Day = arrivalDate
        while Day < departureDate:
            self.used.append(Day)
            Day = Day + timedelta(days= 1)

    def unreserveRoom(self, arrivalDate: date, departureDate: date):
        """
        The function unreserves a room
        :param arrivalDate: arrivalDate
        :param departureDate: departureDate
        :return: nothing
        """
        Day = arrivalDate
        while Day < departureDate:
            if Day in self.used:
                self.used.remove(Day)
            Day = Day + timedelta(days=1)

    def RoomFree(self, arrivalDate: date, departureDate: date):
        Day = arrivalDate
        while Day < departureDate:
            if Day in self.used:
                return False
            Day = Day + timedelta(days=1)

        return True