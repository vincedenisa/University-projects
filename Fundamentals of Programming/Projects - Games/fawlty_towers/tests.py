import unittest
from datetime import date

from reservationsRepo import ReservationsRepo
from services import Services


class ServicesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.services = Services("reservationsTests.txt", "roomsTests.txt")

    # tests for functionality 2
    def testCreateReservation(self):
        self.services.createReservation(9, "George", 1, date(2018, 11, 3), date(2018, 11, 5))
        self.assertEqual(self.services.resRepo.reservations[10].roomNr, 9)
        self.assertEqual(self.services.resRepo.reservations[10].name, "George")
        self.assertEqual(self.services.resRepo.reservations[10].nrGuests, 1)
        self.assertEqual(self.services.resRepo.reservations[10].arrivalDate, date(2018, 11, 3))
        self.assertEqual(self.services.resRepo.reservations[10].departureDate, date(2018, 11, 5))
        # test reserve room
        room = self.services.roomByID(9)
        self.assertEqual(room.used, [date(2018, 11, 3), date(2018, 11, 4)])

    def testRoomByID(self):
        room = self.services.roomByID(1)
        self.assertEqual(room.id, 1)
        self.assertEqual(room.type, 2)

    # tests for functionlity 3
    def testDeleteReservation(self):
        self.services.deleteReservation("1223")
        try:
            self.services.deleteReservation("1223")
            assert False
        except:
            assert True


class ReservationRepoTests(unittest.TestCase):
    def setUp(self) -> None:
        self.resRepo = ReservationsRepo("reservationsTests.txt")

    def testCreateReservation(self):
        self.resRepo.createReservation(9, "George", 1, date(2018, 11, 3), date(2018, 11, 5))
        self.assertEqual(self.resRepo.reservations[0].roomNr, 9)
        self.assertEqual(self.resRepo.reservations[0].name, "George")
        self.assertEqual(self.resRepo.reservations[0].nrGuests, 1)
        self.assertEqual(self.resRepo.reservations[0].arrivalDate, date(2018, 11, 3))
        self.assertEqual(self.resRepo.reservations[0].departureDate, date(2018, 11, 5))

if __name__ == '__main__':
    unittest.main()

