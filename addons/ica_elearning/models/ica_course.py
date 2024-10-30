from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Course(models.Model):
    _name = "ica.course"
    _description = "ICA Course"

    name = fields.Char(required=True,copy=False)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('cancelled', 'Cancelled'),
    ], default='draft')
    partner_id = fields.Many2one('res.partner', required=True,default=lambda self: self.env.user.partner_id)
    category_ids = fields.Many2many('res.partner.category', copy=False)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company, readonly=True)
    currency_id = fields.Many2one('res.currency', related="company_id.currency_id")
    fees = fields.Monetary()
    lesson_ids = fields.One2many('ica.lesson', 'course_id', domain=[('state', '=', 'published')])
    active = fields.Boolean(default=True)
    lesson_count = fields.Integer(compute="_compute_lesson_count")
    reference = fields.Char(default=lambda self:_('New'),readonly=True,copy=False)

    _sql_constraints = [
        ('reference_unique', 'unique(reference)', "Reference must be unique."),
        # ('name_unique', 'unique(1==1)', "Course name must be unique! Please choose another one."),
    ]

    @api.constrains('name')
    def _check_name(self):
        if self.name:
            domain=[('id','not in',self.ids),('name','=',self.name)]
            record_length = self.search_count(domain)
            if record_length > 0:
                raise UserError(_("Name must be unique."))


    @api.model
    def create(self, values):
        if values.get('reference',_('New')) == _('New'):
            values['reference'] = self.env['ir.sequence'].next_by_code('ica.course')
        return super(Course, self).create(values)

    @api.depends('lesson_ids')
    def _compute_lesson_count(self):
        self.lesson_count = len(self.lesson_ids)

    def action_draft(self):
        self.state = 'draft'

    def action_published(self):
        if len(self.lesson_ids) <= 0:
            raise UserError(_('You must select at least one lesson'))
        self.state = 'published'

    def action_cancelled(self):
        self.state = 'cancelled'

    def action_add_lesson(self):
        return {
            'type': 'ir.actions.act_window',
            "name": "Add Lesson",
            "res_model": "ica.lesson",
            "view_mode": "list",
            "target": "current",
            "context":{"default_course_id":self.id}
        }
