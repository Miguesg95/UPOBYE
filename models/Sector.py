
from odoo import models, fields, api

class Sector(models.Model):
    _name = 'upobye.sector'
    _description = 'Sectores de UPOBYE'

    name = fields.Char(string="Nombre", size=60, help="Nombre del sector")
    description = fields.Text(string="Descripción", size=200, help="Descripción del sector")
    proyectos_id= fields.Many2many("upobye.proyecto",string="Proyectos de este sector")
    
    _sql_constraints = [('sector_name_unique','UNIQUE (name)','El nombre del sector debe ser único')]
