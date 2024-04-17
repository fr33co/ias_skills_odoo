from odoo.tests.common import TransactionCase


class TestRoomsReservation(TransactionCase):

    def test_room_reservation_creation(self):
        doctor = self.env["res.partner"].create({
            "name": "Doctor 1"
        })
        room = self.env["rooms.rooms"].create({
            "name": "Room 1"
        })
        specialty = self.env["rooms.specialty"].create({
            "name": "Test 1"
        })
        reservation = self.env["rooms.reservation"].create({
            "name": "Reservation 1",
            "doctor_id": doctor.id,
            "room_id": room.id,
            "specialty_id": specialty.id,
            "responsible_"
            "price": 200.0,
            "weeksdays": "1",
            "init_hour": 10.0,
            "end_hour": 12.0,
            "state": "draft"
        })
        self.assertEqual(reservation.name, "Reservation 1")
        self.assertEqual(reservation.price, 200.0)
        self.assertEqual(reservation.weeksdays, "1")
        self.assertEqual(reservation.state, "draft")
