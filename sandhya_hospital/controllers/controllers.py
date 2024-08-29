# -*- coding: utf-8 -*-
# from odoo import http


# class LmsHospital(http.Controller):
#     @http.route('/lms_hospital/lms_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lms_hospital/lms_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lms_hospital.listing', {
#             'root': '/lms_hospital/lms_hospital',
#             'objects': http.request.env['lms_hospital.lms_hospital'].search([]),
#         })

#     @http.route('/lms_hospital/lms_hospital/objects/<model("lms_hospital.lms_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lms_hospital.object', {
#             'object': obj
#         })
