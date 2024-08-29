from odoo import models, fields, api, _

class MedicalReports(models.Model):
    _name = 'medical.reports'
    _description = 'Medical Reports Information'


    name = fields.Char(string='Medical Report Name', required=True)
    description = fields.Text(string='Description')
    color_tags = fields.Integer(string='Colour')