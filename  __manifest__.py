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
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        #'views/sector_view.xml',
        'security/security.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
