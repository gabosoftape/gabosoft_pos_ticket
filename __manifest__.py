# -*- coding: utf-8 -*-
####################   Gabosoft      ####################
#    License:  OPL-1
####################   Gabosoft     ####################
#
#
#
{
    'name': 'POS Ticket Logo y codigo de barras',
    'summary': """POS Receipt with Barcode and Logo""",
    'version': '11.0.1.0',
    'description': """POS Recibos de punto de venta con codigo de barras """,
    'author': 'Gabosoft',
    'company': 'Gabosoft for Antidoto.',
    'website': 'gabosoft.com',
    'category': 'Point of Sale',
    'depends': ['base', 'point_of_sale'],
    'license': 'OPL-1',
    'data': [
    	'views/import.xml',
    	'views/pos_order.xml',
    ],
    'qweb': ['static/src/xml/posticket.xml'],
    'images': ['static/description/banner.png'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
