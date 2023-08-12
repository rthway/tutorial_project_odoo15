{
    'name': 'Tutorial Project',
    'version': '1.0',
    'summary': 'Tutorial project to learn odoo',
    'description': 'Tutorial project to learn odoo',
    'author': 'Roshan Kumar Thapa',
    'website': 'https://github.com/rthway',
    'sequence': '-531',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/staff_view.xml',
        'views/menu.xml',
    ],
    'application': True,
    'auto_install': False,
    'icon': 'tutorial_project/static/description/icon.png',
}