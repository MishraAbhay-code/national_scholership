from odoo import models, fields, api
from datetime import date
import random
import pandas as pd


class FeeCalculculation(models.Model):
    _name = 'final.form'
    first_name = fields.Char(string="Enter first Name")
    last_name = fields.Char(string="Enter last Name")
    full_name = fields.Char(string="Full Name", compute="full_name_compute")
    gender = fields.Selection([('male', 'Male'),
                               ('femail', 'Femail')], string='Gender')
    date_of_birth = fields.Date(string="Date of Birth")
    father_name = fields.Char(string="Father's Name")
    college_name = fields.Char(string="College Name")
    education = fields.Selection([('btech', 'B.tech'),
                                  ('diploma', 'Diploma'),
                                  ('bsc', 'Bsc'), ('msc', 'Msc')], string='Education')
    education_year = fields.Selection([('firstyear', '1st Year'),
                                       ('secoundyear', '2nd Year'),
                                       ('thierdyear', '3rd Year'),
                                       ('forthyear', '4rth Year')], string="Education Year")
    semester_starting = fields.Date(string="Semester Starting Year")
    roll_number = fields.Char(string="Roll Number")
    email_id = fields.Char(string="NSP ID",compute="full_name_compute")
    adhar_num = fields.Char(string="Adhar Number")
    scholarship_validity = fields.Date(string='Scholarship Validity', compute='full_name_compute')

    def full_name_compute(self):
        for rec in self:
            if rec.first_name:
                name = rec.father_name.split(" ")
                # print student first name + father first name + student last name
                rec.full_name = str(rec.first_name) + " " + str(name[0]) + " " + (rec.last_name)
                # NSP id generation code
                #split_value = rec.full_name.casefold()
                random_value = random.randint(0, 100) # for random number generation
                split_value = rec.full_name.lower()
                split_val = split_value.split(" ")
                rec.email_id = split_val[2]+split_val[0]+str(random_value)+"@nsp"
            else:
                rec.full_name = " "
            choice = rec.education
            evalue = rec.education_year
            if choice in ('btech', 'diploma', 'bsc', 'msc'):
                if choice == 'btech':
                    if evalue in ('firstyear', 'secoundyear', 'thierdyear', 'forthyear'):
                        if evalue == 'firstyear':
                            rec.scholarship_validity = pd.to_datetime(rec.semester_starting) + pd.DateOffset(years=4)
                        if evalue == 'secoundyear':
                            rec.scholarship_validity = pd.to_datetime(rec.semester_starting) + pd.DateOffset(years=3)
                        if evalue == 'thierdyear':
                            rec.scholarship_validity = pd.to_datetime(rec.semester_starting) + pd.DateOffset(years=2)
                        if evalue == 'forthyear':
                            rec.scholarship_validity = pd.to_datetime(rec.semester_starting) + pd.DateOffset(years=1)
                if choice == 'diploma' or 'bsc':
                    if evalue in ('firstyear', 'secoundyear', 'thierdyear'):
                        if evalue == 'firstyear':
                            rec.scholarship_validity = pd.to_datetime(rec.semester_starting) + pd.DateOffset(years=3)
                        if evalue == 'secoundyear':
                            rec.scholarship_validity = pd.to_datetime(rec.semester_starting) + pd.DateOffset(years=2)
                        if evalue == 'thierdyear':
                            rec.scholarship_validity = pd.to_datetime(rec.semester_starting) + pd.DateOffset(years=1)
                if choice == 'msc':
                    if evalue in ('firstyear', 'secoundyear'):
                        if evalue == 'firstyear':
                            rec.scholarship_validity = pd.to_datetime(rec.semester_starting) + pd.DateOffset(years=2)
                        if evalue == 'secoundyear':
                            rec.scholarship_validity = pd.to_datetime(rec.semester_starting) + pd.DateOffset(years=1)
            else:
                rec.scholarship_validity = ""
