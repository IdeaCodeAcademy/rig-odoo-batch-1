from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    ica_order_ids = fields.One2many('ica.order','partner_id')
