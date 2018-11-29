"use strict";
/*
    License: OPL-1
    author: farooq@aarsol.com
*/
odoo.define('gabosoft_pos_ticket.screens', function (require) {

    var models = require('point_of_sale.models');
    var screens = require('point_of_sale.screens');
    var core = require('web.core');
    var utils = require('web.utils');
    var round_pr = utils.round_precision;
    var _t = core._t;
    var gui = require('point_of_sale.gui');
    var qweb = core.qweb;


    screens.ReceiptScreenWidget.include({
        renderElement: function () {
            var self = this;
            this._super();
            this.$('.back_order').click(function () {
                var order = self.pos.get_order();
                if (order) {
                    self.pos.gui.show_screen('products');
                }
            });
        },
        show: function () {
            this._super();
            try {
                $("#barcode_img").barcode(this.pos.get('selectedOrder').ean13,"ean13");
            } catch (error) {
            }
        },

    });



});
