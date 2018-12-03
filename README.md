gabosoft_pos_ticket


agregar a vista en backend ..

<h1>Resolucion de facturacion</h1>
                    <div class="row mt16 o_settings_container">
                      <div class="col-xs-12 col-md-6 o_setting_box">
                        <div class="o_setting_left_pane">
                          <field name="x_bill_resolution"/>
                        </div>
                        <div class="o_setting_right_pane" >
                          <label for="x_bill_resolution"/>
                          <div class="text-muted">
                                   Agregar resolucion de facturacion expedida por la DIAN
                                </div>
                          <div class="content-group mt16" attrs="{'invisible': [('x_bill_resolution','=',False)]}" >
                              <div>
                                  <label string="Prefijo" for="x_prefix_resolution" class="col-md-2 o_light_label"/>
                                  <field name="x_prefix_resolution" placeholder="e.g. TT, XXCD, CMS"/>
                              </div>
                              <div>
                                  <label string="Desde" for="x_ind_resolution" class="col-md-2 o_light_label"/>
                                  <field name="x_ind_resolution"/>
                              </div>
                              <div>
                                   <label string="Hasta" for="x_end_resolution" class="col-md-2 o_light_label"/>
                                   <field name="x_end_resolution" />
                              </div>
                              </div>

                        </div>
                      </div>
                    </div>
