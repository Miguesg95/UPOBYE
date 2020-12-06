# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Contrato(models.Model):

    _name = 'upobye.contrato'
    _description = 'upobye.contrato'
    
    sueldo  = fields.Float(string = "Sueldo", help="Sueldo del empleado")
    jornada = fields.Char(string = "Duración de jornada", help="Media jornada, jornada completa...")
    fecha = fields.Date(default = "") 
    dias_libres = fields.Integer(string = "Días libres")
    tiempo = fields.Date(help="Fecha de cumplimiento de contrato")
    activo = fields.Boolean(string="Activo", help="Indica si el empleado se encuentra activo")

    baja_id = fields.Many2one('upobye.baja', string="Bajas")
    despido_id = fields.Many2one('upobye.despidos', string="Despidos")
    tipo_contrato_id = fields.Many2one('upobye.tipo_contrato', string="Tipo del contrato")
    puesto_id = fields.Many2one('upobye.puesto', string="Puesto")
    proyecto_id = fields.Many2one('upobye.proyecto', string='Proyecto')
    empleado_id = fields.One2many('upobye.empleado', 'contrato_id', 'Empleado')
