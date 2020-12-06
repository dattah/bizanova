# -*- coding: utf-8 -*-
# from odoo import http


# class Mytutor(http.Controller):
#     @http.route('/mytutor/mytutor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mytutor/mytutor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mytutor.listing', {
#             'root': '/mytutor/mytutor',
#             'objects': http.request.env['mytutor.mytutor'].search([]),
#         })

#     @http.route('/mytutor/mytutor/objects/<model("mytutor.mytutor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mytutor.object', {
#             'object': obj
#         })
