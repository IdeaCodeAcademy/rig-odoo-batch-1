from odoo import api, fields, models


class IcaOrderWizard(models.TransientModel):
    _name = 'ica.order.wizard'
    _description = 'Ica_order_wizard'

    partner_id = fields.Many2one('res.partner', string='Partner')
    course_id = fields.Many2one('ica.course', string='Course')

    def action_paid(self):
        data = {'partner_id': self.partner_id.id, 'course_id': self.course_id.id}
        ica_order_id = self.env['ica.order'].create(data)
        ica_order_id.action_paid_order()