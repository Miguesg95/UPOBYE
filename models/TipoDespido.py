# -*- coding: utf-8 -*-

from odoo import models, fields, api



class TipoDespido(models.Model):
     _name = 'upobye.tipo_despido'
     _description = 'upobye.tipoDespido'

     name = fields.Char(string="forma",required=True,help="Tipo de despido")
     forma = fields.Selection([('disciplinario','Disciplinario'),
                                    ('objetivo','Objetivo'),
                                    ('colectivo','Colectivo')
                                    ],'Forma o tipo de despido')