# -*- coding: utf-8 -*-
# from odoo import http


# class Military-module(http.Controller):
#     @http.route('/military-module/military-module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/military-module/military-module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('military-module.listing', {
#             'root': '/military-module/military-module',
#             'objects': http.request.env['military-module.military-module'].search([]),
#         })

#     @http.route('/military-module/military-module/objects/<model("military-module.military-module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('military-module.object', {
#             'object': obj
#         })
