# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TipoContrato(models.Model):
    _name = 'upobye.tipo_contrato'
    _description = 'upobye Tipo de Contrato'
    
    name = fields.Char(string="Nombre", size=60, help="Nombre Tipo Contrato")
    tipo = fields.Selection([('indOrdinario','indefinido ordinario'),
                            ('indIncentivado',' indefinido incentivado'),
                            ('fijoDiscontinuo','fijo discontinuo'),
                            ('contObra','Contrato de obra'),
                            ('contEventual','Contrato eventual'),
                            ('contInterinidad','Contrato de interinidad'),
                            ('contTempInc','Contrato temporal incentivado'),
                            ('contRelevo','Contrato de relevo'),
                            ('contFormacion','Contrato para la formación y el aprendizaje'),
                            ('contPracticas','Contrato en practicas'),
                                    ],'Tipo de contrato')
    description = fields.Text(string="Descripcion del contrato", required=True, help="breve descripcion")
    contrato_id = fields.One2many('upobye.contrato', 'tipo_contrato_id', 'Contrato')

