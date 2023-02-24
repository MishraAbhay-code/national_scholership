from datetime import date
from odoo import models, fields,api


class NationalScholership(models.TransientModel):
    _name = 'wizard.nextbutton'
    registration_num = fields.Char(string="Rollnumber Number")
    date_of_birth = fields.Date(string='Date of Birth')

    def action_next(self):
        # self.state = "features"
        pass


class NationalScholershipWizard(models.TransientModel):
    _name = 'wizard.under'
    # registration_num = fields.Char(string="Your Registration Number is",default="***************")
    # date_of_birth = fields.Char(string='Your Date of Birth is',default="**/**/****")
    colege_name = fields.Many2one('nsp.form',string="Your college name is")
    student_roll = fields.Many2one('data.form',string='Roll number is')

    def action_next(self):
        # self.state = "features"
        pass



