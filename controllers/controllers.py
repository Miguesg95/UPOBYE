# -*- coding: utf-8 -*-
# from odoo import http


# class UPOBYE(http.Controller):
#     @http.route('/UPOBYE/despidos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/despidos/despidos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('despidos.listing', {
#             'root': '/UPOBYE/despidos',
#             'objects': http.request.env['UPOBYE.despidos'].search([]),
#         })

#     @http.route('/UPOBYE/despidos/objects/<model("UPOBYEdespidos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('UPOBYE.object', {
#             'object': obj
#         })
