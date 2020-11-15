# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TipoContrato(models.Model):
    _name = 'upobye.TipoContrato'
    _description = 'upobye Tipo de Contrato'
    
    type = fields.Selection([('indOrdinario','indefinido ordinario'),
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
    description = fields.Text()
    