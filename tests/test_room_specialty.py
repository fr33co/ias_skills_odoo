from odoo.tests.common import TransactionCase


class TestRoomsSpecialty(TransactionCase):

    def test_specialty_creation(self):
        specialty = self.env["rooms.specialty"].create({
            "name": "Test 1"
        })
        self.assertEqual(specialty.name, "Test 1")
