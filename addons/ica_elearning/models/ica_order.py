from odoo import api, fields, models


class IcaOrder(models.Model):
    _name = 'ica.order'
    _description = 'IcaOrder'
    _rec_name = 'course_id'
    _order = 'id desc'

    partner_id = fields.Many2one('res.partner', string='Partner')
    course_id = fields.Many2one('ica.course', string='Course')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('paid', 'Paid'),
        ('refunded', 'Refunded'),
        ('cancelled', 'Cancelled'),
    ], default='draft')

    def action_paid_order(self):
        self.state = 'paid'


