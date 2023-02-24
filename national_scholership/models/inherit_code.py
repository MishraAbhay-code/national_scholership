from odoo import fields, models


class Taxes(models.Model):
    _inherit = 'sale.order'

    customer_data = fields.Char(string='Customer Data(from NSP)', compute="compute_customer_num")

    def compute_customer_num(self):
        if self.partner_id:
            for rec in self.partner_id:
                # rec access one by one customer name
                if rec.phone:
                    # rec.phone access phone number field from customer
                    # 'phone' is a field name from 'sales' module
                    self.customer_data = "91"+str(rec.phone[3:])
                else:
                    self.customer_data = "Null object"
