# -*- coding: utf-8 -*-
# from odoo import http


# class Participantes(http.Controller):
#     @http.route('/participantes/participantes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/participantes/participantes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('participantes.listing', {
#             'root': '/participantes/participantes',
#             'objects': http.request.env['participantes.participantes'].search([]),
#         })

#     @http.route('/participantes/participantes/objects/<model("participantes.participantes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('participantes.object', {
#             'object': obj
#         })

