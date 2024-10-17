from odoo import api, fields, models

class IcaLesson(models.Model):
    _name = 'ica.lesson'
    _description = 'IcaLesson'
    _inherit = ['mail.thread']

    name = fields.Char(required=True,tracking=True)
    description = fields.Text(tracking=True)
    type = fields.Selection([
        ('photo','Photo'),
        ('video','Video'),
        ('text','Text'),
    ],default='text',tracking=True)
    text = fields.Html()
    video = fields.Binary()
    photo = fields.Image()
    course_id = fields.Many2one('ica.course', string='Course',required=True,tracking=True)
    state = fields.Selection([
        ('draft','Draft'),
        ('published','Published'),
    ],default='draft',tracking=True)