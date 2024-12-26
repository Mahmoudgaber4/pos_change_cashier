
{
    'name': 'Pos Change Cashier',
    'version': '17.0.1.0.0',
    'summary': """Pos Change Cashier Task""",
    'description': """Pos Change Cashier Task.""",
    'author': 'Mahmoud Gaber',
    'depends': ['base', 'point_of_sale','hr'],
    'license': 'OPL-1',
    'data': ['views/hr_employee_inherit.xml',],
    'assets': {
        'web.assets_backend': [
        ],
        'point_of_sale._assets_pos': [
            'pos_change_cashier/static/src/js/change_cashier_btn.js',
            'pos_change_cashier/static/src/xml/change_cashier_btn.xml',
        ],
    },
    'images': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
