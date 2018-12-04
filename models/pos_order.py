# -*- coding: utf-8 -*-
####################   AARSOL      ####################
#    AARSOL Pvt. Ltd.
#    Copyright (C) 2010-TODAY AARSOL(<http://www.aarsol.com>).
#    Author: Farooq Arif(<http://www.aarsol.com>)
#
#    It is forbidden to distribute, or sell copies of the module.
#
#    License:  OPL-1
####################   AARSOL      ####################

from odoo import api, fields, models, _
import base64
import json
import logging

_logger = logging.getLogger(__name__)

class pos_order(models.Model):
    _inherit = "pos.order"

    ean13 = fields.Char('Ean13')
    factura_numero = fields.Char('Numero de Factura')

    @api.model
    def _order_fields(self, ui_order):
        order_fields = super(pos_order, self)._order_fields(ui_order)

        if ui_order.get('ean13', False):
            order_fields.update({
                'ean13': ui_order['ean13']

            })


        return order_fields

fact_secuence = fields.Char('Secuencia 1', readonly=True)

@api.model
def create(self, vals):
    print "+++++++++++++++++++++++++++++++++++++++++++++++++"
    print "prepare inherit create function"
    print "change the name TI with sequence"
    vals['fact_secuence'] = self.env['ir.sequence'].next_by_code('secuencia1')
    print "Inherit complete"
    print "+++++++++++++++++++++++++++++++++++++++++++++++++"
    return super(secuencia1, self).create(vals)
