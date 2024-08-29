{
    'name': 'LMS Hospital',
    'icon': '/lms_hospital/static/description/icon.png',
    'version': '1.0',
    'summary': 'Module to manage hospital operations',
    'sequence': -100,
    'category': 'Healthcare',
    'author': 'FlowEazy',
    'website': 'http://www.odoo.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/appointment_views.xml',
        'views/doctor_views.xml',
        'views/department_views.xml',
        'views/medical_reports.xml',
        'data/my_patient_sequence.xml',
        'data/my_appointment_sequence.xml',
        'data/my_doctor_sequence.xml',
        'data/my_department_sequence.xml',
        

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
