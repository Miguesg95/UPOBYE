# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta, datetime

class Contrato(models.Model):

    _name = 'upobye.contrato'
    _description = 'upobye.contrato'
    
    sueldo  = fields.Float(string = "Sueldo", help="Sueldo del empleado", default=1110.00)
    jornada = fields.Char(string = "Duración de jornada", help="Media jornada, jornada completa...")
    fecha = fields.Datetime(string = "Fecha de inicio", default=fields.Date.today()) 
    dias_libres = fields.Integer(string = "Días libres")
    tiempo = fields.Datetime(string = "Fecha de cumplimiento del contrato", help="Fecha de cumplimiento de contrato")
    activo = fields.Boolean(string="Activo", help="Indica si el empleado se encuentra activo")

    baja_id = fields.One2many('upobye.baja', 'contrato_id', 'Bajas')
    despido_id = fields.One2many('upobye.despidos', 'contrato_id', 'Despidos')
    tipo_contrato_id = fields.Many2one('upobye.tipo_contrato', string="Tipo del contrato")
    puesto_id = fields.Many2one('upobye.puesto', string="Puesto")
    proyecto_id = fields.Many2one('upobye.proyecto', string='Proyecto')
    #empleado_id = fields.One2many('upobye.empleado', 'contrato_id', 'Empleado')

    @api.onchange('sueldo')
    def onchange_contrato(self):
        resultado={}
        if self.sueldo < 1109:
            resultado= {
                'value': {'sueldo':1109},
                'warning': {
                    'title':'Sueldo Incorrecto',
                    'message':'El salario mínimo legal es de 1109 Euros'
                }
            }
            return resultado