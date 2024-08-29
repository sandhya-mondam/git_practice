from odoo import models, fields, api, _

class Doctor(models.Model):
    _name = 'doctor.doctor'
    _description = 'Doctor Information'

    name = fields.Char(string='ID', readonly=True, index=True)
    doctor_name = fields.Char(string='Doctor Name', required=True)
    image_1920 = fields.Binary(string='     ')
    specialization = fields.Char(string='Specialization',default="Emergency")
    salary = fields.Float(string='Salary')
    phone = fields.Char(string='Phone',help="Enter your mobile number")
    email = fields.Char(string='Email')
    department = fields.Many2one('department.department', string='Department')
    appointment_ids = fields.One2many('appointment.appointment', 'doctor_id', string='Patient Appointment')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('my_doctor_sequence')
        return super(Doctor, self).create(vals)


