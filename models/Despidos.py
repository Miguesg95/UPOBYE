# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Despidos(models.Model):
     _name = 'upobye.despidos'     #nombremodulo.nombreclase
     _description = 'upobye.despidos'

     name = fields.Integer(string="Finiquito",required=True,help="Indemnización")
     motivo = fields.Text()
     start = fields.Datetime('Starts', required=True, autodate =True)
     end = fields.Datetime('Ends', required=True, autodate =True)
     motivo_despido = fields.Selection([('jubilacion','Jubilación'),
                                    ('fin de contrato','Fin de contrato'),
                                    ('baja indefinida','Baja indefinida')
                                    ],'Motivo del despido')
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

