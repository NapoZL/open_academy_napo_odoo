 #-*- coding: utf-8 -*-

from odoo import models, fields, api


class Session(models.Model):
     _name = 'open_academy.session'
     _startDate = '22/02/2022'
     _duration = '15 semanas'
     _seats = '30'

     name = fields.Char(string='Session')
     startDate = fields.Date(string='Start Date')
     duration = fields.Char(string='Duración')
     seats = fields.Integer(string='Number of seats')