# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


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

     contrato_id = fields.One2many('upobye.contrato', 'despido_id', 'Contrato')

     @api.constrains('start','end')
     def _fecha_despidos(self):
          t1 = datetime.datetime.strptime(self.start, '%Y-%m-%d %H:%M:%S')
          t2 = datetime.datetime.strptime(self.end, '%Y-%m-%d %H:%M:%S')
          if t2<t1:
               raise models.ValidationError('La fecha fin debe ser posterior a la fecha inicio')