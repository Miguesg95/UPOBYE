# -*- coding: utf-8 -*-


from odoo import models, fields, api

class Proyecto(models.Model):
    _name = 'upobye.proyecto'
    _description = 'upobye.proyecto'

    name = fields.Char(string="Nombre", size=60, help="Nombre del proyecto")
    description = fields.Text(string="Descripción", size=200, help="Descripción del proyecto")
    sectores_id= fields.Many2many("upobye.sector",string="Sectores de este proyecto")
    contrato_id = fields.One2many('upobye.contrato', 'proyecto_id', 'Contrato')