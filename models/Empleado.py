# -*- coding: utf-8 -*-


from odoo import models, fields, api

class Empleado(models.Model):
    _name = 'upobye.empleado'
    _description = 'Empleados'

    name = fields.Char(String='DNI', size=200, required=True, help='Dni del empleado')
    nomEmpleado =  fields.Char(String='Nombre completo', size=200, required=True, help='Nombre del empleado')
    telefono = fields.Char(String='Telefono', size=200, help='Telefono del empleado')
    nSeguridadSocial = fields.Char(String='Número de la seguridad social', size=200)
    correo = fields.Char(String='Correo Electrónico', size=200)
    cuentaBancaria = fields.Char(String='Número de cuenta bancaria', size=200)

    experiencia_id = fields.One2many('upobye.experiencia', 'empleado_id', 'Experiencias')
    titulación_id= fields.One2many('upobye.titulacion', 'empleado_id', 'Titulaciones')
    idioma_id= fields.One2many('upobye.idioma', 'empleado_id', 'Idiomas')
    contrato_id = fields.One2many('upobye.contrato', 'empleado_id', 'Contratos')
    
    
