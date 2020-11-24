# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Puesto(models.Model):
    _name = 'upobye.puesto'
    _description = 'Distintos Puestos'
    
    name = fields.Char(string="Nombre", size=60, help="Nombre puesto")
    ID = fields.Char(string="ID", required=True, help="ID")
    required = fields.Boolean("¿Es necesario?")
    qualification = fields.Text()