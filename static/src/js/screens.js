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
                var hoy = new Date();
                var fechalimite1EnMilisegundos = 1000 * 60 * 60 * 24 * 8;
                var fechalimite2EnMilisegundos = 1000 * 60 * 60 * 24 * 30;
                var suma1 = hoy.getTime() + fechalimite1EnMilisegundos;
                var suma2 = hoy.getTime() + fechalimite2EnMilisegundos;  //getTime devuelve milisegundos de esa fecha
                var fechalimite1 = new Date(suma1);
                var fechalimite2 = new Date(suma2);
                $('#caducidad_coupon1').html(fechalimite1);
                $('#caducidad_coupon2').html(fechalimite2);

                console.log("la fecha del cupon1 seria .."+fechalimite1);
                console.log("la fecha del cupon2 seria .."+fechalimite2);
            } catch (error) {
            }
        },

    });



});
