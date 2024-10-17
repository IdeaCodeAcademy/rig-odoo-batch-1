from odoo import api, fields, models


class Course(models.Model):
    _name = "ica.course"
    _description = "ICA Course"

    name = fields.Char(required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('cancelled', 'Cancelled'),
    ], default='draft')
    partner_id = fields.Many2one('res.partner', required=True)
    category_ids = fields.Many2many('res.partner.category')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company, readonly=True)
    currency_id = fields.Many2one('res.currency', related="company_id.currency_id")
    fees = fields.Monetary()
    lesson_ids = fields.One2many('ica.lesson', 'course_id', domain=[('state', '=', 'published')])
