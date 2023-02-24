from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # def action_tests(self):
    #     action = self.env["ir.actions.act_window"]._for_xml_id("national_scholership.nsp_menu_wizard_action_window")
    #     # action['context'] = {'active_id': self.env.context['active_id'],
    #     #                      'active_model': self.env.context['active_model']}
    #     return action
    #     print("test++++++++++++++++++++++")
    def action_tests(self):
        action = self.env["ir.actions.act_window"]._for_xml_id("national_scholership.wizard_under_action_window")
        # action['context'] = {'active_id': self.env.context['active_id'],
        #                      'active_model': self.env.context['active_model']}
        return action
        print("test++++++++++++++++++++++")


