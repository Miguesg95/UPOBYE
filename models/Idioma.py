# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Idioma(models.Model):
     _name = 'upobye.idioma'
     _description = 'Titulacion en idioma del empleado'

     name = fields.Char(string="Nombre", required=True, help="Nombre")
     certificacion = fields.Char(string="Certificado por",required=True,help="Nombre de la identidad que certifica el idioma")

