# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Puesto (models.Model):
    _name = 'upobye.puesto'
    _description = 'Distintos Puestos'
    
    name = fields.Char(string="Nombre",required=True, help="Nombre puesto")
    ID = fields.Char(string="ID", required=True, help="ID")
    required = fields.Boolean(string="Necesario", help="¿Es necesario o no?")
    qualification = fields.Text(string="Requisitos", required=True, help="requisitos del puesto")

    contrato_id = fields.One2many('upobye.contrato', 'puesto_id', 'Contrato')