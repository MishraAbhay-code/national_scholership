from odoo import models, fields, api


class FeeCalculculation(models.Model):
    _name = 'fee.calculation'
    choice_data = fields.Selection([('add', 'Add'),
                                    ('subtract', 'Subtract'),
                                    ('multiply', 'Multiply'),
                                    ('divide', 'Divide'),
                                    ('percent', 'Percent'),
                                    ('percentprofit', 'Percent With Profit'),
                                    ('percentloss', 'Percent with Loss'),
                                    ('inpercent', 'Profit or loss in percent')], string='Select Choice')
    enter_num_f = fields.Float(string="Enter first number")
    enter_num_s = fields.Float(string="Enter second number", default=1)
    mathematical_cal = fields.One2many('mathmatical.calculation', 'pass_calculator', string='Mathematical Calculator')
    cgpa_cal = fields.One2many('cgpa.calculation', 'pass_cgpa_calculator', string='Mathematical Calculator')
    calculated_output = fields.Float(string="Calculated Output", compute='calculator_compute')

    # def calculate_compute function for addition,multiplication...... logic
    @api.onchange('choice_data', 'enter_num_f', 'enter_num_s')
    def calculator_compute(self):
        # if value is true then enter while loop
        for r in self:
            # r defined as a self (self access all outer parameter of function)
            if r.choice_data:
                while True:
                    choice = r.choice_data
                    # 'choice' is selection type user parameter

                    if choice in ('add', 'subtract', 'multiply', 'divide',
                                  'percent', 'percentprofit', 'percentloss', 'inpercent'):

                        if choice == 'add':
                            r.calculated_output = r.enter_num_f + r.enter_num_s
                            break
                            # if condition true then run only under if condition code and terminate loop after break keyword
                        elif choice == 'subtract':
                            r.calculated_output = r.enter_num_f - r.enter_num_s
                            break

                        elif choice == 'multiply':
                            r.calculated_output = r.enter_num_f * r.enter_num_s
                            break

                        elif choice == 'divide':
                            r.calculated_output = r.enter_num_f / r.enter_num_s
                            break

                        elif choice == 'percent':
                            r.calculated_output = (r.enter_num_s * r.enter_num_f) / 100
                            break

                        elif choice == 'percentprofit':
                            profit_value = (r.enter_num_s * r.enter_num_f) / 100
                            r.calculated_output = r.enter_num_f + profit_value
                            break

                        elif choice == 'percentloss':
                            loss_value = (r.enter_num_s * r.enter_num_f) / 100
                            r.calculated_output = r.enter_num_f - loss_value
                            break

                        elif choice == 'inpercent':
                            if r.enter_num_f > r.enter_num_s:
                                value = (r.enter_num_f * 100) / r.enter_num_s
                                value = value - 100
                                r.calculated_output = -value
                            else:
                                value = (r.enter_num_f * 100) / r.enter_num_s
                                value = 100 - value
                                r.calculated_output = value
                            break
            else:
                r.calculated_output = 0.00


#================= for mathematical calculation  ===========
class MathmaticalCalculation(models.Model):
    _name = 'mathmatical.calculation'
    choice_data = fields.Selection([('simple', 'Simple interest'),
                                    ('compound', 'Compound')
                                    ], string='Select Choice')
    enter_num_f = fields.Float(string="Enter Principal Amount")
    enter_num_s = fields.Float(string="Rate of Interest")
    enter_num_t = fields.Float(string="Time (In year)")
    pass_calculator = fields.Many2one('fee.calculation')
    calculated_output = fields.Float(string="Calculated Output", compute='mathematical_calculation_compute')

    @api.onchange('choice_data', 'enter_num_f', 'enter_num_s', 'enter_num_t')
    def mathematical_calculation_compute(self):
        for r in self:
            if r.choice_data:
                while True:
                    choice = r.choice_data
                    # 'choice' is selection type user parameter

                    if choice in ('simple', 'compound'):

                        if choice == 'simple':
                            simple_interest = (r.enter_num_f * r.enter_num_s * r.enter_num_t) / 100
                            r.calculated_output = r.enter_num_f + simple_interest
                            break
                        elif choice == 'compound':
                            value_a = r.enter_num_f
                            for rec in range(1, int(r.enter_num_t) + 1):
                                simple_interest = (value_a * r.enter_num_s * 1) / 100
                                value_a = value_a + simple_interest
                            r.calculated_output = value_a
                            break
            else:
                r.calculated_output = 0.00


# ==========   for CGPA & Percentage code ===========
class CgpaCalculation(models.Model):
    _name = 'cgpa.calculation'
    choice_data = fields.Selection([('cgpa', 'Percentage into CGPA'),
                                    ('percentage', 'CGPA into Percentage')
                                    ], string='Select Choice')
    enter_data = fields.Float(string="Enter Data")
    pass_cgpa_calculator = fields.Many2one('fee.calculation')
    calculated_output = fields.Char(string="Calculated Output", compute='cgpa_calculation_compute')

    @api.onchange('choice_data')
    def cgpa_calculation_compute(self):
        for rec in self:
            if rec.enter_data:
                choice = rec.choice_data
                if choice in ('cgpa', 'percentage'):
                    if choice == 'cgpa':
                        # percentage into cgpa formula =  percentage / 9.5
                        cgpa_value = rec.enter_data / 9.5
                        # "{:.2f}".formate(cgpa_value)  gives .23(point two digit float value) two digit float value
                        rec.calculated_output = "{:.2f}".format(cgpa_value) + " CGPA"
                    elif choice == 'percentage':
                        #  cgpa into percentage formula = cgpa * 10
                        percentage_value = rec.enter_data * 10
                        rec.calculated_output = str(percentage_value) + "%"
            else:
                rec.calculated_output = " "
