# -*- coding: utf-8 -*-
from odoo import http

# class RendementDemo(http.Controller):
#     @http.route('/rendement_demo/rendement_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rendement_demo/rendement_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rendement_demo.listing', {
#             'root': '/rendement_demo/rendement_demo',
#             'objects': http.request.env['rendement_demo.rendement_demo'].search([]),
#         })

#     @http.route('/rendement_demo/rendement_demo/objects/<model("rendement_demo.rendement_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rendement_demo.object', {
#             'object': obj
#         })