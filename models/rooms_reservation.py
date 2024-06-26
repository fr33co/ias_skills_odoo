from odoo import models, fields


class RoomsReservation(models.Model):
    _name = "rooms.reservation"
    _rec_name = "name"
    _order = "id, name"

    name = fields.Char(string="name")
    doctor_id = fields.Many2one(
        "res.partner", string="Doctor")
    room_id = fields.Many2one(
        "rooms.rooms",
        string="Room"
    )
    specialty_id = fields.Many2one(
        "rooms.specialty",
        string="Specialty"
    )
    price = fields.Float(
        related="room_id.price",
    )
    weeksdays = fields.Selection([
        ("0", "Monday"),
        ("1", "Tuesday"),
        ("2", "Wednesday"),
        ("3", "Thursday"),
        ("4", "Friday"),
        ("5", "Saturday"),
        ("6", "Sunday"),
    ], string="Weekday")
    init_hour = fields.Float(
        string="Init hour"
    )
    end_hour = fields.Float(
        string="End hour"
    )
    state = fields.Selection([
        ("draft", "draft"),
        ("confirmed", "Confirmed"),
        ("reserved", "Reserved"),
    ], string="State")

    def move_draft(self):
        self.write(
            {"state": "draft"}
        )

    def move_confirmed(self):
        self.write(
            {"state": "confirmed"}
        )

    def move_reserved(self):
        self.write(
            {"state": "reserved"}
        )
