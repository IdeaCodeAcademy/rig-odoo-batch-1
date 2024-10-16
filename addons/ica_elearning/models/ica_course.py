from odoo import api, fields, models

class Course(models.Model):
    _name = "ica.course"
    _description = "ICA Course"

    name = fields.Char(required=True)
    # number = fields.Integer()
    # floating = fields.Float()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('cancelled', 'Cancelled'),
    ],default='draft')
    partner_id = fields.Many2one('res.partner',required=True)
    category_ids = fields.Many2many('res.partner.category')