# -*- coding: utf-8 -*-

=======
>>>>>>> Stashed changes
from odoo import models, fields, api

class proyecto(models.Model):
    _nombre = 'upobye.proyecto'
    _descripcion = 'upobye.proyecto'

    nombre = fields.Char(string="nombre_proyecto", size=60, help="Nombre del proyecto")
    descripcion = fields.Text(string="descripcion_proyecto", size=200, help="Descripción del proyecto")
    sectores_proyecto = fields.One2many("UPOBYE.sector", "Sector")
    sectores = fields.Selection([('agricola','Agricola'),
                      ('transportes', 'Transportes'),
                      ('sanitario', 'Sanitario'),],
                      'Sector')
    
