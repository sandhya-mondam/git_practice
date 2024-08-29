from odoo import models, fields, api, tools, _

class Patient(models.Model):
    _name = 'patient.patient'
    _description = 'Patient Information'


    name = fields.Char(string='ID', readonly=True)
    patient_name = fields.Char(string='Patient Name')
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    medical_history = fields.Text(string='Medical History', translate=True)
    reports_ids = fields.Many2many('medical.reports','patient_medical_reports_rel','patient_id','medical_id',string="Medical Tests")
    emergency_contact = fields.Char(string='Emergency Contact')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('my_patient_sequence')
        return super(Patient, self).create(vals)

