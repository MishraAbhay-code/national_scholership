from datetime import date
from odoo import models, fields, api


class NationalScholership(models.Model):
    _name = 'nsp.form'
    _rec_name = "college_name"
    student_name = fields.Char(string='Name')
    student_roll = fields.Many2one('registered.student')  # for One2many field
    student_gendar = fields.Selection([('male', 'Male'),
                                       ('femail', 'Female')], string='Gender')
    student_dob = fields.Date(string='Date of Birth')
    # age_calculation = fields.Char(string='Age(compute)',compute='age_compute')
    age_calculation = fields.Char(string='Age(onchange)', compute='age_onchange')  # onchange
    college_name = fields.Char(string='Collage Name')
    roll_number = fields.Char(string='Roll Number')
    year_of_passing = fields.Date(string='Year of Passing')
    father_name = fields.Char(string="Father's name")
    contact_num = fields.Char(string='Contact Number(attrs)', default=" 'email id' required then option will be open")
    e_mail = fields.Char(string='Email ID')
    adhar_num = fields.Char(string='Adhar Numbar(atrrs)',
                            default="'name','DOB','father's name' are required then option will be open")
    qualification = fields.Selection([('intermediat', 'Intermediat'),
                                      ('diploma', 'Diploma'),
                                      ('under graduation', 'Under Graduation'),
                                      ('post graduation', 'Post Graduation')],
                                     string='Select Your Qualification')
    student_image = fields.Image(store="True")
    state_button = fields.Selection([
        ('next', 'Next'),
        ('confirm', 'Confirm'),
        ('done', 'Done')])

    def action_next(self):
        self.state_button = "next"

    def action_confirm(self):
        self.state_button = "confirm"

    def action_done(self):
        self.state_button = "done"

    # --------------------------------------------------------------------------
    # def age_compute(self):
    #     age = self.student_dob
    #     today = date.today()
    #     self.age_calculation = today.year - age.year - ((today.month,today.day) < (age.month,age.day))

    @api.onchange('student_dob')
    def age_onchange(self):
        age = self.student_dob
        if age:
            today = date.today()
            self.age_calculation = today.year - age.year - ((today.month, today.day) < (age.month, age.day))
        else:
            self.age_calculation = 'select date of birth'
    # ================================= other class =================================


class NationalScholership(models.Model):
    _name = 'data.form'
    _rec_name = 'student_roll'
    student_name = fields.Char(string='Name')
    student_roll = fields.Char(string='Roll Number',required="True")
