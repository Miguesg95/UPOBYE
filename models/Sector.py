
from odoo import models, fields, api

class Sector(models.Model):
    _name = 'upobye.sector'
    _description = 'Sectores de UPOBYE'

    name = fields.Char(string="nombre_sector", size=60, help="Nombre del sector")
    description = fields.Text(string="descripcion_sector", size=200, help="Descripción del sector")
    #sectores_proyecto = fields.many2many("upobye.Sector","Sector")
    