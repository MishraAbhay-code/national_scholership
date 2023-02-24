from odoo import models, fields, api
import random
import string
from datetime import date  # for month
import pandas as pd  # for year
from dateutil.relativedelta import relativedelta  # for month


class NationalScholership(models.Model):
    _name = 'scholership.main'
    _rec_name = 'student_name_m'

    student_name_m = fields.Char(string='Name(Required)', required="True")
    student_gendar = fields.Selection([('male', 'Male'),
                                       ('femail', 'Female')], string='Gender')
    student_dob = fields.Date(string='Date of Birth')
    father_name = fields.Char(string="Father's name")
    contact_num = fields.Char(string='Contact Number')
    e_mail = fields.Char(string='Email ID')
    edu_ad = fields.Date(string='Educational Admission Date')
    status = fields.Char(string='Status', compute='education_end_date_compute')
    edu_comp = fields.Date(string='Education Completion Date', compute='education_end_date_compute')
    registration_num = fields.Char(string='Registration Number', compute='education_end_date_compute')
    password = fields.Char(string='Generated Password', compute='password_generation_compute')
    qualification = fields.Selection([('intermediat', 'Intermediat'),
                                      ('diploma', 'Diploma'),
                                      ('ugraduationthree', 'UG (Bsc,BCA,B.com,BA,BBA)'),
                                      ('ugraduationfour', 'UG (B.Tech,BioTech)'),
                                      ('pgraduation', 'PG (M.tech,Msc,MBA,MCA,M.com,MA)')
                                      ],
                                     string='Select Your Education')
    student_image = fields.Image(store="True")
    state_button = fields.Selection([
        ('next', 'Next'),
        ('confirm', 'Confirm'),
        ('done', 'Done')])

    # def action_next(self):
    #     # self.state_button = "next"
    #     pass

    def action_confirm(self):
        self.state_button = "confirm"

    def action_done(self):
        self.state_button = "done"

    @api.onchange('edu_ad', 'qualification')
    def education_end_date_compute(self):
        for outer_value in self:
            if outer_value.qualification:
                while True:
                    choice = outer_value.qualification
                    # 'choice' is selection type user parameter
                    if choice in ('intermediat', 'diploma', 'ugraduationthree', 'ugraduationfour', 'pgraduation'):

                        if choice == 'intermediat':
                            #outer_value.edu_comp = outer_value.edu_ad + relativedelta(month=+12)
                            outer_value.edu_comp = pd.to_datetime(outer_value.edu_ad) + pd.DateOffset(years=1)
                            break

                        elif choice == 'diploma':
                            # self.edu_comp = self.edu_ad + relativedelta(days=+1095)
                            outer_value.edu_comp = pd.to_datetime(outer_value.edu_ad) + pd.DateOffset(years=3)
                            # self.edu_comp = date(self.edu_ad) + relativedelta(years=3)
                            break

                        elif choice == 'ugraduationthree':
                            outer_value.edu_comp = pd.to_datetime(outer_value.edu_ad) + pd.DateOffset(years=3)
                            break

                        elif choice == 'ugraduationfour':
                            outer_value.edu_comp = pd.to_datetime(outer_value.edu_ad) + pd.DateOffset(years=4)
                            break

                        elif choice == 'pgraduation':
                            outer_value.edu_comp = pd.to_datetime(outer_value.edu_ad) + pd.DateOffset(years=2)
                            break
            else:
                outer_value.edu_comp = '2019-01-01'

        for value in self:
            if value.edu_comp:
                today = date.today()
                if value.edu_comp > today:
                    value.registration_num = random.randint(0, 100000000)
                    value.status = "eligible"
                elif str(value.edu_comp) == '2019-01-01':
                    value.registration_num = "complete required field"
                    value.password = "complete required field"
                else:
                    value.registration_num = "Null"
                    value.status = "Not eligible"

    @api.onchange('edu_comp')
    def password_generation_compute(self):
        for outer in self:
            today = date.today()
            if outer.edu_comp > today:
                pass_value = ""
                randum_value = random.randint(0, 100000000)
                randum_value = str(randum_value)
                for i in range(3):
                    ran_pass = random.choice(string.ascii_letters)
                    pass_value += ran_pass
                outer.password = randum_value[0:3] + pass_value + randum_value[5:]
            else:
                outer.password = "Null"

