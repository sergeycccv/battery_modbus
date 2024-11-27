            # for i in range(0, 3):

            #     if config.has_option('CH1', 'i_start_discharge'):
            #         self.i_start_discharge_list[0] = config.getfloat('CH1', 'i_start_discharge')
            #         # self.settings_ch.edit_i_start_discharge.setText(str(self.i_start_discharge_list))
            #     else:
            #         self.i_start_discharge_list[0] = 0.025
            #         # self.settings_ch.edit_i_start_discharge.setText('0.025')

            #     if config.has_option('CH1', 'u_stop_discharge'):
            #         self.u_stop_discharge_list[0] = config.getfloat('CH1', 'u_stop_discharge')
            #         # self.settings_ch.edit_u_stop_discharge.setText(str(self.u_stop_discharge_list))
            #     else:
            #         self.u_stop_discharge_list[0] = 10.8
            #         # self.settings_ch.edit_u_stop_discharge.setText('10.8')

            #     if config.has_option('CH1', 'i_stop_charge'):
            #         self.i_stop_charge_list[0] = config.getfloat('CH1', 'i_stop_charge')
            #         # self.settings_ch.edit_i_stop_charge.setText(str(self.i_stop_charge_list))
            #     else:
            #         self.u_stop_discharge_list[0] = 0.025
            #         # self.settings_ch.edit_i_stop_charge.setText('0.025')

            # QMessageBox.warning(self, 'Предупреждение', 'Ошибка чтения настроек из ini-файла:\n' + str(e))


            # config.add_section('CH1')
            # config.set('CH1', 'i_start_discharge', str(win.i_start_discharge_list[0]))
            # config.set('CH1', 'u_stop_discharge', str(win.u_stop_discharge_list[0]))
            # config.set('CH1', 'i_stop_charge', str(win.i_stop_charge_list[0]))

            # config.add_section('CH2')
            # config.set('CH2', 'i_start_discharge', str(win.i_start_discharge_list[1]))
            # config.set('CH2', 'u_stop_discharge', str(win.u_stop_discharge_list[1]))
            # config.set('CH2', 'i_stop_charge', str(win.i_stop_charge_list[1]))

            # config.add_section('CH3')
            # config.set('CH3', 'i_start_discharge', str(win.i_start_discharge_list[2]))
            # config.set('CH3', 'u_stop_discharge', str(win.u_stop_discharge_list[2]))
            # config.set('CH3', 'i_stop_charge', str(win.i_stop_charge_list[2]))

            # config.add_section('CH4')
            # config.set('CH4', 'i_start_discharge', str(win.i_start_discharge_list[3]))
            # config.set('CH4', 'u_stop_discharge', str(win.u_stop_discharge_list[3]))
            # config.set('CH4', 'i_stop_charge', str(win.i_stop_charge_list[3]))

            # QMessageBox.warning(self, 'Предупреждение', 'Ошибка записи настроек в ini-файл:\n' + str(e))


                # if widget.objectName() == 'u_start_ch1':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('0, 255, 0'))
                # if widget.objectName() == 'u_current_ch1':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('255, 255, 255'))
                # if widget.objectName() == 'i_current_ch1':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('255, 255, 255'))
                # if widget.objectName() == 'p_current_ch1':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('255, 255, 255'))
                # if widget.objectName() == 'c_recharge_ch1':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('0, 255, 0'))
                # if widget.objectName() == 'w_recharge_ch1':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('0, 255, 0'))
                # if widget.objectName() == 'c_discharge_ch1':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('255, 135, 0'))#255, 110, 255
                # if widget.objectName() == 'w_discharge_ch1':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('255, 135, 0'))
                # if widget.objectName() == 'c_charge_ch1':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('100, 100, 100'))
                # if widget.objectName() == 'w_charge_ch1':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('100, 100, 100'))


                # if widget.objectName() == f'u_start_{channel}':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('100, 100, 100'))
                # if widget.objectName() == f'u_current_{channel}':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('100, 100, 100'))
                # if widget.objectName() == f'i_current_{channel}':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('100, 100, 100'))
                # if widget.objectName() == f'p_current_{channel}':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('100, 100, 100'))
                # if widget.objectName() == f'c_recharge_{channel}':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('100, 100, 100'))
                # if widget.objectName() == f'w_recharge_{channel}':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('100, 100, 100'))
                # if widget.objectName() == f'c_discharge_{channel}':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('100, 100, 100'))
                # if widget.objectName() == f'w_discharge_{channel}':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('100, 100, 100'))
                # if widget.objectName() == f'c_charge_{channel}':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('100, 100, 100'))
                # if widget.objectName() == f'w_charge_{channel}':
                #     widget.setProperty('styleSheet', self.set_styleSheet_indicator('100, 100, 100'))



        # self.findChild(QToolButton, f'btn_write_settings_ch{channel}').setEnabled(False)
