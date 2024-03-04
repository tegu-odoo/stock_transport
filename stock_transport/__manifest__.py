{
    'name' : 'Transport Management System',
    'depends' : ['stock_picking_batch','fleet'],

    'data' : [
        'security/ir.model.access.csv',

        'views/fleet_vehicle_model_category_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_transport_menus.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
