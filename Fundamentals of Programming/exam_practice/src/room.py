from datetime import date, timedelta

class Room:
    def __init__(self, id:int, type:int):
        self.id = id
        self.type = type
        self.used=[]

    def reserveRoom(self, arrDate:date, depDate:date):
        Day = arrDate
        while Day<depDate:
            self.used.append(Day)
            Day = Day + timedelta(days=1)

    def unreserveRoom(self, arrDate:date, depDate:date):
        Day = arrDate
        while Day<depDate:
            if Day in self.used:
                self.used.remove(Day)
            Day = Day + timedelta(days=1)

    def roomFree(self, arrDate:date, depDate:date):
        Day = arrDate
        while Day<depDate:
            if Day in self.used:
                return False
            Day = Day + timedelta(days=1)
        return True