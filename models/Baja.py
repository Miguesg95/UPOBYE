# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Baja (models.Model):
    _name = 'upobye.Baja'
    _description = 'Gestión de baja del empleado'

    import datetime
    duracionDias = fields.Integer(string='Duración',required=True, help="Tiempo en días que dura la baja")
    fechaInicio = fields.Datetime(string="Fecha de inicio", required=True, autodate=True)
    fechaFin = fechaInicio + datetime.timedelta(days=duracionDias)
    motivoBaja = fields.Text(string="Motivo", required=True, help="Motivo por el que se concedió la baja")