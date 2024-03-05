{
    'name' : 'Stock Inventory',
    'depends' : ['stock'],

    'data' : [
        'security/ir.model.access.csv',

        'views/res_config_settings_views.xml',
    ],

    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
