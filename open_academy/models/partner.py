# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    inherit = fields.Char(string='Partner')
    instructor = fields.Boolean("Instructor", default=False)
    session_ids = fields.Many2many('open_academy.session',
        string="Attended Sessions", readonly=True)
