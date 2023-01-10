# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RendementSubscription(models.Model):
    _name = 'rendement.subscription'
    _description='Rendement Subscription'

    name = fields.Char('Product Name')
    partner_id = fields.Many2one('res.partner', 'Customer')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    price = fields.Float('Periodic Price')

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100