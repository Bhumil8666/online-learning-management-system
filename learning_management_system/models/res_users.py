from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    is_student = fields.Boolean(string='Is a Student')
    is_teacher = fields.Boolean(string='Is a Teacher')
    is_admin = fields.Boolean(string='Is an Admin')