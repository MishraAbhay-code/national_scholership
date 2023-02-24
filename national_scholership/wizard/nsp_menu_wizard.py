from odoo import models, fields


class NationalScholership(models.TransientModel):
    _name = 'nsp.menu.wizard'

    registration_num = fields.Char(string="Registration Number")
    date_of_birth = fields.Date(string='Date of Birth')
    state = fields.Selection([
        ('next', 'Next'),
        ('confirm', 'Confirm')])

    def action_next(self):
        pass

    def action_confirm(self):
        pass

    def action_menu_wizard(self):
        # self.state = "features"
        pass
