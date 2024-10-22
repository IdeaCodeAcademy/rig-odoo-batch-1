from odoo import api, fields, models, _
from odoo.exceptions import UserError


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
    category_ids = fields.Many2many('res.partner.category', copy=False)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company, readonly=True)
    currency_id = fields.Many2one('res.currency', related="company_id.currency_id")
    fees = fields.Monetary()
    lesson_ids = fields.One2many('ica.lesson', 'course_id', domain=[('state', '=', 'published')])
    active = fields.Boolean(default=True)

    def action_draft(self):
        self.state = 'draft'

    def action_published(self):
        if len(self.lesson_ids) <= 0:
            raise UserError(_('You must select at least one lesson'))
        self.state = 'published'

    def action_cancelled(self):
        self.state = 'cancelled'

    # def action_add_lesson(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         "name": "Add Lesson",
    #         "res_model": "ica.lesson",
    #         "view_mode": "form",
    #         "target": "new",
    #         "context":{"default_course_id":self.id}
    #     }
