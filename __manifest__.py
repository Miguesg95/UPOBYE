# -*- coding: utf-8 -*-
{
    'name': "UPOBYE",

    'summary': """
        Módulo de gestión de despidos""",

    'description': """
        El objetivo de este módulo es facilitar la gestión de despidos, bajas y vacaciones
    """,

    'author': "GRUPO2",
    'website': "https://github.com/Miguesg95/UPOBYE.git",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/reports.xml',
        'reports/Despidos_report.xml',
        'views/Experiencia_view.xml',
        'views/Baja_view.xml',
        'views/Titulacion_view.xml',
        'views/sector_view.xml',
        'views/proyecto_view.xml',
        'views/Despidos_view.xml',
        'views/Idioma_view.xml',
        'views/Puesto_view.xml',
        'views/TipoContrato_view.xml',
        'views/TipoDespido_view.xml',
        'views/Contrato_view.xml',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
