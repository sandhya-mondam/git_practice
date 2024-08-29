from odoo import models, fields, api, _

class Department(models.Model):
    _name = 'department.department'
    _description = 'Department Information'


    name = fields.Char(string='ID', readonly=True)
    department_name = fields.Char(string='Department Name')
    description = fields.Text(string='Description')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('my_department_sequence')
        return super(Department, self).create(vals)
