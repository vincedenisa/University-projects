from datetime import date

class Reservation:
    def __init__(self, id:str, roomNr:int, name:str, noGuests:int, arrDate:date, depDate:date):
        self.id = id
        self.roomNr = roomNr
        self.name = name
        self.noGuests = noGuests
        self.arrDate = arrDate
        self.depDate = depDate
        