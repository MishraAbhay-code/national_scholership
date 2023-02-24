from odoo import models, fields, api


class NationalScholership(models.Model):
    _name = 'renewable.login'
    nsp_id = fields.Char(string='NSP ID')
    nsp_pasword = fields.Char(string='NSP Password')
    validation_button = fields.Char(string='Done', compute='validation_check')


    def validation_check(self):
        if self.nsp_id:
            val_list = self.nsp_id
            for rec in self.nsp_id:
                if rec == '@' and val_list[len(val_list) - 1] != '@':
                    value = self.nsp_id.split('@')
                    val = ['nsp']
                    if value[1] == val[0]:
                        self.validation_button = "Validated"
                        break
                    else:
                        self.validation_button = "unvalidated"
                else:
                    self.validation_button = "unvalidated"
        else:
            self.validation_button = " "


class NspId(models.Model):
    _inherit = 'sale.order'
    nsp_id_inherit = fields.Char(string='NSP ID',compute='validation_check') #inherit_code_view.xml
