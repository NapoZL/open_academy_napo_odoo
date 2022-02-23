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

     name = fields.Char(string='Session')
     startDate = fields.Date(string='Start Date')
     duration = fields.Char(string='Duración')
     seats = fields.Integer(string='Number of seats')

     instructor_id = fields.Many2one('res.partner', string="Instructor",
        domain=[('instructor', '=', True)])
     course_id = fields.Many2one('open_academy.course',
        ondelete='cascade', string="Course", required=True)
     attendee_ids = fields.Many2many('res.partner', string="Attendees")


