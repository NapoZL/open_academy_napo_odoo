 #-*- coding: utf-8 -*-

from odoo import models, fields, api

class Session(models.Model):
     _name = 'open_academy.session'
     _startDate = '22/02/2022'
     _duration = '15 semanas'
     _seats = '30'
     _instructor_id = "expample inst"
     _course_id = "course 1"
     _atttende_ids = "a"
     _taken_seats = ""

     name = fields.Char(string='Session')
     startDate = fields.Date(default=fields.Date.today)
     duration = fields.Char(string='Duración')
     seats = fields.Integer(string='Number of seats')
     active = fields.Boolean(default=True)


     instructor_id = fields.Many2one('res.partner', string="Instructor",
         domain=['|', ('instructor', '=', True), ('category_id.name', 'ilike', "Teacher")])
     course_id = fields.Many2one('open_academy.course',
        ondelete='cascade', string="Course", required=True)
     attendee_ids = fields.Many2many('res.partner', string="Attendees")

     taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')

@api.depends('seats', 'attendee_ids')
def _taken_seats(self):
            for r in self:
               if not r.seats:
                  r.taken_seats = 0.0
               else:
                  r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

@api.onchange('seats', 'attendee_ids')
def _verify_valid_seats(self):
   if self.seats < 0:
      return {
         'warning': {
               'title': "Incorrect 'seats' value",
               'message': "The number of available seats may not be negative",
                },
            }
   if self.seats < len(self.attendee_ids):
      return {
            'warning': {
               'title': "Too many attendees",
               'message': "Increase seats or remove excess attendees",
                },
            }
