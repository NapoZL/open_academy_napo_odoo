 #-*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
     _name = 'open_academy.course'
     _description = 'Course'
     _responsible_id = 'example'

     name = fields.Char(string='Course')
     title = fields.Char(string='Title')
     description = fields.Text(string='Description')
     responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)