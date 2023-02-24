from odoo import models, fields


class NationalScholership(models.Model):
    _name = 'registered.student'
    #many2many field from nsp_form.py==== must defind in xml file
    student_name = fields.Many2many('scholership.main',string='Name (Many2many)',domain = [('qualification','!=',False)])
    college_name = fields.Many2one('nsp.form',string='Collage (Many2one)')
    roll_number = fields.One2many('nsp.form','student_roll',string='Roll Number')
    #and then mention field in notebook tag in xml file
    year_of_passing = fields.Date(string='Year of Passing')
    e_mail = fields.Char(string='Email ID',default="@gmail.com")