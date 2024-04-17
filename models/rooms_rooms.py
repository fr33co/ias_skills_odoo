from odoo import models, fields


class RoomsSpecialty(models.Model):
    _name = "rooms.specialty"
    _rec_name = "name"
    _order = "id, name"

    name = fields.Char(string="Name", required=True)


class RoomsRooms(models.Model):
    _name = "rooms.rooms"
    _rec_name = "name"
    _order = "id, name"

    name = fields.Char(string="Name", required=True)
    price = fields.Float(string="Price", required=True)
    responsible_id = fields.Many2one(
        "res.users",
        string="Responsible",
        required=True
    )
    availability_ids = fields.One2many(
        "rooms.availability",
        "room_id",
        string="Availabilty"
    )


class RoomsAvailability(models.Model):
    _name = "rooms.availability"
    _rec_name = "weeksdays"
    _order = "id, weeksdays"

    room_id = fields.Many2one(
        "rooms.rooms",
        string="Room"
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
