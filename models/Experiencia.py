# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Experiencia (models.Model):  
    _name = 'upobye.Experiencia'
    _description = 'Recoge una experiencia laboral del empleado'  

    nombre = fields.Char(string="Nombre",required=True,help="Nombre de la ocupación que desea acreditar")
    certificacion = fields.Char(string="Certificado por",required=True,help="Nombre de la identidad que certifica la experiencia")
    fechaInicio = fields.Datetime(string="Fecha de inicio", required=True, autodate=True)
    fechaFin = fields.Datetime(string="Fecha de finalización", required=True, autodate=True)
    duracionDias = fields.Integer(string='Duración',required=True, help="Tiempo en días que ejerció ese trabajo")
    jornada = fields.Selection([
        ('completa', 'Completa'),
        ('media', 'Media'),
    ],string="Jornada", default='completa', help="Horas de duración de la jornada laboral")

