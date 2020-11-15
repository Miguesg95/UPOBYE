# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Titulacion(models.Model):
     _name = 'upobye.Titulacion'
     _description = 'upobye Titulacion'
     name = fields.Char(string="Nombre", required=True, help="Nombre")
     certificacion = fields.Char(string="certificacion", required=True, help="Certificacion")
