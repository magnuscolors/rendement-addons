# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    rendement_subscription_count = fields.Integer(compute='_compute_rendement_subscription_count', string='Sale Order Count')
    rendement_subscription = fields.One2many('rendement.subscription','partner_id', string="Rendement Subscription")
    mailings = fields.Text('Mailings')
    newsletters = fields.Text('Newsletters')
    consent = fields.Text('Consent')


    def _compute_rendement_subscription_count(self):
        # retrieve all children partners and prefetch 'parent_id' on them
        all_partners = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
        all_partners.read(['parent_id'])

        rem_groups = self.env['rendement.subscription'].read_group(
            domain=[('partner_id', 'in', all_partners.ids)],
            fields=['partner_id'], groupby=['partner_id']
        )
        partners = self.browse()
        for group in rem_groups:
            partner = self.browse(group['partner_id'][0])
            while partner:
                if partner in self:
                    partner.rendement_subscription_count += group['partner_id_count']
                    partners |= partner
                partner = partner.parent_id
        (self - partners).rendement_subscription_count = 0

    def action_view_rendement_subscription(self):
        action = self.env['ir.actions.act_window']._for_xml_id('rendement_demo.action_window')
        all_child = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
        action["domain"] = [("partner_id", "in", all_child.ids)]
        return action