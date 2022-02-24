 #-*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Course(models.Model):
     _name = 'open_academy.course'
     _description = 'Course'
     _responsible_id = 'example'
     _session_ids = 'exaxmple'

     name = fields.Char(string='Course')
     title = fields.Char(string='Title')
     description = fields.Text(string='Description')
     responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
     session_ids = fields.One2many(
        'open_academy.session', 'course_id', string="Sessions")

def copy(self, default=None):
   default = dict(default or {})

   copied_count = self.search_count(
      [('name', '=like', u"Copy of {}%".format(self.name))])
   if not copied_count:
      new_name = u"Copy of {}".format(self.name)
   else:
      new_name = u"Copy of {} ({})".format(self.name, copied_count)

   default['name'] = new_name
   return super(Course, self).copy(default)