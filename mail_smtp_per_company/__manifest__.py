# -*- coding: utf-8 -*-
{
    'name': 'SMTP Server Per Company',
    'summary': 'SMTP Server Per Company',
    'description': 'SMTP Server Per Company.',

    'author': 'iPredict IT Solutions Pvt. Ltd.',
    'website': 'http://ipredictitsolutions.com',
    "support": "ipredictitsolutions@gmail.com",

    'category': 'Discuss',
    'version': '15.0.0.1.1',
    "depends": ['base', 'mail'],

    'data': [
        'security/mail_security.xml',
        'security/ir.model.access.csv',
        'views/mail_server_view.xml',
    ],

    'license': "OPL-1",
    'price': 20,
    'currency': "EUR",

    'installable': True,
    'auto_install': False,

    'images': ['static/description/main.png'],
    'pre_init_hook': 'pre_init_check',
}
