# -*- coding: utf-8 -*-

from odoo import models, fields, api



class TipoDespido(models.Model):
     _name = 'despidos.TipoDespido'
    _description = 'despidos.TipoDespido'

     name = fields.String(string="forma",required=True,help="Tipo de despido")
    descripcion = fields.Text()
    start = fields.Datetime('Starts', required=True, autodate =True)
    end = fields.Datetime('Ends', required=True, autodate =True)
    forma = fields.Selection([('disciplinario','Disciplinario'),
                                    ('objetivo','Objetivo'),
                                    ('colectivo','Colectivo')
                                    ],'Forma o tipo de despido')
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100