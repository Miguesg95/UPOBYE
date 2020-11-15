from odoo import models, fields, api

def sector(models.Model)
    _nombre = 'upobye.sector'
    _descripcion = 'upobye.sector'

    nombre = fields.Char(string="nombre_sector", size=60, help="Nombre del sector")
    descripcion = fields.Text(string="descripcion_sector", size=200, help="Descripción del sector")
    
    