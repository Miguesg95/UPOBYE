# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Idioma(models.Model):
     _name = 'upobye.Idioma'
     _description = 'upobye Idioma'
     name = fields.Char(string="Nombre", required=True, help="Nombre")
     certificacion = fields.Char(string="certificacion", required=True, help="Certificacion")

