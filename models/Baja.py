# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Baja (models.Model):
    _name = 'upobye.baja'
    _description = 'Gestión de baja del empleado'

    name = fields.Char(string="Nombre del empleado",required=True, size=20, help="Nombre del empleado que solicita la baja")
    duracionDias = fields.Integer(string='Duración en días',required=True, help="Tiempo en días que dura la baja")
    fechaInicio = fields.Datetime(string="Fecha de inicio", required=True, autodate=True)
    fechaFin = fields.Datetime(string="Fecha de finalización", required=True, autodate=True)
    motivoBaja = fields.Text(string="Motivo", required=True, size=200, help="Motivo por el que se concedió la baja")

    contrato_id = fields.One2many('upobye.contrato', 'baja_id', 'Contrato')