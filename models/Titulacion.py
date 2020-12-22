# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Titulacion(models.Model):
     _name = 'upobye.titulacion'
     _description = 'Titulacion del empleado'
     
     name = fields.Char(string="Nombre", required=True, help="Nombre")
     certificacion = fields.Char(string="Certificado por",required=True,help="Nombre de la identidad que certifica la titulacion")

     empleado_id = fields.Many2one('upobye.empleado', string='Empleado')
