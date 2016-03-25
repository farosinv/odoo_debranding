# -*- coding: utf-8 -*-
from openerp import http

# class OdooDebranding(http.Controller):
#     @http.route('/odoo_debranding/odoo_debranding/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_debranding/odoo_debranding/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_debranding.listing', {
#             'root': '/odoo_debranding/odoo_debranding',
#             'objects': http.request.env['odoo_debranding.odoo_debranding'].search([]),
#         })

#     @http.route('/odoo_debranding/odoo_debranding/objects/<model("odoo_debranding.odoo_debranding"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_debranding.object', {
#             'object': obj
#         })