# -*- coding: utf-8 -*-
{
    'name': "military-module",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "eugensemenov",
    'website': "https://github.com/eugensemenov",

    'category': 'HR',
    'version': '0.2',

    'depends': [
        'base',
        'contacts'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/battalion_views.xml',
        'views/company_views.xml',
        'views/platoon_views.xml',
        'views/menu_views.xml'
    ],
}
