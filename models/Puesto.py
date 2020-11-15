# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Puesto(models.Model):
    _name = 'upobye.Puesto'
    _description = 'Distintos Puestos'
    
    ID = fields.Char(string="Nombre", required=True, help="Nombre")
    required = fields.Boolean("¿Es necesario?")
    qualification = fields.Text()