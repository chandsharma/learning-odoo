# -*- coding: utf-8 -*-
{
    'name': "hospital_management",

    'summary': """Manage yor Staff and Patients on the GO.""",

    'description': """
                Custom upgradable module with lots of features.\n
                Hospital Management Module for Odoo.\n
                manage yor Staff and Patients on the GO.
    """,

    'author': "Chandan",
    'website': "http://www.techneith.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
