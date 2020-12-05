# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Contrato(models.Model):

    _name = 'upobye.contrato'
    _descripcion = 'upobye.contrato'
    
    sueldo  = fields.Float(string = "Sueldo", help="Sueldo del empleado")
    jornada = fields.Char(string = "Duración de jornada", help="Media jornada, jornada completa...")
    fecha = fields.Date(default = "") 
    dias_libres = fields.Integer(string = "Días libres")
    tiempo = fields.Date(help="Fecha de cumplimiento de contrato")
    activo = fields.Boolean(string="Activo", help="Indica si el empleado se encuentra activo")

    #baja_id = fields.Many2one('upobye.baja', 'contrato_id', 'Baja')
    #despido = fields.One2many('upobye.despido', 'upobye.contrato', 'Despidos')
    tipo_contrato_id = fields.Many2one('upobye.tipo_contrato', 'contrato_id', 'TipoContrato')
    #puesto_id = fields.One2many('upobye.puesto', 'upobye.contrato', 'Puesto')
    #proyecto_id = fields.One2many('upobye.proyecto', 'upobye.contrato', 'Proyecto')
    #empleado_id = fields.One2many('upobye.empleado', 'upobye.contrato', 'Empleado')

    @api.depends()
    def __init__(self, Fecha, Tiempo):
        self.duracion = (Tiempo - Fecha)
    