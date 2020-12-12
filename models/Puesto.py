# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Puesto (models.Model):
    _name = 'upobye.puesto'
    _description = 'Distintos Puestos'

    name = fields.Char(string="Nombre", required=True, size=60, help="Nombre puesto")
    ID = fields.Char(string="ID", required=True, size=40, help="ID")
    required = fields.Boolean(string="Necesario", help="¿Es un puesto que debe estar siempre ocupado?")
    qualification = fields.Text(string="Requisitos", size=300, help="requisitos del puesto")

    contrato_id = fields.One2many('upobye.contrato', 'puesto_id', 'Contrato')
    
    def btn_limpiarContratos(self):
        self.write({'contrato_id':[(5,)]})
    