# -*- coding: utf-8 -*-


from odoo import models, fields, api

class Empleado(models.Model):
    _name = 'upobye.empleado'
    _description = 'upobye.empleado'

    contrato_id = fields.Many2one('upobye.contrato', string="Contratos")