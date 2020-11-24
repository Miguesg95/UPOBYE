# -*- coding: utf-8 -*-


from odoo import models, fields, api

class proyecto(models.Model):
    _name = 'upobye.proyecto'
    _description = 'upobye.proyecto'

    name = fields.Char(string="nombre_proyecto", size=60, help="Nombre del proyecto")
    descripcion = fields.Text(string="descripcion_proyecto", size=200, help="Descripción del proyecto")
    sectores_id= fields.Many2many("upobye.sector",string="Sectores de este proyecto")
    sectores = fields.Selection([('agricola','Agricola'),
                      ('transportes', 'Transportes'),
                      ('sanitario', 'Sanitario'),],
                      'Sector')
    