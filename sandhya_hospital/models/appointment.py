from odoo import models, fields, api, _
from datetime import datetime

class Appointment(models.Model):
    _name = 'appointment.appointment'
    _description = 'Appointment'


    name = fields.Char(string='ID', readonly=True)
    appointment_name = fields.Char(string='Appointment Name')
    patient_id = fields.Many2one('patient.patient', string='Patient')
    doctor_id = fields.Many2one('doctor.doctor', string='Doctor')
    currency_id = fields.Many2one('res.currency', string='Currency')
    appointment_fee = fields.Monetary(string='Appointment Fee',currency_field='currency_id')
    appointment_date = fields.Date(string='Appointment Date', default=datetime.today())
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    status = fields.Selection([('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], string='Status')
    reason = fields.Text(string='Reason')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('my_appointment_sequence')
        return super(Appointment, self).create(vals)
