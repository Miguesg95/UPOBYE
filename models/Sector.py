
from odoo import models, fields, api

class sector(models.Model):
    _nombre = 'upobye.sector'
    _descripcion = 'Sectores de UPOBYE'

    nombre = fields.Char(string="nombre_sector", size=60, help="Nombre del sector")
    descripcion = fields.Text(string="descripcion_sector", size=200, help="Descripción del sector")
    sectores_proyecto = fields.many2many("upobye.sector","Sector")