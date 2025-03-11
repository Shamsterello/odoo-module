{
    'name': 'Module1',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Module with text',
    'author': 'ishamilov',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/model.xml',
        'views/menu.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
