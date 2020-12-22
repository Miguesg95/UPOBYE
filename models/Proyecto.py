# -*- coding: utf-8 -*-


from odoo import models, fields, api

class Proyecto(models.Model):
    _name = 'upobye.proyecto'
    _description = 'upobye.proyecto'

    name = fields.Char(string="Nombre", size=60,required=True, help="Nombre del proyecto")
    description = fields.Text(string="Descripción", required=True, size=200, help="Descripción del proyecto")
    sectores_id= fields.Many2many("upobye.sector",string="Sectores de este proyecto")
    contrato_id = fields.One2many('upobye.contrato', 'proyecto_id', 'Contrato')

    @api.constrains('description')
    def _size_description(self):
        if len(self.description)<10:
            raise models.ValidationError('La descripción debe ser más extensa.')
