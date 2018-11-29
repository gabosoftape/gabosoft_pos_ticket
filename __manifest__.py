# -*- coding: utf-8 -*-
#
{
    'name': 'POS Ticket Logo and Barcode',
    'summary': """POS Receipt with Barcode and Logo""",
    'version': '11.0.1.0',
    'description': """POS Receipt with Barcode and Logo""",
    'author': 'AARSOL (Pvt) Limited.',
    'company': 'AARSOL (Pvt) Limited.',
    'website': 'http://www.aarsol.com',
    'category': 'Point of Sale',
    'depends': ['base', 'point_of_sale'],
    'license': 'OPL-1',
    'data': [
    	'views/import.xml',
    	'views/pos_order.xml',
    ],
    'qweb': ['point_of_sale/static/src/xml/pos.xml'],
    'images': ['static/description/banner.png'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
